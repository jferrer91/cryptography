#!/usr/bin/python

import sys
from fractions import gcd

b = int(sys.argv[1])
n = int(sys.argv[2])

test = False

if gcd(b,n) == 1:
	test = (pow(b,n-1,n) == 1)
	
print "Test: ", test
