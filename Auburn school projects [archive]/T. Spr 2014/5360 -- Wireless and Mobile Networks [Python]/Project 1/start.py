from socket import *

for port in xrange(10100, 10110):
	sockfd = socket(AF_INET, SOCK_DGRAM)
	sockfd.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	sockfd.sendto('You been nuked son!', ("<broadcast>", port))