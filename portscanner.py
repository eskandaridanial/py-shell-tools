#!/bin/python3

# this script finds open ports on a network ip range

import sys
import socket
from datetime import datetime

# define the target
if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1]) # transalte hostname to ipv4
else:
		print("Invalid amount of args")
		print("Syntax : python3 scanner.py <ip>")
		sys.exit()


# banner
print("." * 50)
print("Scanning target : " + target)
print("Time started : " + str(datetime.now()))
print("." * 50)

try:
		for port in range(50 , 85):
				s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # INET == ipv4 , STREAM == port
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,port))
				print("Checking the port {}".format(port))
				if result == 0:
						print("Port {} is open".format(port))
				s.close()
		
except KeyboardInterrupt:
		print("Exiting the program.")
		sys.exit()

except socket.gaierror:
		print("Hostname could not resolve.")
		sys.exit()

except socket.error:
		print("Couldn't connect to server.")
		sys.exit()