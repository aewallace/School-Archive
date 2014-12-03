#!usr/bin/python

'''
Must install Pexpect before running this script
>> pip install pexpect

Arguments follow this format:
>> python sshAuto.py numNodes startId interval simTime

Where:
	numNodes = number of nodes to use
	startId = id of first truckNode
	interval = interval between consecutive truckNode ids (1 for consecutive, 2 for evens/odds, etc.)
	simTime = expected runtime of simulation in seconds

When prompted to continue, enter the letter 'n' to quit, or hit enter to continue
'''

import sys
import pexpect
import time

def login():
	while True:
		try:
			child = pexpect.spawn('ssh aew0024@gate.eng.auburn.edu', timeout=5)
			child.expect('.*password:')
			child.sendline('au5ke7chypp1fa11')
			child.expect('.*:')
			child.sendline('')
			child.expect('.*password:')
			child.sendline('au5ke7chypp1fa11')
			child.sendline('cd COMP5360')
			print str(login.counter) + ' Logged in.'
			login.counter += 1
			return child
		except:
			print 'Trying ' + str(login.counter) + ' again...'

numNodes = int(sys.argv[1])
startId = int(sys.argv[2])
interval = int(sys.argv[3])
simTime = int(sys.argv[4])

login.counter = 1
nodes = [login() for x in xrange(numNodes)]
starter = login()

while (True):
	print 'Initializing nodes.'
	id = startId
	for node in nodes:
		node.sendline('python init.py ' + str(id))
		print 'Initialized ' + str(id)
		id += interval

	if 'n' == raw_input('All nodes initialized. Awaiting start confirmation...'):
		starter.sendline('python start.py')
		starter.sendline('python start.py')
		for node in nodes:
			node.sendline('logout')
		exit()
	
	print 'Simulation started! Running for ' + str(simTime) + ' seconds.'
	starter.sendline('python start.py')
	
	success = False
	count = 0
	maxTries = 5
	waitTime = simTime
	while (not success and count < maxTries):
		try:
			time.sleep(waitTime)
			nodes[0].expect(['Simulation finished.*', 'timed out'])
			success = True
			print "Simulation finished."
		except Exception as e:
			if 'n' == raw_input('Simulation may not be finished. Would you like to wait? (y/n): '):
				count = maxTries
			else:
				print "Waiting a little longer..."
				waitTime -= int(waitTime/2)
				count += 1
		
	
	if 'y' == raw_input("View output? (y/n): "):
		print "Please wait while we gather data..."
		if (not success): #we didn't have a successful run on the first one, so get a flush of everything that happened
			id = startId
			print "interval", interval
			for node in nodes:
				node.expect([pexpect.EOF, pexpect.TIMEOUT],1)
				
				print '******************************'
				print id
				print '******************************'
				id += interval
				print node.before
		else: #we had a successful run on the first one, so flush all the data a slightly different way
			id = startId
			print "interval", interval
			#first, finish up the first node
			print '******************************'
			print id
			print '******************************'
			id += interval
			print nodes[0].before
			print nodes[0].after
			nodes[0].expect([pexpect.EOF, pexpect.TIMEOUT],1)
			print nodes[0].before
			nodes[0].sendcontrol('k')
			#now do the rest of the nodes
			if len(nodes) > 1:
				for nn in range(1, len(nodes)):
					actualError = nodes[nn].expect([pexpect.EOF, pexpect.TIMEOUT],1)
					print '******************************'
					print id
					print '******************************'
					id += interval
					print nodes[nn].before
					if actualError == 1:
						print 'Hit timeout instead of end of buffer...'
		print '******************************'
	
	if 'n' == raw_input('Awaiting re-initialization...'):
		for node in nodes:
			node.sendline('logout')
		exit()

	

