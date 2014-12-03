from math import fabs
from vanetController import *
from time import time
from threading import Thread
from collections import deque
import sys

#time between broadcasts (10 ms)
BCAST_PER = 0.01
RANGE_BCAST_PER = 0.1
#time limit (sec)
TIME_LIM = 30
EPOCH_MOD = 100000
OLD_SEQ_DIFF = 10
#Comm range
COMM_DIST = 100
#coord indices
X, Y = 0, 1
#Y-position (lane) constants
LEFT, RIGHT = 0, 1
#length of truck
TRUCK_LEN = 25
BUF_DIST = 5
#allowable platoon distance range
PLAT_DIST = (TRUCK_LEN + 10, TRUCK_LEN + 20)
#motion constants
PLAT_SPD = 30
MAX_ACCEL = 1
MAX_DECEL = -3.5
SLOW_DOWN = (MAX_DECEL, 0)
SPEED_UP = (MAX_ACCEL, 0)
FALL_BACK = 3
CATCH_UP = 3
#TruckNode.packetDrops index constants
DROP, RECV = 0, 1
#Period over which to calculate drop rates
DROP_PER = 1



'''
X refers to the axis along the road.
Y refers to the axis across the road (lane position).
'''
class TruckNode:
	
	def __init__(self, id, x, v, a, config='config.txt'):
		#network controller
		self.vc = VanetController()
		#position (px, py)
		self.x = x
		self.sendX = self.x
		#velocity (vx, vy)
		self.v = v
		self.sendV = self.v
		#acceleration (ax, ay)
		self.a = a
		self.sendA = self.a
		#unique 16-bit ID (address)
		self.id = id
		#platoon id
		self.platId = id
		#TruckNode identifiers
		self.leader = 0
		self.follower = 0
		self.leaderCand = 0
		self.followerCand = 0
		#neighbor cache {id: TruckNode}
		self.cache = {}
		self.neighbors = deque() #set up a double-ended queue; holds every truck within talking distance of the node
		#sequence number
		self.seqNum = 0
		self.time = 0
		#related to MPR
		self.actAsMPR = False #default to false until told to commission self as an MPR
		self.oneHopNeighborCache = {} #list of known single-hop neighbors; holds a caches full node entry for each.
		self.multiHopNeighborCache = {} #list of known multi-hop neighbors
		self.primaryMPR = 0 #ID of one of the closest MPRs, potentially including self. Logic will use this as the primary MPR listing
		self.secondaryMPR = 0 #ID of another of the closest MPRs, hopefully excluding self. Logic will use this as the secondary MPR listing.
		self.pushForwardNodeToBeMPR = False #set ot true to have the Ctrl thread push out a packet to the most forward node in reach to be an MPR
		#dict maps neighbor ids to [numDrops, numReceives]
		self.packetDrops = {}
		self.bcastCount = 0
		#config file
		self.confPath = config
		self.configFile = None
		#FOR DEBUGGING
		self.adjustmentMade = -1
	
	'''
	Sets up the TruckNode to wait for start signal.
	Completes all initial setup that can be done
	prior to runtime.
	'''
	def initialize(self):
		#state output file
		self.logFile = open(str(self.id) + '.log', 'w')
		self.vc.setupSocket(self.id, TIME_LIM)
		self.ctrlThread = Thread(target=self.controlThread)
		self.lstnThread = Thread(target=self.listenerThread)
		if self.vc.awaitStart():
			print 'Starting Simulation! Running for', TIME_LIM, 'seconds...'
			self.run()
	
	'''
	Runs the TruckNode's two threads,
	ctrlThread and lstnThread.
	'''
	def run(self):
		curTime = time()
		self.time = curTime
		self.writeState()
		self.startTime = curTime
		self.lastUpdate = curTime
		self.ctrlThread.start()
		self.lstnThread.start()
		self.ctrlThread.join()
	
	'''
	This is the main method for ctrlThread.
	This thread controls all TruckNode data
	updating and decision-making, as well as
	telling the VanetController when to broadcast
	the TruckNode's data.
	'''
	def controlThread(self):
		self.lastBroadcast = time()
		self.bcastCount = 0
		while time() - self.lastBroadcast < 0.001 * self.id % 10:
			pass
		self.lastBroadcast = time()
		while time() < self.startTime + TIME_LIM:
			while time() - self.lastBroadcast < BCAST_PER:
				pass
			try:
				desiredMPR = self.seekPotentialMPR()
				if self.amIRearmostNodeInRange():
					self.pushForwardNodeToBeMPR = True
					self.actAsMPR = True
				if desiredMPR > 10000 and self.pushForwardNodeToBeMPR and self.actAsMPR:
					self.initiateNextForwardMPR(desiredMPR)
					self.pushForwardNodeToBeMPR = False
				self.sendData()
				self.nextTimestep()
				self.checkDropRates()
				if self.bcastCount == RANGE_BCAST_PER / BCAST_PER:
					self.blanketSendData()
			except Exception as e:
				print "Exception in ControlThread:"
				print e
		self.logFile.close()
		print "Simulation finished."
		print "Drop rate:", float(self.vc.drops) / (self.vc.drops + self.vc.recvs)
		print "Throughput:", float(self.vc.recvs) / TIME_LIM;
	
	'''
	This is the main method for lstnThread.
	It controls the reception of packets
	from other TruckNodes, and updates
	the caches with the latest received
	information.
	'''
	def listenerThread(self):
			while time() < self.startTime + TIME_LIM:
				try:
					pkt, prev = self.vc.receive(self.x, self.packetDrops, self.id)
					if pkt:
						#if the PREV field of the pkt was 0, then it was a broadcast, and we can update
						#similarly, if DST field of the pkt was self.id, then it was meant for me, and we should store the information/process it
						node = self.nodeFromPacket(pkt)
						doPutInOneHopCache = self.isOneHop(pkt)
						pktType = self.amIMeantToBeAnMPR(pkt) #will also set self to an MPR as necessary
						if (pktType == YES_MPR): #if the packet type is a type that dictates self as an MPR...
							#do not change if self is an MPR here; it's done in the amIMeantToBeAnMPR logic
							#self.pushForwardNodeToBeMPR = True #this, combined with the right conditional where a node is ahead, will trigger self to search for & set another MPR
							self.updateCache(node, doPutInOneHopCache)
							self.addThisAsNearbyMPR(node)
						elif (pktType == NO_MPR): #if the packet is an MPR-setter, but did NOT dictate self as an MPR...
							#do not change if self is an MPR here; it's done in the amIMeantToBeAnMPR logic
							self.updateCache(node, doPutInOneHopCache)
							self.addThisAsNearbyMPR(node) #still checks if the node was an MPR and should be added to our cache
						elif (pktType == NORMALPKT): #if the packet is a normal packet that has nothing to do with choosing MPRs...
							if node.id != self.id:
								self.updateCache(node, doPutInOneHopCache)
								self.vc.oneHopNeighborCache = self.oneHopNeighborCache #note that we update the caches stored within the VC, too
								self.vc.multiHopNeighborCache = self.multiHopNeighborCache #still updating the caches stored within the VC
								self.addThisAsNearbyMPR(node) #still checks if the node was an MPR and should be added to our cache
					#self.cleanCache()
				except Exception as e:
					print "Exception in ListenerThread:"
					print e
	
	'''
	Sends self data and packets to be forwarded
	to all neighbor nodes. [Broadcast mode].
	Also sends self data and packets to be forwarded
	to all inner-platoon nodes. [PB Mode].
	'''
	def sendData(self):
		self.lastBroadcast = time()
		if self.actAsMPR == True: #we broadcast almost universally if we are an MPR, and we insert ourself as the sending MPR
			for neighbor in list(self.neighbors):
			    self.vc.sendData(neighbor, self.seqNum, self.id, neighbor, self.id, self.id, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA) #send data like normal
			    self.vc.forwardPackets(neighbor, self.id, MANIP_MPR_FIELD) #and forward all the packets we caught, just in case
		elif self.primaryMPR == 0 and self.secondaryMPR == 0: #if an MPR isn't known OR IF self is the MPR, broadcast to all known nodes within range
		    for neighbor in list(self.neighbors):
			    self.vc.sendData(neighbor, self.seqNum, self.id, neighbor, self.id, NO_KNOWN_MPR, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA) #send data like normal
			    self.vc.forwardPackets(neighbor, self.id, KEEP_MPR_FIELD) #and forward all the packets we caught, just in case
		elif self.primaryMPR > 10000 or self.secondaryMPR > 10000: #if the MPR is known, and it isn't "self", then...send it out via MPR. We do not forward other packets, though we may return a reply.
			if self.primaryMPR > 10000: #use the primaryMPR field as the PORT [first field in sendData and forwardPackets] to which you send packets to get them out, and set SRCMPR to 0...let the MPR update it itself to avoid accidental lies!
				self.vc.forwardPackets(self.primaryMPR, self.id, MANIP_MPR_FIELD)
				for neighbor in list(self.neighbors):
					self.vc.sendData(self.primaryMPR, self.seqNum, self.id, neighbor, self.id, SENDING_TO_MPR, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA)
			elif self.secondaryMPR > 10000: #use the secondaryMPR field similarly to how you would use the primaryMPR variable above.
				self.vc.forwardPackets(self.secondaryMPR, self.id, MANIP_MPR_FIELD)
				for neighbor in list(self.neighbors):
					self.vc.sendData(self.secondaryMPR, self.seqNum, self.id, neighbor, self.id, SENDING_TO_MPR, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA)
		self.vc.clearTBF()
		self.bcastCount += 1
	
	'''
	Sends self data to all ports. This will
	identify self to any previously out of
	range nodes that are now in range.
	'''
	def blanketSendData(self):
		self.vc.blanketBroadcast(self.seqNum, self.id, self.primaryMPR, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA)
	
	'''
	Builds a TruckNode object from an
	unpacked data packet.
	'''
	def nodeFromPacket(self, pkt):
		node = TruckNode(pkt[SRC], (pkt[Xx], pkt[Xy]), (pkt[Vx], pkt[Vy]), (pkt[Ax], pkt[Ay]))
		node.seqNum = pkt[SEQ]
		node.platId = pkt[PLAT]
		node.leader = pkt[LEAD]
		node.follower = pkt[TRAIL]
		if pkt[SRCMPR] == pkt[SRC]:
			node.actAsMPR = True #for the purposes of knowing that the node is an MPR, for storage in the cache.
		elif pkt[PREV] != BLANKET and pkt[PREV] == pkt[SRCMPR]:
			node.actAsMPR = True
		else:
			node.actAsMPR = False #we treat any MPR that required more than a hop as just another node!
		return node
	
	'''
	Updates the cached copy of a given TruckNode.
	Also determines if any properties change
	as a result of this update.
	'''
	def updateCache(self, node, doPutInOneHopCache):
		if fabs(self.xDistance(node)) < COMM_DIST or node.id in self.neighbors:
			if node.id not in list(self.neighbors):
				self.neighbors.append(node.id) #pretty much contains every node within communication distance
				if (node.primaryMPR != 0) and (node.primaryMPR == self.primaryMPR):
					self.oneHopNeighborCache[node.id] = node #add or update one-hop neighbor cache if they share the same MPR
				#print "Added", node.id, "to neighbor list at", self.time % EPOCH_MOD
				#print "\tSelfPos, NbrPos:", self.x, node.x
			if self.cache.has_key(node.id):
				self.cache[node.id] = node
			else:
				self.cache[node.id] = node
			self.updateLeader(node)
			self.updateFollower(node)
			
		if doPutInOneHopCache:
			self.oneHopNeighborCache[node.id] = node
		elif not doPutInOneHopCache:
		    self.multiHopNeighborCache[node.id] = node
	
	'''
	Calculates average drop rates for each neighbor
	over a given period, DROP_PER. If above a certain
	threshold, DROP_T, the neighbor is removed.
	'''
	def checkDropRates(self):
		if self.bcastCount >= int(DROP_PER / BCAST_PER):
			for id in self.packetDrops:
				if id in self.neighbors and float(self.packetDrops[id][DROP]) / self.packetDrops[id][RECV] >= DROP_T:
					self.neighbors.remove(id)
					#print "Removed", id, "from neighbor list at", self.time % EPOCH_MOD
					#print "\tSelfPos, NbrPos:", self.x, self.cache[id].x
				self.packetDrops[id][DROP] = 0
				self.packetDrops[id][RECV] = 0.001
			self.bcastCount = 0
	
	'''
	This setter method for self.leader ensures that
	all changes to self.leader are more than simply
	spur-of-the-moment decisions.
	'''
	def setLeader(self, newLead):
		if self.leaderCand == newLead:
			self.leader = newLead
		self.leaderCand = newLead
		return self.leader == newLead
	
	'''
	This setter method for self.follower ensures that
	all changes to self.follower are more than simply
	spur-of-the-moment decisions.
	'''
	def setFollower(self, newFollow):
		if self.followerCand == newFollow:
			self.follower = newFollow
		self.followerCand = newFollow
		return self.follower == newFollow
	
	
	'''
	If node is immediately in front of self,
	update self.leader. If current leader is
	no longer valid, reset.
	'''
	def updateLeader(self, node):
		if self.leader and self.platId == self.id and self.cache[self.leader].x[Y] != self.x[Y] \
		or self.leader and self.cache[self.leader].seqNum < self.seqNum - OLD_SEQ_DIFF:
			#print "Reset leader at", self.time % EPOCH_MOD
			self.leader = 0
		if node and node.x[Y] == self.x[Y] and node.x[X] > self.x[X]:
			if not self.leader:
				if self.setLeader(node.id):
					#print "Set leader to", self.leader, "at", self.time % EPOCH_MOD
					pass
			elif self.cache.has_key(self.leader) and self.cache[self.leader].x[X] > node.x[X]:
				if self.setLeader(node.id):
					#print "Set leader to", self.leader, "at", self.time % EPOCH_MOD
					pass
	
	'''
	If node is immediately behind self,
	update self.follower. If current
	follower is no longer valid, reset.
	'''
	def updateFollower(self, node):
		if self.follower and self.cache[self.follower].platId != self.platId and self.cache[self.follower].x[Y] != self.x[Y]:
			#print "Reset follower at", self.time % EPOCH_MOD
			self.follower = 0
		if node and node.x[Y] == self.x[Y] and node.x[X] < self.x[X]:
			if not self.follower:
				if self.setFollower(node.id):
					#print "Set follower to", self.follower, "at", self.time % EPOCH_MOD
					pass
			if self.cache.has_key(self.follower) and self.cache[self.follower].x[X] < node.x[X]:
				if self.setFollower(node.id):
					#print "Set follower to", self.follower, "at", self.time % EPOCH_MOD
					pass
	
	'''
	Updates position, velocity, and acceleration
	based on context. Writes to logFile.
	'''
	def nextTimestep(self):
		curTime = time()
		step = curTime - self.lastUpdate
		self.lastUpdate = curTime
		self.syncToSend()
		self.adjustSelf()
		self.x = (self.x[X] + self.v[X] * step, self.x[Y] + self.v[Y] * step)
		self.v = (self.v[X] + self.a[X] * step, self.v[Y] + self.a[Y] * step)
		self.seqNum += 1
		self.time = time()
		self.writeState()
	
	'''
	Syncs data to be sent with actual data.
	'''
	def syncToSend(self):
		self.sendX = self.x
		self.sendV = self.v
		self.sendA = self.a
	
	'''
	Make state-based decisions to
	affect motion and platooning.
	'''
	def adjustSelf(self):
		#DEBUG
		#if self.leader and 0 <= self.cache[self.leader].x[X] - self.x[X] <= 25 and self.cache[self.leader].x[Y] == self.x[Y]:
		#	print "CRASH WITH", self.leader, "at", self.time
		#	print "\tDistance", self.cache[self.leader].x[X] - self.x[X]
		#DEBUG
		self.adjustmentMade = -1
		immLead = self.immPlatoonLeader()
		if immLead:
			immLead = self.cache[immLead]
			self.stayInPlatoon(immLead)
		elif self.leader:
			immLead = self.cache[self.leader]
			self.avoidCollision(immLead)
			self.adjustmentMade += 0.5
		
		if self.isNotInPlatoon():
			self.adjustmentMade = 3
			platNode = self.findPlatoon()
			if platNode:
				self.adjustmentMade = 4
				if self.setLeader(platNode.id):
					self.platId = platNode.platId
			else:
				self.adjustmentMade = 5
				#try to form a platoon with self.leader, if they're not in a platoon yet (their platId is their own)
				if immLead and immLead.id in self.neighbors and immLead.platId == immLead.id:
					self.platId = immLead.platId
					self.adjustmentMade = 6
				else:
					#no one is in front of you, get into right lane and let any platoons catch up to you
					if not self.laneBlocked(RIGHT, (self.x[X], self.x[X] - TRUCK_LEN)):
						self.x = (self.x[X], RIGHT)
						self.adjustmentMade = 7
		elif self.isJoiningPlatoon():
			self.adjustmentMade = 8
			platNode = self.cache[self.leader]
			if self.xDistance(platNode) > PLAT_DIST[0]:
				self.adjustmentMade = 9
				blockingNode = self.laneBlocked(platNode.x[Y], (self.x[X], self.x[X] - TRUCK_LEN))
				if not blockingNode:
					self.joinPlatoon(platNode)
					self.adjustmentMade = 10
				else:
					self.sendX = (max(blockingNode.x[X] + 1, self.x[X]), platNode.x[Y])
					self.adjustmentMade = 11
		elif self.isPlatoonLeader():
			self.adjustmentMade = 12
			if self.x[Y] == LEFT:
				self.adjustmentMade = 13
				#someone behind you wants to make a platoon with you, merge right if there's enough space
				if not self.laneBlocked(RIGHT, (self.x[X], self.x[X] - 2 * TRUCK_LEN - PLAT_DIST[0])):
					self.x = (self.x[X], RIGHT)
					self.adjustmentMade = 14
			elif self.leader:
				self.adjustmentMade = 15
				immLead = self.cache[self.leader]
				self.mergeIntoPlatoon(immLead)
			else:
				self.adjustmentMade = 16
				self.accelerate((PLAT_SPD - self.v[X], 0))
	
	'''
	If self is in a platoon and following another
	TruckNode, adjust to stay within the acceptable
	distance range.
	'''
	def stayInPlatoon(self, immLead):
		self.platId = immLead.platId
		self.avoidCollision(immLead)
		if self.x[Y] != immLead.x[Y] and self.x[X] < immLead.x[X] and not self.laneBlocked(immLead.x[Y], (self.x[X], self.x[X] - TRUCK_LEN)):
			self.x = (self.x[X], immLead.x[Y])
	
	'''
	If self is not in a platoon, avoid overrunning
	any car in front of self, and do not continue
	slowing down unnecessarily.
	'''
	def avoidCollision(self, immLead):
		d = self.xDistance(immLead)
		if d < PLAT_DIST[0]:
			self.adjustmentMade = 0
			self.accelerate((min(0, immLead.v[X] + immLead.a[X] - self.v[X] - FALL_BACK), self.a[Y]))
		elif d > PLAT_DIST[1]:
			self.adjustmentMade = 1
			self.accelerate((immLead.v[X] + immLead.a[X] - self.v[X] + CATCH_UP, self.a[Y]))
		else:
			self.adjustmentMade = 2
			self.accelerate((immLead.v[X] - self.v[X], self.a[Y]))
		#if self.willCrash():
		#	if self.x[Y] == RIGHT and not self.laneBlocked((self.x[X], self.x[X] - TRUCK_LEN), LEFT):
		#		self.x = (self.x[X], LEFT)
		#		self.leader = 0
		#		self.leaderCand = 0
		#		self.follower = 0
		#		self.followerCand = 0
		#		self.platId = self.id
		#	elif self.x[Y] == LEFT and not self.laneBlocked((self.x[X], self.x[X] - TRUCK_LEN), RIGHT):
		#		self.x = (self.x[X], RIGHT)
		#		self.leader = 0
		#		self.leaderCand = 0
		#		self.follower = 0
		#		self.followerCand = 0
		#		self.platId = self.id
		#	else:
		#		print "NOOOOOOOOOOOO *raises arms in front of face*"
	
	'''
	
	'''
	def willCrash(self):
		if self.leader:
			lead = self.cache[self.leader]
			return 0 < self.xDistance(lead) < self.v[X] - lead.v[X]
		else:
			return False
	
	'''
	Returns True if self is not in a platoon
	and False otherwise.
	'''
	def isNotInPlatoon(self):
		return self.x[Y] == LEFT and self.platId == self.id# and not (self.follower and self.cache[self.follower].platId == self.id)
	
	def isJoiningPlatoon(self):
		return self.x[Y] == LEFT and self.platId != self.id and self.leader and self.cache[self.leader].x[Y] == RIGHT
	
	'''
	Checks for a nearby platoon that may be joined.
	A platoon is a viable candidate if its first
	TruckNode is in front of the back of self.
	Any platoon that is behind self will not be joined.
	'''
	def findPlatoon(self):
		platNode = None
		for id in self.cache:
			node = self.cache[id]
			if node.x[Y] == RIGHT and node.x[X] - (self.x[X] - TRUCK_LEN) > 0:
				if not platNode:
					platNode = node
				elif platNode.x[X] - node.x[X] > 0:
					platNode = node
		if not platNode and self.platId != self.id and self.leader and self.x[X] - TRUCK_LEN > self.cache[self.leader].x[X]:
			platNode = self.cache[self.leader]
		return platNode
	
	'''
	Checks if a range of the specified
	lane is blocked. xRange is (front, back)
	If blocked, return blocking node.
	'''
	def laneBlocked(self, lane, xRange):
		for id in self.cache:
			node = self.cache[id]
			if node.x[Y] == lane:
				if xRange[1] - BUF_DIST <= node.x[X] < xRange[0] + TRUCK_LEN + BUF_DIST:
					return node
		return None
	
	'''
	As a standalone TruckNode, join the platoon
	of platNode, and transfer into the appropriate
	lane. Reset self.follower.
	'''
	def joinPlatoon(self, platNode):
		if self.setLeader(platNode.id):
			self.x = (self.x[X], platNode.x[Y])
			self.follower = 0
	
	'''
	As a platoon leader, join the platoon
	directly in front of self.
	'''
	def mergeIntoPlatoon(self, immLead):
		if self.xDistance(immLead) < PLAT_DIST[1]:
			self.adjustmentMade = 16
			self.platId = immLead.platId
			self.accelerate((immLead.v[X] + immLead.a[X] - self.v[X], 0))
			if self.xDistance(immLead) < PLAT_DIST[0] or self.v[X] > immLead.v[X] + immLead.a[X]:
				self.adjustmentMade = 17
				self.accelerate(SLOW_DOWN)
		elif self.v[X] < immLead.v[X] + CATCH_UP:
			self.platId = immLead.platId
			self.adjustmentMade = 18
			self.accelerate(SPEED_UP)
	
	'''
	Returns True if self is a platoon leader.
	'''
	def isPlatoonLeader(self):
		return self.x[Y] == RIGHT and self.platId == self.id and (self.follower and self.cache[self.follower].platId == self.id or not self.follower) and not (self.leader and self.cache[self.leader].platId == self.platId)
	
	'''
	If self is in a platoon and is following
	another TruckNode, return the id of the
	TruckNode immediately ahead of self.
	'''
	def immPlatoonLeader(self):
		if self.leader and self.platId != self.id:
			return self.leader
		else:
			return 0
	
	'''
	If self is in a platoon and is followed by
	another TruckNode, return the id of the
	TruckNode immediately behind of self.
	'''
	def immPlatoonFollower(self):
		if self.follower and self.cache[self.follower].platId == self.platId:
			return self.follower
		else:
			return 0
	
	'''
	Calculates and returns the distance along
	the x-axis (along the road) between self
	and another TruckNode.
	'''
	def xDistance(self, node):
		if node:
			return node.x[X] - self.x[X]
		else:
			return 0
	
	'''
	Currently a setter for self.a,
	but may be better as a delta?
	'''
	def accelerate(self, a):
		if a[X] > MAX_ACCEL:
			self.a = (MAX_ACCEL, a[Y])
		elif a[X] < MAX_DECEL:
			self.a = (MAX_DECEL, a[Y])
		else:
			self.a = a
	
	'''
	Appends a line of state data to the TruckNode's
	log file.
	'''
	def writeState(self):
		self.logFile.write(str(self.seqNum) + ' ' + str(self.time % EPOCH_MOD) + ' ')
		self.logFile.write(str(self.platId) + ' ')
		self.logFile.write(str(self.adjustmentMade) + ' ')
		self.logFile.write(str(self.leader) + ' ')
		if self.leader:
			self.logFile.write(str(self.cache[self.leader].seqNum) + ' ')
		else:
			self.logFile.write('-1 ')
		self.logFile.write(str(self.follower) + ' ')
		if self.follower:
			self.logFile.write(str(self.cache[self.follower].seqNum) + ' ')
		else:
			self.logFile.write('-1 ')
		self.logFile.write(str(self.x[X]) + ' ' + str(self.x[Y]) + ' ')
		self.logFile.write(str(self.v[X]) + ' ' + str(self.v[Y]) + ' ')
		self.logFile.write(str(self.a[X]) + ' ' + str(self.a[Y]) + ' ')
		for id in list(self.neighbors):
			self.logFile.write(str(id) + ' ')
		self.logFile.write('MPR ' + str(self.primaryMPR) + ' ')
		if self.actAsMPR:
			self.logFile.write(' YES_I_AM ')
		else:
			self.logFile.write(' NO_I_AM_NOT ')
		self.logFile.write('\n')
		
	'''
	Logic to determine, from a received packet,
	whether the sending node is a one-hop neighbor 
	(PREV = SRC indicates a close MPR, SRCMPR = PREV indicates it only passes through one MPR to get there)
	or multi-hop neighbor
	(PREV != SRC and PREV != SRCMPR)
	...this decides into which cache we place the node!
	Return True if is a one-hop node, false if not
	'''
	def isOneHop(self, pkt):
		if pkt[PREV] == pkt[SRC] or pkt[PREV] == pkt[SRCMPR]:
			return True
		elif pkt[PREV] != pkt[SRC] and pkt[PREV] != pkt[SRCMPR]:
			return False
		else: #just assume it is a multi-hop neighbor for scenarios outside of the above
			return False
			
	'''
	Logic to determine whether to set self as an MPR from an external prompt!
	Upon receipt of the matching packet prompt, determines if self should remain
	an MPR or demote self to passive node, and does said demotion under certain situations.
	Since the packet is allowed to be a not-MPR-setting packet, also be sure
	to allow for the packet to be "normal".
	'''
	def amIMeantToBeAnMPR(self, pkt):
		if pkt[DST] == pkt[SRCMPR]:
			if self.id == pkt[DST] and self.id == pkt[SRCMPR]:
				#self.pushForwardNodeToBeMPR = True
				self.actAsMPR = True
				return YES_MPR
			elif self.id != pkt[SRCMPR]:
				if self.x[X] < pkt[Xx]: #then we are behind of the pulsing node [node sending MPR instruction], and we should not be an MPR
					self.actAsMPR = False
					return NO_MPR
				else:
					self.actAsMPR = self.actAsMPR
					return NO_MPR
			else:
				return NO_MPR
		else:
			return NORMALPKT
			
	'''
	Determine if self is the rearmost truck in range.
	(Used to decide if self should be the MPR that sets off the chain of instantiating all other MPRs)
	'''
	def amIRearmostNodeInRange(self):
		maxDeltaEncountered = 0
		for id in self.cache:
			newMPR = self.cache[id]
			if self.xDistance(newMPR) > maxDeltaEncountered:
				maxDeltaEncountered = self.xDistance(newMPR)
			if self.xDistance(newMPR) < 0: #if this triggers, then self is ahead of another vehicle
				#thus I am not the most rearward thing. In context of other uses, this also means I shouldn't force other nodes to be an MPR
				return False
		if maxDeltaEncountered == 0: #we still didn't find ourselves behind anything, necessarily, so no, we are not rearmost
			return False
		return True #if we reach this point, we were probably the rearmost thing in the whole wide world
		
		
	'''
	This allows	us to determine the next prime candidate 
	for being an MP router/relay.
	'''
	def seekPotentialMPR(self):
		potentialMPR = 0 #if you receive a 0 back at the end, you know you can't instruct anyone to be an MPR, and you just end the chain
		maxDistanceSoFar = 0 #accept nothing less than a distance of 1
		print 'Seeking potential MPR'
		for id in self.cache:
			newMPR = self.cache[id]
			#if self.xDistance(newMPR) <= maxDistanceSoFar: #then that means self is ahead of what might have been the newMPR, or the cache entry was invalid
			if self.xDistance(newMPR) > maxDistanceSoFar and self.xDistance(newMPR) < COMM_DIST: #then that means self is behind what could be the next newMPR
				maxDistanceSoFar = self.xDistance(newMPR)
				potentialMPR = newMPR.id	
				print 'found potential MPR'
		return potentialMPR #return the ID of the node you vote to be an MPR, and we'll broadcast a packet to everything in reach
	
	'''
	To push other nodes into becoming an MPR,
	the rearmost node will have to send out a packet. This
	is the method which figures out all those logistics
	to send that packet.
	'''
	def initiateNextForwardMPR(self, desiredMPR):
		for neighbor in list(self.neighbors): #"yes, we want to let all neighbors hear this packet"
			self.vc.sendData(neighbor, self.seqNum, self.id, desiredMPR, desiredMPR, BLANKET, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA)
		#self.vc.sendData(neighbor, self.seqNum, self.id, desiredMPR, desiredMPR, BLANKET, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.sendX, self.sendV, self.sendA) #if we're thinking "just directly tell the node to be an MPR and tell no one else."
					#but we should be able to prevent spurrious MPR changes
			
	
	
	'''
	This allows us to determine if a node
	being added to the cache is a viable local MPR 
	through which we can route our packets.
	'''
	def addThisAsNearbyMPR(self, node): #put preference on having a good primary MPR, then on having a good secondary MPR, to communicate with the outside world
		if not node:
			return False #if the node isn't viable, just don't even try to set anything
		if node.actAsMPR == False:
			return False #we don't need the node being represented as an MPR when it isn't
		if self.primaryMPR == 0: #then we set this new node as an MPR and return success
			self.primaryMPR = node.id
			return True #we can stop the fancy calculations here since we just set an MPR
		elif self.secondaryMPR == 0:
			self.secondaryMPR = node.id
			return True
		#then a fancy decision-making algorithm on who to replace with the better MPR
		pri_node_totest = self.cache[self.primaryMPR]
		sec_node_totest = self.cache[self.secondaryMPR]
		pri_node_distance = -111
		sec_node_distance = -111
		if pri_node_totest:
			pri_node_distance = self.xDistance(pri_node_totest)
		if sec_node_totest:
			sec_node_distance = self.xDistance(sec_node_totest)
		input_node_distance = self.xDistance(node)
		#continue decision making now that we have all the necessary values
		if fabs(input_node_distance) < fabs(pri_node_distance):
			self.primaryMPR = node.id
			return True
		elif fabs(input_node_distance) < fabs(sec_node_distance):
			self.secondaryMPR = node.id
			return True
		else: #give up and return false
			return False
