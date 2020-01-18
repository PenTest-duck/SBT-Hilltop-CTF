#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from sys import argv
from struct import pack

with open("sneaky_flag", "a+b") as f:
    f.write(pack("1B", *[int(argv[1])]))
