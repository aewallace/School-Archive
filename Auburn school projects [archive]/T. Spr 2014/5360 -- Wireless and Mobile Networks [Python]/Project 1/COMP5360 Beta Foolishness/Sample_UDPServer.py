#!usr/bin/python
#UDPServer.py
#run on cmd line as follows
#>>>python UDPServer.py (port num)

import socket
import struct
import sys
from collections import deque
from datetime import datetime

SRVR_IP = ''
SRVR_PORT = int(sys.argv[1])

def checksum(pkt):
   checksum = 0
   for c in pkt:
      checksum += ord(c)
      if (checksum & 0x100) == 0x100: checksum += 1#add carry
      checksum &= 0xff
   print "Packet sums to:", checksum
   checksum ^= 0xff#invert bits
   checksum &= 0xff#take only last 8 bits
   print "Checksum byte:", checksum
   return checksum
   
def lengthMismatch(pkt, length):
   return pkt[0] != length

def extractNames(str):
   return str.split('~')[1:]

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockfd.bind((SRVR_IP, SRVR_PORT))

while (True):
   try:
      pkt, addr = sockfd.recvfrom(1024)#buffer size = 1024 bytes
      if checksum(pkt) == 0:
         #packet not corrupted
         print "Good checksum received."
         length = len(pkt)
         ClientFormat = "!HBBB" + str(len(pkt) - 5) + 's'
         pkt = struct.unpack(ClientFormat, pkt)
         print "Packet contains", pkt
         if (lengthMismatch(pkt, length)):
            print "Length mismatch from client: responding..."
            #send length mismatch error packet
            pkt = struct.pack("!BBB2s", checksum("\x7f\x7f"), 127, 127, "\x00\x00")
            numBytes = sockfd.sendto(pkt, addr)
            if numBytes > 0:
               print "Length mismatch response sent."
            else:
               print "No data in response!!!"
         else:
            #resolve IP addresses and send valid response
            DNList = extractNames(pkt[4])
            ipBytes = deque()
            for name in DNList:
               try:
                  addrList = socket.gethostbyname_ex(name)[2]
                  if len(addrList) > 0:
                     ipBytes.append(chr(len(addrList)))
                     for ip in addrList:
                        ipBytes.extend((chr(int(b)) for b in ip.split('.')))
                  else:
                     ipBytes.append('\x01')
                     ipBytes.extend(['\xff', '\xff', '\xff', '\xff'])
               except socket.gaierror:
                  ipBytes.append('\x01')
                  ipBytes.extend(['\xff', '\xff', '\xff', '\xff'])
            if len(ipBytes) > 0:
               msg = ''.join(ipBytes)
               pkt = list(struct.pack("!HBBB" + str(len(msg)) + 's', len(msg) + 5, 0, pkt[2], pkt[3], msg))
               pkt[2] = chr(checksum(pkt))
               print "Sending checksum byte =", ord(pkt[2])
               pkt = ''.join(pkt)
               numBytes = sockfd.sendto(pkt, addr)
               if numBytes > 0:
                  print "Sent", numBytes, "bytes to", addr[0]
               else:
                  print "No data in response!!!"
      else:
         #send bad checksum error packet
         print "Bad checksum received."
         if len(pkt) > 3:
            pkt = list(struct.pack("!BBB2s", 0, ord(pkt[2]), ord(pkt[3]), "\x00\x00"))
         else:
            pkt = list(struct.pack("!BBB2s", 0, 1, 42, "\x00\x00"))
         pkt[1] = chr(checksum(pkt))
         pkt = ''.join(pkt)
         numBytes = sockfd.sendto(pkt, addr)
         if numBytes > 0:
            print "Checksum error response sent."
         else:
            print "No data in response!!!"
   except KeyboardInterrupt:
      exit(0)
   except Exception as e:
      print e