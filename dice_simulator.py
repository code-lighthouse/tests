#! /usr/bin/python

import random

random.seed(100)

for roll in xrange(10):
    print random.randint(1, 6)

print 'Re-seeded'

random.seed(100)

for roll in xrange(10):
    print random.randint(1, 6)
