#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')+1):
    if chr(alpha) not in ['q', 'e']:
        print("{0}".format(chr(alpha)), end='')
