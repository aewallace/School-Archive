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
PORT_RANGE = range(10100, 10120, 2)
#packet structure
#16-bit Sequence number
#16-bit Source address
#16-bit Previous hop (self id)
#16-bit platoon id
#16-bits each for ids of immediately leading/trailing vehicles
#32-bits each for X, Y, Vx, Vy, Ax, Ay
#36 bytes total
PKT_STRUCT = "!HHHHHHffffff"
#Packet index constants
SEQ, SRC, PREV, PLAT, LEAD, TRAIL, Xx, Xy, Vx, Vy, Ax, Ay = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
#TruckNode.packetDrops index constants
DROP, RECV = 0, 1
#Blanket broadcast identifier
BLANKET = 0

class VanetController:

	def __init__(self):
		self.sockfd = None
		self.port = None
		self.tbfQueue = deque()
		self.seqTable = {}

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
	def receive(self, pos, dropMap):
		pkt = None
		while not pkt:
			pkt, addr = self.sockfd.recvfrom(128)
			pkt = struct.unpack(PKT_STRUCT, pkt)
			#if packet is old, drop
			if self.seqTable.has_key(pkt[SRC]) and pkt[SEQ] <= self.seqTable[pkt[SRC]]:
				pkt = None
			else:
				if not dropMap.has_key(pkt[PREV]):
						dropMap[pkt[PREV]] = [0, 0.001]
				#probabilistically drop packet unless it is from a blanket broadcast
				if pkt[PREV] != BLANKET and self.dropPacket(pos, (pkt[Xx], pkt[Xy])):
					dropMap[pkt[PREV]][DROP] += 1
					pkt = None
		dropMap[pkt[PREV]][RECV] += 1
		self.seqTable[pkt[SRC]] = pkt[SEQ]
		self.tbfQueue.append(pkt)
		return pkt, pkt[PREV]
	
	'''
	Given TruckNode data, builds and
	broadcasts a data packet.
	'''
	def sendData(self, port, seq, src, prev, plat, lead, trail, x, v, a):
		pkt = struct.pack(PKT_STRUCT, seq, src, prev, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1])
		self.broadcast(pkt, port)
	
	'''
	Broadcasts TruckNode data on all ports.
	This method eliminates the need for 
	continuous checking and updating of the
	shared config file.
	'''
	def blanketBroadcast(self, seq, src, plat, lead, trail, x, v, a):
		pkt = struct.pack(PKT_STRUCT, seq, src, BLANKET, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1])
		for port in PORT_RANGE:
			self.broadcast(pkt, port)
	
	'''
	Forwards all packets in to-be-forwarded
	queue to the given port.
	'''
	def forwardPackets(self, port, id):
		for pkt in list(self.tbfQueue):
			self.sendData(port, pkt[SEQ], pkt[SRC], id, pkt[PLAT], pkt[LEAD], pkt[TRAIL], (pkt[Xx], pkt[Xy]), (pkt[Vx], pkt[Vy]), (pkt[Ax], pkt[Ay]))
	
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