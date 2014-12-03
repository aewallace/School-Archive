'''
This script will kick off the simulations for any
initialized TruckNodes on the local network.

Run on cmd as follows:
>> python start.py

Note that the TruckNodes must use IDs in the
port range allotted to Group 1 (10100 - 10109).

Developers: Seth Denney, Albert Wallace
Date: March 2014
'''

from socket import *

for port in xrange(10100, 10110):
	sockfd = socket(AF_INET, SOCK_DGRAM)
	sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	sockfd.sendto('You been nuked son!', ("<broadcast>", port))
