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
	
	def run(self):
		#state output file
		self.logFile = open(str(self.id) + '.log', 'w')
		curTime = time()
		self.startTime = curTime
		self.lastUpdate = curTime
		self.lastWrite = curTime
		ctrlThread = Thread(target=self.controlThread)
		lstnThread = Thread(target=self.listenerThread)
		ctrlThread.start()
		lstnThread.start()
		for thrd in (ctrlThread, lstnThread):
			thrd.join()
	
	def controlThread(self):
		try:
			self.vc.setupSocket(self.id)
			lastBroadcast = time()
			while time() < self.startTime + TIME_LIM:
			#while True:
				while time() - lastBroadcast < BC_PER:
					pass
				#raw_input()
				lastBroadcast = time()
				#print "Neighbor loop"
				for neighbor in list(self.neighbors):
					#print "\t" + str(neighbor)
					if self.xDistance(self.cache[neighbor]) <= COMM_DIST:
						#print "\t\tBroadcasting..."
						self.vc.sendData(neighbor, self.seqNum, self.id, self.id, self.platId, self.immPlatoonLeader(), self.immPlatoonFollower(), self.x, self.v, self.a)
						#print "\t\tForwarding..."
						self.vc.forwardPackets(self.id, self.id)
				#print "Clear forwarding queue"
				self.vc.clearTBF()
				#print "Next timestep"
				self.nextTimestep()
			self.logFile.close()
			print "Simulation finished."
		except Exception as e:
			print "Exception in ControlThread:"
			print e
	
	def listenerThread(self):
		try:
			while time() < self.startTime + TIME_LIM:
				pkt, prev = self.vc.receive()
				if pkt:
					node = self.nodeFromPacket(pkt)
					self.updateCache(node)
				elif not pkt and prev:
					#packet was dropped, TODO
					pass
				self.cleanCache()
		except Exception as e:
			print "Exception in ListenerThread:"
			print e
	
	'''
	Builds a TruckNode object from an
	unpacked packet.
	'''
	def nodeFromPacket(self, pkt):
		node = TruckNode(pkt[SRC], (pkt[Xx], pkt[Xy]), (pkt[Vx], pkt[Vy]), (pkt[Ax], pkt[Ay]))
		node.seqNum = pkt[SEQ]
		node.platNum = pkt[PLAT]
		node.leader = pkt[LEAD]
		node.follower = pkt[TRAIL]
		return node
	
	'''
	Updates the cached copy of a given TruckNode.
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
	'''
	def cleanCache(self):
		for id in self.cache.keys():
			if self.xDistance(self.cache[id]) > COMM_DIST:
				#if self.follower == id:
				#	self.follower = 0
				#if self.leader == id:
				#	self.leader = 0
				#del self.cache[id]
				if id in list(self.neighbors):
					self.neighbors.remove(id)
	
	'''
	If node is immediately in front of self,
	update self.leader.
	'''
	def updateLeader(self, node):
		if self.leader and self.platId == self.id and self.x[Y] == LEFT:
			if self.cache[self.leader].x[Y] == RIGHT or self.cache[self.leader].x[X] < self.x[X]:
				self.leader = 0
		if self.platId == self.id and node and node.id != self.leader and node.x[Y] == self.x[Y] and node.x[X] > self.x[X]:
			if not self.leader:
				self.leader = node.id
			elif self.cache.has_key(self.leader) and self.cache[self.leader].x[X] > node.x[X]:
				self.leader = node.id
	
	'''
	If node is immediately behind self,
	update self.follower.
	'''
	def updateFollower(self, node):
		if self.follower and self.platId == self.id and self.x[Y] == LEFT:
			if self.cache[self.follower].x[Y] == RIGHT or self.cache[self.follower].x[X] > self.x[X]:
				self.follower = 0
		if node and node.id != self.follower and node.x[Y] == self.x[Y] and node.x[X] < self.x[X]:
			if not self.follower:
				self.follower = node.id
			if self.cache.has_key(self.follower) and self.cache[self.follower].x[X] < node.x[X]:
				self.follower = node.id
	
	'''
	Updates position, velocity, and acceleration
	based on context.
	'''
	def nextTimestep(self):
		curTime = time()
		step = curTime - self.lastUpdate
		#step = 1
		self.lastUpdate = curTime
		self.adjustSelf()
		self.x = (self.x[X] + self.v[X] * step, self.x[Y] + self.v[Y] * step)
		self.v = (self.v[X] + self.a[X] * step, self.v[Y] + self.a[Y] * step)
		self.seqNum += 1
		#if curTime - self.lastWrite > 1:
		#	self.writeState()
		#	self.lastWrite = curTime
		self.writeState()
	
	'''
	Make state-based decisions regarding
	how to adjust motion.
	'''
	def adjustSelf(self):
		immLead = self.immPlatoonLeader()
		if immLead:
			immLead = self.cache[immLead]
			self.stayInPlatoon(immLead)
		elif self.leader:
			immLead = self.cache[self.leader]
			self.avoidCollision(immLead)
		
		if self.isNotInPlatoon():
			if self.x[Y] == RIGHT:
				if self.laneClear(LEFT, (self.x[X], self.x[X] - TRUCK_LEN)):
					self.x[Y] = LEFT
			else:
				platNode = self.findPlatoon()
				if platNode:
					self.platId = platNode.platId
					if self.xDistance(platNode) < PLAT_DIST[0]:
						self.accelerate(SLOW_DOWN)
					elif self.laneClear(RIGHT, (self.x[X], self.x[X] - TRUCK_LEN)):
						self.joinPlatoon(platNode)
					else:
						#can't get over yet, squeeze in?
						pass
				else:
					#try to form a platoon with self.leader, if they're not in a platoon yet (their platId is their own)
					if immLead and self.xDistance(immLead) < COMM_DIST and immLead.platId == immLead.id:
						self.platId = immLead.platId
		elif self.isPlatoonLeader():
			if self.x[Y] == LEFT:
				#someone behind you wants to make a platoon with you, merge right if there's enough space
				if self.laneClear(RIGHT, (self.x[X], self.x[X] - 2 * TRUCK_LEN - PLAT_DIST[0])):
					self.x[Y] = RIGHT
			elif self.leader:
				immLead = self.cache[self.leader]
				self.mergeIntoPlatoon(immLead)
	
	'''
	If self is in a platoon and following another
	TruckNode, adjust to stay within the acceptable
	distance range.
	'''
	def stayInPlatoon(self, immLead):
		self.platId = immLead.platId
		self.avoidCollision(immLead)
		if self.x[Y] != immLead.x[Y] and self.laneClear(RIGHT, (self.x[X], self.x[X] - TRUCK_LEN)):
			self.x[Y] = RIGHT
	
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
		return self.platId == self.id and not (self.follower and self.cache[self.follower].platId != self.id)
	
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
	
	def laneClear(self, lane, xRange):
		for id in self.cache:
			node = self.cache[id]
			if node.x[lane] == RIGHT:
				if xRange[1] <= node.x[X] < xRange[0] + TRUCK_LEN:
					return False
		return True
	
	'''
	As a standalone TruckNode, join the platoon
	of platNode, and transfer into the right lane.
	Reset self.follower.
	'''
	def joinPlatoon(self, platNode):
		self.x[Y] = RIGHT
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
		return self.platId == self.id and self.follower and self.cache[self.follower].platId == self.id and not (self.leader and self.leader.platId == self.platId)
	
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
	Adjust acceleration by a specified amount.
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
		self.logFile.write(str(self.seqNum) + ' ')
		self.logFile.write(str(self.x[X]) + ' ' + str(self.x[Y]) + ' ')
		self.logFile.write(str(self.v[X]) + ' ' + str(self.v[Y]) + ' ')
		self.logFile.write(str(self.a[X]) + ' ' + str(self.a[Y]) + '\n')