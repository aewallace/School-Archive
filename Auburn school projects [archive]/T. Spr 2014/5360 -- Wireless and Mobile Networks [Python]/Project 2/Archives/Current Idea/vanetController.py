'''
The VanetController class contains all of the
functionality to build, send, receive, and
unpack TruckNode data packets.

Developers: Seth Denney, Albert Wallace
Date: April 20 2014
'''
from math import fabs
from random import random
import struct
import socket
from collections import deque

#constant for packet drop probability
DROP_K = 0.00002
#threshold for packet drop range limit
DROP_T = 0.2
#Port range for blanket broadcasts
START_ID = 10100
NUM_NODES = 10
PORT_RANGE = range(START_ID, START_ID + NUM_NODES)
#packet structure
#16-bit Sequence number
#16-bit Source address
#16-bit Previous hop (self id)
#16-bit platoon id
#16-bits each for ids of immediately leading/trailing vehicles
#32-bits each for X, Y, Vx, Vy, Ax, Ay
#16-bits each to hold the list of nodes that have touched this packet, for a maximum of 10 previous nodes [yes, 10]
#36 + 20 = 56 bytes total
PKT_STRUCT = "!HHHHHHffffffHHHHHHHHHH"
#Packet index constants
SEQ, SRC, PREV, PLAT, LEAD, TRAIL, Xx, Xy, Vx, Vy, Ax, Ay, NBR0, NBR1, NBR2, NBR3, NBR4, NBR5, NBR6, NBR7, NBR8, NBR9 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
NULL_VAL = 0 #if a given field in the packet is supposed to be empty, it is this value
#return value expected when no better node than self is discovered for sending a packet
NO_NODE_ID = 56
#TruckNode.packetDrops index constants
DROP, RECV = 0, 1
#coord indices
POSX, POSY = 0, 1
#Blanket broadcast identifier
BLANKET = 0



