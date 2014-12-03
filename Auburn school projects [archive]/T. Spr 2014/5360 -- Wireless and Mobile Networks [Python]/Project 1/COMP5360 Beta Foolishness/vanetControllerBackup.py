from random import random
from math import sqrt
import struct
import socket

#constant for packet drop probability
DROP_K = 0.00002
#threshold for packet drop range limit
DROP_T = 0.2
#timeout for listening (in seconds)
TIMEOUT = 0.05
#port to be used for all TruckNodes (for now)
PORT = 10010
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

class VanetController:

	def __init__(self):
		self.sockfd = None
		self.port = None

	'''
	Sets up socket for UDP packet transmission
	and reception.
	'''
	def setupSocket(self):
		try:
			self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.sockfd.bind(('', PORT))
			self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
			self.sockfd.settimeout(TIMEOUT)
			if self.sockfd:
				self.port = PORT
				return True
			else:
				return False
		except:
			print "Socket initialization failed. Aborting..."
			exit(1)
	
	'''
	Given a TruckNode's data, broadcast() builds
	and broadcasts a data packet.
	'''
	def broadcast(self, seq, id, plat, lead, trail, x, v, a):
		pkt = struct.pack(PKT_STRUCT, seq, id, id, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1])
		self.sockfd.sendto(pkt, ("<broadcast>", self.port))
	
	'''
	Given an UNPACKED packet and the id of the
	forwarding TruckNode, forwards the packet.
	'''
	def forwardPacket(self, pkt, id):
		pkt = struct.pack(PKT_STRUCT, pkt[SEQ], pkt[SRC], id, pkt[PLAT], pkt[LEAD], pkt[TRAIL], pkt[Xx], pkt[Xy], pkt[Vx], pkt[Vy], pkt[Ax], pkt[Ay])
		self.sockfd.sendto(pkt, ("<broadcast>", self.port))

	'''
	Given a TruckNode's position tuple, receive
	any sent packet and return it (if not dfopped).
	'''
	#def receive(self, selfPos):
	def receive(self):
		try:
			pkt, addr = self.sockfd.recvfrom(128)
			pkt = struct.unpack(PKT_STRUCT, pkt)
			#if dropPacket(selfPos, (pkt[X], pkt[Y})):
			#	return None, pkt[PREV]
			#else:
			#	return pkt, pkt[PREV]
			return pkt, pkt[PREV]#don't drop packets for now
		except:
			return None, None

	'''
	Given a packet, dropPacket() will return true
	to drop the packet, or false to receive the packet.
	'''
	def dropPacket(xA, xB):
		return random() <= calcDropProbability(xA, xB)

	'''
	Given two position tuples, calcDropProbability() will
	return a drop probability proportional to the square
	of the distance between the two points.
	'''
	def calcDropProbability(xA, xB):
		return DROP_K * distance(xA, xB)**2

	'''
	Given two position tuples, distance() calculates the
	distance between the two points.
	'''
	def distance(pA, pB):
		return sqrt((pA[0] - pB[0])**2 + (pA[1] - pB[1])**2)