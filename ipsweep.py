# Ping sweep is a technique that can be used to find out which hosts are alive in a network for a defined IP range. Network admins who allow ICMP are vulnerable to ICMP based attacks.

import subprocess
import datetimeimport re
import argparse

def write_result(filename , ping):
	with open(filename , "w") as f:
		f.write(f"start time {datetime.datetime.now()}")
		for result in ping:
			f.write(result)
		f.write(f"end time {datetime.datetime.now()}")

def ping_subnet(subnet):
	for addr in range(1,255):
		yield subprocess.Popen(["ping" , f"{subnet}.{addr}" , "-n" "1"] , stdout=subprocess.PIPE) \
						.stdout.read()                                                            \
						.decode()

def main(subnet , filename):
	write_result(filename , ping_subnet(subnet))

def parse_argument():
	parser = argparse.ArgumentParser(usage='%(prog)s [options] <subnet>' ,
									 description = 'ip checker',
									 epilog = "python ipscanner.py 192.168.1 -f somefile.txt")

	parser.add_argument('subnet' , type=str , help='the subnet you want to ping')
	parser.add_argument("-f" , '--filename' , type=str , help='the filename')
	args = parser.parse_args()
	
	if not re.match(r"(\d{1,3}\.\d{1,3})\.\d{1,3}" , args.subnet) \
		or any(a not in range(1,255) for a in map(int , args.subnet.split("."))):
			parser.error("this is not a valid subnet")

 	if " " in args.filename:
 		parser.error("there can not be white spaces in the filename")

 	return args.subnet , args.filename

if __name__ == '__main__':
	main(*parse_argument())
	pass