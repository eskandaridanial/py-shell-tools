#!/bin/bash

# Ping sweep is a technique that can be used to find out which hosts are alive in a network for a defined IP range. Network admins who allow ICMP are vulnerable to ICMP based attacks.
# visit https://www.javatpoint.com/icmp-protocol for ICMP details 

if [[ $1 == "" ]]; then
	echo "you forgot an ip address"
	echo "syntax : ./ipsweep.sh 192.168.1"

else
	for ip in {1..254}; do
		if out=`ping -c 1 $1.$ip`; then
			echo "$out" | grep "64 bytes" | cut -d " " -f 4 | tr -d ":"
		fi
	done
fi

# for ip in ${ips[@]}; do
# 	echo $ip
# done