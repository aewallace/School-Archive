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
		exit()
	
	print 'Simulation started! Running for ' + str(simTime) + ' seconds.'
	starter.sendline('python start.py')
	
	success = False
	count = 0
	maxTries = 5
	while (!success && count < maxTries):
		try:
			time.sleep(simTime)
			nodes[0].expect(".*finished")
			success = true
    	except Exception as e:
        	print "Simulation not finished. Waiting a little bit..."
        	count += 1
        	
    if (!success):
    	print "Simulation never reported itself as being finished."
    else:
    	print "Simulation finished."
	
	
	if 'y' == raw_input("View output? (y/n): "):
		id = startId
		print "interval", interval
		for node in nodes:
			print '******************************'
			print id
			print '******************************'
			id += interval
			print node.before
		print '******************************'
	
	if 'n' == raw_input('Awaiting re-initialization...'):
		for node in nodes:
		node.sendline('logout')
		exit()

	

