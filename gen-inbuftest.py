#! /usr/bin/python

# Generate a series of (OFFSET,LENGTH) pairs for testing map_ptr, and
# also the output file that ought to be generated by them.  This
# version generates forward-moving, non-skipping ranges suitable for
# use on a socket or pipe.

# Copyright (C) 2000 by Martin Pool
# $Id$

import sys
from random import randint, expovariate

ntests = 4000

suck = open(sys.argv[3]).read()
filelen = len(suck)

cmdfile = open(sys.argv[1], 'wt')
datafile = open(sys.argv[2], 'wb')

off = 0

for i in range(ntests):
    remain = filelen - off
    if remain <= 0:
        break
    amount = min(remain, max(1, int(expovariate(1.0/2000))))

    cmdfile.write('%d,%d ' % (off,amount))
    datafile.write(suck[off:off+amount])

    off = off + randint(0, amount)
    