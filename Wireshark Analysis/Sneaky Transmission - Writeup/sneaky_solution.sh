#!/bin/bash

tcpdump -v icmp[icmptype] != icmp-echoreply -r sneaky_transmission.pcapng | grep -v "echo request" | while read -r line; do
	if [ $(echo $line | wc -w) != 17 ]; then
		./sneaky_solution.py 0
	else
		./sneaky_solution.py $(echo $line | awk '{print $6}' | cut -d "," -f 1)
	fi
done