class VanetController:

    def __init__(self):
        self.sockfd = None
        self.port = None
        self.tbfQueue = deque()
        self.seqTable = {}
        self.drops = 0
        self.recvs = 0
        self.heardFromSelf = 0
        self.sentFromSelf = 0
        self.knownGoodForwards = {}

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
            if pkt[SRC] == self.port:
            	self.heardFromSelf += 1
            #if pkt[PREV] == BLANKET:
            	#pkt = None
            	#self.recvs += 1
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
        self.tbfQueue.append(pkt)
        return (pkt, pkt[PREV])
    
    '''
    Given TruckNode data, builds and
    broadcasts a data packet.
    '''
    def sendData(self, port, seq, src, prev, plat, lead, trail, x, v, a, neighbors):
        pkt = self.makePacket(seq, src, prev, plat, lead, trail, x, v, a, neighbors)
        self.broadcast(pkt, port)
    
    '''
    Broadcasts TruckNode data on all ports.
    This method eliminates the need for 
    continuous checking and updating of the
    shared config file.
    '''
    def blanketBroadcast(self, seq, src, plat, lead, trail, x, v, a, neighbors):
        pkt = self.makePacket(seq, src, BLANKET, plat, lead, trail, x, v, a, neighbors)
        for port in PORT_RANGE:
            self.broadcast(pkt, port)
        #when we use the function we made, be sure to put BLANKET as the destination      
    
    '''
    Forwards all packets in to-be-forwarded
    queue to the given port, unless specific
    conditions are met which assure the packet
    will eventually reach the desired destination
    '''
    def forwardPackets(self, dstPort, id, selfXPos, neighbors, nodeCache):
        for pktToFwd in list(self.tbfQueue):
            if not self.hasVisited(pktToFwd, dstPort):
                pkt = self.updatePacket(pktToFwd, neighbors)
                self.broadcast(pkt, dstPort)
            elif dstPort in self.knownGoodForwards:
                pkt = self.updatePacket(pktToFwd, neighbors)
                self.broadcast(pkt, dstPort)
            elif dstPort in nodeCache:   
                dstNodePos = nodeCache[dstPort].x[POSX]
                mostContentiousNodeID, contentiousNodeDistance = self.getMinimumDistanceToNode(dstNodePos, dstPort, nodeCache)
                if mostContentiousNodeID != NO_NODE_ID and self.hasVisited(pktToFwd, mostContentiousNodeID) and self.doSendToNode(selfXPos, contentiousNodeDistance, dstNodePos): #if we determined that it'd be good to forward this packet...
                    pkt = self.updatePacket(pktToFwd, neighbors)
                    self.broadcast(pkt, dstPort)
                    self.knownGoodForwards[dstPort] = dstPort
            else:
            	return #if the dstPort isn't good for forwarding in the first iteration of the for loop, it won't be good until maybe the next call to forwardPackets
            #else we just don't forward the packet at all. like, at all.
            
    
    '''
    Clears the to-be-forwarded queue.
    '''
    def clearTBF(self):
        self.tbfQueue.clear()
        
    '''
    Clears the known list of good forwarding port IDs.
    Helps ensure a stable, truthful forwarding algorithm.
    '''
    def clearFIDCache(self):
    	self.knownGoodForwards = {}
    
    '''
    Given a packed packet, broadcast on selected port.
    '''
    def broadcast(self, pkt, port):
    	self.sentFromSelf += 1
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
        
    '''
    Checks the visited neighbors field of the packet
    to see if the input ID exists there. Returns TRUE if
    visited, returns FALSE otherwise.
    Accepts an unpacked packet and the node ID to be compared.
    '''
    def hasVisited(self, pkt, id):
        position = NBR0
        while position < NBR0 + NUM_NODES:
            if id == pkt[position]: #if we find the ID in the packet's list of neighbors, return true
                return True
            position += 1
        return False
      
                
    '''
    Creates a packed packet based on fresh input data, and adds our known neighbors that will have been reached.
    For sending with the sendData or blanketBroadcast functions.
    If you want to manipulate an already-made [and unpacked] packet, see "updatePacket".
    '''
    def makePacket(self, seq, src, prev, plat, lead, trail, x, v, a, neighbors):
        pkt = [NULL_VAL for xnum in xrange(NUM_NODES)]
        for neighbor in neighbors:
            pkt[neighbor % NUM_NODES] = neighbor
        pkt[src % NUM_NODES] = src
        return struct.pack(PKT_STRUCT, seq, src, prev, plat, lead, trail, x[0], x[1], v[0], v[1], a[0], a[1], pkt[0], pkt[1], pkt[2], pkt[3], pkt[4], pkt[5], pkt[6], pkt[7], pkt[8], pkt[9])
              
    '''
    Update the packet with our known neighbors & pack as desired.
    Input is an unpacked packet.
    Return is a packed packet with the neighbors updated & PREV updated.
    For the forwardPacket function
    '''
    def updatePacket(self, pkt, neighbors):
        pktNbrs = [NULL_VAL for xnum in xrange(NUM_NODES)]
        for neighbor in neighbors:
            pktNbrs[neighbor % NUM_NODES] = neighbor 
        pktNbrs[self.port % NUM_NODES] = self.port
        newPrevID = pkt[PREV]
        if (pkt[PREV] != BLANKET): #if packet is not a blanket control packet, update the PREV field of the packet with self's ID
            newPrevID = self.port
        return struct.pack(PKT_STRUCT, pkt[SEQ], pkt[SRC], newPrevID, pkt[PLAT], pkt[LEAD], pkt[TRAIL], pkt[Xx], pkt[Xy], pkt[Vx], pkt[Vy], pkt[Ax], pkt[Ay], pktNbrs[0], pktNbrs[1], pktNbrs[2], pktNbrs[3], pktNbrs[4], pktNbrs[5], pktNbrs[6], pktNbrs[7], pktNbrs[8], pktNbrs[9])
        
    
    '''
    Determine if, looking at the neighbors, we should probably send the packet.
    If we should send it, return TRUE; else, return FALSE
    ''' 
    def doSendToNode(self, selfXPos, competitionXPos, destinationXPos):
        if fabs(selfXPos - destinationXPos) < fabs(competitionXPos - destinationXPos):
            return True
        else:
            return False
    
    '''
    Gets the minimum distance from a node, identified with its ID and its position,
    to a nearby node. If the nodeID with the minimum distance returned is a competitor,
    specifically when trying to decide when to forward, it should exist in the neighbor list. 
    If it ends up that this node is not in the neighbor list, then forward.
    '''
    def getMinimumDistanceToNode(self, dstNodePos, dstNodePort, nodeCache):
        minimumNodeID = NO_NODE_ID
        minimumDistance = 100000
        for node in nodeCache:
            if dstNodePort in list(nodeCache[node].neighbors) and node != self.port:
                distance = fabs(nodeCache[node].x[POSX] - dstNodePos)
                if distance < minimumDistance:
                    distance = minimumDistance
                    minimumNodeID = nodeCache[node].id
        return (minimumNodeID, minimumDistance)
                
                
        
        
