# URL Tsunami - Writeup

This Wireshark analysis challenge requires the solver to extract, concatenate and decode elements of a .pcapng file to retrieve an encoded .mp3 file which contains the flag.

From the moment you look at the .pcapng file in Wireshark, the exfiltration vector should be clear - HTTP requests for bizarre-looking URLs - and a little bit of CTF experience should tell you that the link is in base-64 and URL encoded.

Considering the characteristics of base-64, 3 symbols would have needed to be URL encoded - '+', '/' and '='.
The encoded version of those characters are %2B, %2F and %3D, respectively.

In order to recover the original .mp3 file, only the final portion of the URL should be extracted from the .pcapng file, the leading '/' and newline characters should be removed, the URL encoded symbols should be decoded and the base64 string should be decoded and saved to a .mp3 file (the file type can be verified by using the *file* command).

The following bash one-liner, with solve.py performs this process.

`./solve.py $(tcpdump -r tsunami_waves.pcapng | awk '{print $(NF-1)}' | tr -d "/" | tr -d "\n") | base64 -D > solved.mp3`

The .mp3 file has a TTS reading seemingly random words and numbers, however, they are NATO phonetic alphabets, and form each character of the flag.
Carefully listening to the .mp3 file and writing out each character should get you the flag.

Flag: HilltopCTF{s1l3n7_w4v35_9r0w_1nt0_t5un4m15}
