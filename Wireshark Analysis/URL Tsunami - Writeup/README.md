# URL Tsunami - Writeup

This Wireshark analysis challenge requires the solver to extract, concatenate and decode elements of a .pcapng file to retrieve an encoded .mp3 file which contains the flag.

From the moment you look at the .pcapng file in Wireshark, the exfiltration vector should be clear - HTTP requests for bizarre-looking URLs - and a little bit of CTF experience should tell you that the link is in base-64 and URL encoded.

Considering the characteristics of base-64, 3 symbols would have needed to be URL encoded - '+', '/' and '='.
The encoded version of those characters are %2B, %2F and %3D, respectively.

`./solve.py $(tcpdump -r tsunami_waves.pcapng | awk '{print $(NF-1)}' | tr -d "/" | tr -d "\n") | base64 -D > solved.mp3`

Flag: HilltopCTF{s1l3n7_w4v35_9r0w_1nt0_t5un4m15}
