from math import fabs
from vanetController import *
from time import time
from threading import Thread
from collections import deque
import sys

#time between broadcasts (10 ms)
BC_PER = 0.01
#time limit (5*60 sec)
#TIME_LIM = 5 * 60
TIME_LIM = 30
#Comm range
COMM_DIST = 100
#coord indices
X, Y = 0, 1
#Y-position (lane) constants
LEFT, RIGHT = 0, 1
#length of truck
TRUCK_LEN = 25
#allowable platoon distance range
PLAT_DIST = (TRUCK_LEN + 10, TRUCK_LEN + 20)
#acceleration magnitudes
SLOW_DOWN = (-5, 0)
SPEED_UP = (5, 0)
CATCH_SPEED = 5
#TruckNode.packetDrops index constants
DROP, RECV = 0, 1
#Period over which to calculate drop rates
DROP_PER = 1

'''
X refers to the axis along the road.
Y refers to the axis across the road (lane position).
'''
class TruckNode:
	
	def __init__(self, id, x, v, a):
		#network controller
		self.vc = VanetController()
		#position (px, py)
		self.x = x
		#velocity (vx, vy)
		self.v = v
		#acceleration (ax, ay)
		self.a = a
		#unique 16-bit ID (address)
		self.id = id
		#platoon id
		self.platId = id
		#TruckNode identifiers
		self.leader = 0
		self.follower = 0
		#neighbor cache {id: TruckNode}
		self.cache = {}
		self.neighbors = deque()
		#sequence number
		self.seqNum = 0
		self.time = 0
		#dict maps neighbor ids to [numDrops, numReceives]
		self.packetDrops = {}
		self.bcastCount = 0
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
			print 'Starting Simulation! Running for', TIME_LIM, 'seconds'
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
		#try:
		lastBroadcast = time()
		self.bcastCount = 0
		while time() < self.startTime + TIME_LIM:
			while time() - lastBroadcast < BC_PER:
				pass
			self.sendData()
			self.nextTimestep()
			self.checkDropRates()
		self.logFile.close()
		print "Simulation finished."
		#except Exception as e:
		#	print "Exception in ControlThread:"
		#	print e
	
	'''
	This is the main method for lstnThread.
	It controls the reception of packets
	from other TruckNodes, and updates
	the caches with the latest received
	information.
	'''
	def listenerThread(self):
		#try:
		while time() < self.startTime + TIME_LIM:
			pkt, prev = self.vc.receive(self.x, self.packetDrops)
			if pkt:
				node = self.nodeFromPacket(pkt)
				self.updateCache(node)
				#self.cleanCache()
		#except Exception as e:
                       # print "Exception in ListenerThread:"
			#print e
	
	'''
	Sends self data and packets to be forwarded
	to all neighbor nodes.
	'''
	def sendData(self):
		lastBroadcast = time()
		for neighbor in list(self.neighbors):
			if self.xDistance(self.cache[neighbor]) <= COMM_DIST:
				self.vc.sendData(neighbor, self.seqNum, self.id, self.id, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.x, self.v, self.a)
				self.vc.forwardPackets(self.id, self.id)
		self.vc.clearTBF()
		self.bcastCount += 1
	
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
		return node
	
	'''
	Updates the cached copy of a given TruckNode.
	Also determines if any properties change
	as a result of this update.
	'''
	def updateCache(self, node):
		if self.xDistance(node) < COMM_DIST and node.id not in list(self.neighbors):
			self.neighbors.append(node.id)
		if self.cache.has_key(node.id):
			self.cache[node.id] = node
		else:
			self.cache[node.id] = node
		self.updateLeader(node)
		self.updateFollower(node)
	
	'''
	Removes all cached TruckNode objects
	that are now out of range.
	NOT NEEDED???????????
	'''
	def cleanCache(self):
		nbrs = list(self.neighbors)
		for id in self.cache.keys():
			if self.xDistance(self.cache[id]) > COMM_DIST:
				#if self.follower == id:
				#	self.follower = 0
				#if self.leader == id:
				#	self.leader = 0
				#del self.cache[id]
				if id in nbrs:
					self.neighbors.remove(id)
	
	'''
	Calculates average drop rates for each neighbor
	over a given period, DROP_PER. If above a certain
	threshold, DROP_T, the neighbor is removed.
	'''
	def checkDropRates(self):
		if self.bcastCount == int(DROP_PER / BC_PER):
			for id in self.packetDrops:
				if id in self.neighbors and float(self.packetDrops[id][DROP]) / self.packetDrops[id][RECV] >= DROP_T:
					self.neighbors.remove(id)
					print "Removed", id, "from neighbor list"
				self.packetDrops[id][DROP] = 0
				self.packetDrops[id][RECV] = 0
			self.bcastCount = 0
	
	'''
	If node is immediately in front of self,
	update self.leader. If current leader is
	no longer valid, reset.
	'''
	def updateLeader(self, node):
		if self.leader and self.platId == self.id and self.cache[self.leader].x[Y] != self.x[Y]:
			self.leader = 0
		if self.platId == self.id and node and node.id != self.leader and node.x[Y] == self.x[Y] and node.x[X] > self.x[X]:
			if not self.leader:
				self.leader = node.id
			elif self.cache.has_key(self.leader) and self.cache[self.leader].x[X] > node.x[X]:
				self.leader = node.id
	
	'''
	If node is immediately behind self,
	update self.follower. If current
	follower is no longer valid, reset.
	'''
	def updateFollower(self, node):
		if self.follower and self.cache[self.follower].platID != self.platId and self.cache[self.follower].x[Y] != self.x[Y]:
			self.follower = 0
		if node and node.id != self.follower and node.x[Y] == self.x[Y] and node.x[X] < self.x[X]:
			if not self.follower:
				self.follower = node.id
			if self.cache.has_key(self.follower) and self.cache[self.follower].x[X] < node.x[X]:
				self.follower = node.id
	
	'''
	Updates position, velocity, and acceleration
	based on context. Writes to logFile.
	'''
	def nextTimestep(self):
		curTime = time()
		step = curTime - self.lastUpdate
		self.lastUpdate = curTime
		self.adjustSelf()
		self.x = (self.x[X] + self.v[X] * step, self.x[Y] + self.v[Y] * step)
		self.v = (self.v[X] + self.a[X] * step, self.v[Y] + self.a[Y] * step)
		self.seqNum += 1
		self.time = time()
		self.writeState()
	
	'''
	Make state-based decisions to
	affect motion and platooning.
	'''
	def adjustSelf(self):
		immLead = self.immPlatoonLeader()
		if immLead:
			immLead = self.cache[immLead]
			self.stayInPlatoon(immLead)
			self.adjustmentMade = 0
		elif self.leader:
			immLead = self.cache[self.leader]
			self.avoidCollision(immLead)
			self.adjustmentMade = 1
		
		if self.isNotInPlatoon():
			self.adjustmentMade = 2
			platNode = self.findPlatoon()
			if platNode:
				self.adjustmentMade = 3
				self.platId = platNode.platId
				if self.xDistance(platNode) < PLAT_DIST[0]:
					self.accelerate(SLOW_DOWN)
					self.adjustmentMade = 4
				elif self.laneClear(platNode.x[Y], (self.x[X], self.x[X] - TRUCK_LEN)):
					self.joinPlatoon(platNode)
					self.adjustmentMade = 5
				else:
					#can't get over yet, squeeze in?
					self.adjustmentMade = 6
			else:
				self.adjustmentMade = 7
				#try to form a platoon with self.leader, if they're not in a platoon yet (their platId is their own)
				if immLead and self.xDistance(immLead) < COMM_DIST and immLead.platId == immLead.id:
					self.platId = immLead.platId
					self.adjustmentMade = 8
				else:
					#no one is in front of you, get into right lane and let any platoons catch up to you
					if self.laneClear(RIGHT, (self.x[X], self.x[X] - TRUCK_LEN)):
						self.x = (self.x[X], RIGHT)
		elif self.isPlatoonLeader():
			self.adjustmentMade = 9
			if self.x[Y] == LEFT:
				self.adjustmentMade = 10
				#someone behind you wants to make a platoon with you, merge right if there's enough space
				if self.laneClear(RIGHT, (self.x[X], self.x[X] - 2 * TRUCK_LEN - PLAT_DIST[0])):
					self.x = (self.x[X], RIGHT)
					self.adjustmentMade = 11
			elif self.leader:
				immLead = self.cache[self.leader]
				self.mergeIntoPlatoon(immLead)
				self.adjustmentMade = 12
	
	'''
	If self is in a platoon and following another
	TruckNode, adjust to stay within the acceptable
	distance range.
	'''
	def stayInPlatoon(self, immLead):
		self.platId = immLead.platId
		self.avoidCollision(immLead)
		if self.x[Y] != immLead.x[Y] and self.laneClear(immLead.x[Y], (self.x[X], self.x[X] - TRUCK_LEN)):
			self.x = (self.x[X], immLead.x[Y])
	
	'''
	If self is not in a platoon, avoid overrunning
	any car in front of self, and do not continue
	slowing down unnecessarily.
	'''
	def avoidCollision(self, immLead):
		d = self.xDistance(immLead)
		if d < PLAT_DIST[0]:
			self.accelerate((immLead.v[X] - self.v[X] - 1, self.a[Y]))
		elif d > PLAT_DIST[1]:
			self.accelerate((immLead.v[X] - self.v[X] + 1, self.a[Y]))
		else:
			self.accelerate((immLead.v[X] - self.v[X], self.a[Y]))
	
	'''
	Returns True if self is not in a platoon
	and False otherwise.
	'''
	def isNotInPlatoon(self):
		return self.x[Y] == LEFT and self.platId == self.id and not (self.follower and self.cache[self.follower].platId == self.id)
	
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
			if node.x[Y] == RIGHT:
				if node.x[X] - self.x[X] - TRUCK_LEN > 0:
					if not platNode:
						platNode = node
					elif platNode.x[X] - node.x[X] > 0:
						platNode = node
		return platNode
	
	'''
	Checks if a range of the specified
	lane is clear. xRange is (front, back)
	'''
	def laneClear(self, lane, xRange):
		for id in self.cache:
			node = self.cache[id]
			if node.x[Y] == lane:
				if xRange[1] <= node.x[X] < xRange[0] + TRUCK_LEN:
					return False
		return True
	
	'''
	As a standalone TruckNode, join the platoon
	of platNode, and transfer into the appropriate
	lane. Reset self.follower.
	'''
	def joinPlatoon(self, platNode):
		self.x = (self.x[X], platNode.x[Y])
		self.leader = platNode.id
		self.follower = 0
	
	'''
	As a platoon leader, join the platoon
	directly in front of self.
	'''
	def mergeIntoPlatoon(self, immLead):
		if self.xDistance(immLead) < PLAT_DIST[1]:
			self.platId = immLead.platId
		elif self.v[X] < immLead.v[X] + CATCH_SPEED:
			self.accelerate(SPEED_UP)
	
	'''
	Returns True if self is a platoon leader.
	'''
	def isPlatoonLeader(self):
		return self.x[Y] == RIGHT and self.platId == self.id and (self.follower and self.cache[self.follower].platId == self.id or not self.follower) and not (self.leader and self.leader.platId == self.platId)
	
	'''
	If self is in a platoon and is following
	another TruckNode, return the id of the
	TruckNode immediately ahead of self.
	'''
	def immPlatoonLeader(self):
		if self.leader and self.cache[self.leader].platId == self.platId:
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
			return fabs(node.x[X] - self.x[X])
		else:
			return 0
	
	'''
	Currently a setter for self.a,
	but may be better as a delta?
	'''
	def accelerate(self, a):
		#x, y = 0, 0
		#if (self.a[X] + a[X] >= 0):
		#	x = self.a[X] + a[X]
		#if self.a[Y] + a[Y] >= 0:
		#	y = self.a[Y] + a[Y]
		#self.a = (x, y)
		self.a = a
	
	'''
	Appends a line of state data to the TruckNode's
	log file.
	'''
	def writeState(self):
		self.logFile.write(str(self.seqNum) + ' ' + str(self.time) + ' ')
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
		self.logFile.write(str(self.a[X]) + ' ' + str(self.a[Y]) + '\n')
