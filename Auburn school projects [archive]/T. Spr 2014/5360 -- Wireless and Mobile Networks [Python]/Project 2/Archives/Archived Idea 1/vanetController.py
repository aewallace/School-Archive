#Project 2 VC; used with Project 2 TN, not backwards compatible with Project 1 materials!

from random import random
import struct
import socket
from collections import deque

#constant for packet drop probability
DROP_K = 0.00002
#threshold for packet drop range limit
DROP_T = 0.2
#Port range for blanket broadcasts
#Ultimately should not have a step size of 2
PORT_RANGE = range(10100, 10120)
#packet structure
#16-bit Sequence number
#16-bit Source address
#16-bit Destination address
#16-bit address indicating the MPR of the source (for hop-count purposes)
#16-bit Previous hop (self id)
#16-bit platoon id
#16-bits each for ids of immediately leading/trailing vehicles
#32-bits each for X, Y, Vx, Vy, Ax, Ay
#40 bytes total
PKT_STRUCT = "!HHHHHHHHffffff"
#Packet index constants
SEQ, SRC, DST, SRCMPR, PREV, PLAT, LEAD, TRAIL, Xx, Xy, Vx, Vy, Ax, Ay = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
#TruckNode.packetDrops index constants
DROP, RECV = 0, 1
#Blanket broadcast identifier
BLANKET = 0
#For forwarding, if we manipulate the MPR field with our own or we let the original stay
KEEP_MPR_FIELD = 0
MANIP_MPR_FIELD = 1
#Indicate that the destination is a broadcast, since we need to identify a destination node now
BROADCAST_TO_ALL = -15
NO_KNOWN_MPR = 0
SENDING_TO_MPR = 0
#To determine if self is an MPR or not an MPR, or if normal packet not for setting MPR status
YES_MPR = 0
NO_MPR = 1
NORMALPKT = 2

class VanetController:

	def __init__(self):
		self.sockfd = None
		self.port = None
		self.tbfQueue = deque()
		self.seqTable = {}
		self.drops = 0
		self.recvs = 0
		self.oneHopNeighborCache = {} #updated by the TN who owns this VC; used only when an MPR
		self.multiHopNeighborCache = {} #same sitch as the oneHop cache above.

	'''
	Sets up socket for UDP packet transmission
	and reception.
	'''
	def setupSocket(self, port, timeout):
		try:
			self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.sockfd.bind(('', port))
			self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			self.sockfd.settimeout(timeout)
			if self.sockfd:
				self.port = port
				return True
			else:
				return False
		except:
			print "Socket initialization failed. Aborting..."
			exit(1)
	
	'''
	Awaits the start signal.
	'''
	def awaitStart(self):
		pkt = None
		print "Node ready. Awaiting signal..."
		#awaits a start packet (no required format)
		while not pkt:
			try:
				pkt, addr = self.sockfd.recvfrom(128)
				if pkt:
					return True
			except socket.timeout:
				pkt = None
			except:
				return False

	'''
	Given a TruckNode's position tuple, receive
	any sent packet and return it (if not dropped).
	Record receive/drop in dropMap for drop-rate
	calc in TruckNode.
	'''
	def receive(self, pos, dropMap, inputNodeID):
		pkt = None
		while not pkt:
			pkt, addr = self.sockfd.recvfrom(128)
			pkt = struct.unpack(PKT_STRUCT, pkt)
			#if packet is old, ignore it.
			if self.seqTable.has_key(pkt[SRC]) and pkt[SEQ] <= self.seqTable[pkt[SRC]]:
				pkt = None
				self.recvs += 1
			else:
				if not dropMap.has_key(pkt[PREV]):
						dropMap[pkt[PREV]] = [0, 0.001]
				#probabilistically drop packet unless it is from a blanket broadcast
				if pkt[PREV] != BLANKET and self.dropPacket(pos, (pkt[Xx], pkt[Xy])):
					dropMap[pkt[PREV]][DROP] += 1
					pkt = None
					self.drops += 1
		self.recvs += 1
		dropMap[pkt[PREV]][RECV] += 1
		self.seqTable[pkt[SRC]] = pkt[SEQ]
		#we now only append to the forwarding queue if the message was not meant for us,
		#	as we have no satisfactory way of getting the packet back to the original source
		#	(the MPR to which we'd send it would just send it back to us unless we swapped SRC and DST...
		#	...and that would result in us updating caches with erroneous data).
		if pkt[DST] != inputNodeID:
			self.tbfQueue.append(pkt)
		return pkt, pkt[PREV]
	
	'''
	Given TruckNode data, builds and
	broadcasts a data packet.
	'''
	def sendData(self, port, seq, src, dst, srcmpr, prev, plat, lead, trail, x, v, a):
		pkt = struct.pack(PKT_STRUCT, seq, src, dst, srcmpr, prev, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1])
		self.broadcast(pkt, port)
	
	'''
	Broadcasts TruckNode data on all ports.
	This method eliminates the need for 
	continuous checking and updating of the
	shared config file.
	'''
	def blanketBroadcast(self, seq, src, srcmpr, plat, lead, trail, x, v, a):
		for port in PORT_RANGE:
			pkt = struct.pack(PKT_STRUCT, seq, src, port, srcmpr, BLANKET, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1])
			self.broadcast(pkt, port)

	
	'''
	Forwards all packets in to-be-forwarded
	queue to the given port.
	'''
	def forwardPackets(self, port, id, keep_or_overwrite_MPR):
		if keep_or_overwrite_MPR == MANIP_MPR_FIELD:
			for pkt in list(self.tbfQueue):
				self.sendData(port, pkt[SEQ], pkt[SRC], pkt[DST], id, id, pkt[PLAT], pkt[LEAD], pkt[TRAIL], (pkt[Xx], pkt[Xy]), (pkt[Vx], pkt[Vy]), (pkt[Ax], pkt[Ay]))
		elif keep_or_overwrite_MPR == KEEP_MPR_FIELD:
			for pkt in list(self.tbfQueue):
				#some fancy logic probably has to go here regarding the whole forwarding thing
				self.sendData(port, pkt[SEQ], pkt[SRC], pkt[DST], pkt[SRCMPR], id, pkt[PLAT], pkt[LEAD], pkt[TRAIL], (pkt[Xx], pkt[Xy]), (pkt[Vx], pkt[Vy]), (pkt[Ax], pkt[Ay]))
	
	'''
	Clears the to-be-forwarded queue.
	'''
	def clearTBF(self):
		self.tbfQueue.clear()
	
	'''
	Given a packed packet, broadcast on selected port.
	'''
	def broadcast(self, pkt, port):
		self.sockfd.sendto(pkt, ("<broadcast>", port))
		

	'''
	Given a packet, dropPacket() will return true
	to drop the packet, or false to receive the packet.
	'''
	def dropPacket(self, xA, xB):
		return random() <= self.calcDropProbability(xA, xB)

	'''
	Given two position tuples, calcDropProbability() will
	return a drop probability proportional to the square
	of the distance between the two points.
	'''
	def calcDropProbability(self, xA, xB):
		return DROP_K * self.distanceSquared(xA, xB)

	'''
	Given two position tuples, distanceSquared() calculates the
	squared distance between the two points.
	'''
	def distanceSquared(self, pA, pB):
		return (pA[0] - pB[0])**2 + (pA[1] - pB[1])**2