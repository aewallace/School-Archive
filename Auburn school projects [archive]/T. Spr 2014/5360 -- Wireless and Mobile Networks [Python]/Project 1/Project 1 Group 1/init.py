'''
This script will build the node and initialize it, ready to be kicked off by start.py.

Run on cmd line as follows:
>> python init.py (id) [startingV [configFile]]

By default, randomly generates starting velocity.
If a set starting velocity is desired, use the startingV parameter.

By default, reads from config.txt.
If a separate configuration file is desired, use the configFile parameter.

The format for each line in the configuration file is as follows:
(nodeID) (initX) (initY) links [linkID]*
For example, if node 10100 starts at (100, 0) and links to 10102 and 10104:
10100 100 0 links 10102 10104

Developers: Seth Denney, Albert Wallace
Date: March 2014
'''

from truckNode import *
import random
import sys

#velocity mean and stdev
MEAN_V = 30
STDEV_V = 10
MAX_V = 50
MIN_V = 10
#Config index constants
ID = 0
X = 1
Y = 2
LINKS = 4

class Node:
	def __init__(self, id, x, y, links):
		self.id = id
		self.x = x
		self.y = y
		self.links = links
	
	def getXY(self):
		return (self.x, self.y)

class TruckNodeBuilder:
	def __init__(self, id, v=None, path='config.txt'):
		self.id = id
		self.v = v
		self.configFile = open(path, 'r')
		self.nodeLines = [line.split() for line in self.configFile.readlines()]
		self.nodes = {}
		for line in self.nodeLines:
			if len(line) > LINKS:
				links = [int(link) for link in line[LINKS:]]
			else:
				links = []
			self.nodes[int(line[ID])] = Node(int(line[ID]), float(line[X]), float(line[Y]), links)
	
	def buildNode(self):
		tn = TruckNode(self.id, self.nodes[self.id].getXY(), (self.generateV(), 0), (0, 0))
		for link in self.nodes[self.id].links:
			node = self.nodes[link]
			tn.updateCache(TruckNode(node.id, node.getXY(), (0, 0), (0, 0)))
		if self.v is not None and self.v >= 0:
			tn.v = (self.v, 0)
		return tn
	
	def generateV(self):
		v = MEAN_V
		v = random.randint(v - STDEV_V, v + STDEV_V)
		if random.choice((True, False)):
			if random.choice((True, False)):
				v = random.randint(v, v + 2 * STDEV_V)
			else:
				v = random.randint(v - 2 * STDEV_V, v)
			if random.choice((True, False)):
				if random.choice((True, False)):
					v = random.randint(v, v + 2 * STDEV_V)
				else:
					v = random.randint(v - 2 * STDEV_V, v)
		return min(max(MIN_V, v), MAX_V)

#Main Code
builder = None
if len(sys.argv) == 4:
	builder = TruckNodeBuilder(id=int(sys.argv[1]), v=float(sys.argv[2]), path=sys.argv[3])
elif len(sys.argv) == 3:
	builder = TruckNodeBuilder(id=int(sys.argv[1]), v=float(sys.argv[2]))
elif len(sys.argv) == 2:
	builder = TruckNodeBuilder(id=int(sys.argv[1]))
if builder:
	tn = builder.buildNode()
	tn.initialize()