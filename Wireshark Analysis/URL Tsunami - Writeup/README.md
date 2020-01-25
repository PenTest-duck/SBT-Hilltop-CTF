# URL Tsunami - Writeup

`./solve.py $(tcpdump -r tsunami_waves.pcapng | awk '{print $(NF-1)}' | tr -d "/" | tr -d "\n") | base64 -D > solved.mp3`
