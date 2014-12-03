from truckNode import TruckNode
import sys

tn = TruckNode(int(sys.argv[1]), (int(sys.argv[2]), 0), (int(sys.argv[3]), 0), (int(sys.argv[4]), 0))
nbr = int(raw_input('Known neighbor: '))
if nbr:
	tn.neighbors.append(nbr)
	tn.updateCache(TruckNode(nbr, (int(raw_input('X: ')), 0), (int(raw_input('V: ')), 0), (int(raw_input('A: ')), 0)))
tn.run()

#from truckNode import TruckNode; tn = TruckNode(10011, (0, 0), (1, 0), (0, 0)); tn.run()
#from truckNode import TruckNode; tn = TruckNode(10010, (0, 0), (2, 0), (0, 0)); tn.updateCache(TruckNode(10011, (50, 0), (1, 0), (0, 0))); tn.neighbors.append(10011); tn.run()