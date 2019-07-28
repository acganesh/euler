from operator import xor

for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            if reduce(xor, [a, b, c]) == 0:
                print a, b, c
