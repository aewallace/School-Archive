#!usr/bin/python
#run on cmd line as follows
#python ClientUDP.py (server IP) (port num) (op code) (message w/ no spaces)

import socket
import struct
import sys
from datetime import datetime

SRVR_IP = sys.argv[1]
UDP_PORT = int(sys.argv[2])
OP = int(sys.argv[3])
MSG = sys.argv[4]
GID = 10011

ClientFormat = "!HHB" + str(len(MSG)) + 's'
VLenFormat = "!HHH"
DisVowFormat = "!HH"

pkt = struct.pack(ClientFormat, 5 + len(MSG), GID, OP, MSG)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
time = datetime.now()
sock.sendto(pkt, (SRVR_IP, UDP_PORT))

sock.settimeout(3)
try:
    pkt, addr = sock.recvfrom(128) # buffer size is 128 bytes
    time = datetime.now() - time
    sock.close()
    if OP == 85:
        pkt = struct.unpack(VLenFormat, pkt)
        print "Received: ", pkt[2]
        print "Response Time:", time.microseconds / 1000.0 + time.seconds * 1000, "ms"
    elif OP == 170:
        DisVowFormat += str(len(pkt) - 4) + 's'
        pkt = struct.unpack(DisVowFormat, pkt)
        print "Received: ", pkt[2]
        print "Response Time:", time.microseconds / 1000.0 + time.seconds * 1000, "ms"
except socket.timeout:
    print "No Response"