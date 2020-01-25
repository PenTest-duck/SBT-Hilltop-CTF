#!/usr/bin/python

from sys import argv

print(argv[1].replace("%2B", "+").replace("%2F", "/").replace("%3D", "="))
