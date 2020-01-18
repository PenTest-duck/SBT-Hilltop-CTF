# Sneaky Transmission - Writeup

This challenge included a .pcapng file where data exfiltration was occuring via an unusual field in the IP header - the TTL (Time To Live) - where each byte of the flag was encoded into the TTL value.

Since there are only ping packets (this can be verified in Wireshark by clicking on Statistics > Protocol Hierarchy), it is obvious that the exfiltration protocol is ICMP. 
The solver's first instinct would be to check the fields in the ICMP header, from where they would find nothing out of the ordinary.

While analysing different values in the packet, the solver should notice the fluctuating TTL values in the IP headers of the ICMP ping request packets.
From there, the solver can assume that exfiltration is occuring through the TTL field.
Since the TTL values only range from 0 to 255 (which is also the range of decimal numbers representable through 1 byte), the solver can also assume that 1 byte of the flag is being sent in each ping request.

Once identifying the exfiltration vector, a short script, or scripts, utilising tcpdump can be written to collect and convert the TTL values to a file.
One possible way to solve the challenge is the following:

# Bash Script
```
#!/bin/bash

tcpdump -v icmp[icmptype] != icmp-echoreply -r sneaky_transmission.pcapng | grep -v "echo request" | while read -r line; do
	if [ $(echo $line | wc -w) != 17 ]; then
		./sneaky_solution.py 0
	else
		./sneaky_solution.py $(echo $line | awk '{print $6}' | cut -d "," -f 1)
	fi
done
```

# Python Script
```
#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from sys import argv
from struct import pack

with open("sneaky_flag", "a+b") as f:
    f.write(pack("1B", *[int(argv[1])]))
```

The script first reads the .pcapng file using tcpdump, picks out all ICMP echo request packets and discards lines that don't contain the TTL.
Since tcpdump doesn't display the TTL parameter if the TTL is set to 0, the if-else statement picks out lines that don't have the TTL (and thus are shorter) and manually places 0 as the argument for the Python script.
If the line does contain the TTL, the value of the TTL is extracted and used as the argument for the Python script.
The Python script converts the decimal TTL value to an ASCII/ANSI character and writes it to an output file.
*N.B. Using the bytes() function returns 2 bytes for integers over 127.*

Once the script has completed (it may take a few minutes), the output file should be the flag that was being exfiltrated.
Running the *file* command reveals the file to be in JPEG format. 
Simplfy add a .jpg or .jpeg prefix to the file to view the photo of the flag, which is a play on the phrase "sneak peek".

Flag: HilltopCTF{sn34k_p1c}
