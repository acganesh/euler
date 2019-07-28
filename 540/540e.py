from fractions import gcd

def main(lim):
    c = 0
    #go up to limit
    for m in xrange(2, int(lim ** .5) + 1):
        #start from opposite parity
        for n in xrange(1 + m % 2, m, 2):
            #check for over limit
            if m * m + n * n > lim:
                break
            #check for relative primality
            if not gcd(m, n) == 1:
                continue
            c += 1
    return c

print main(3141592653589793)
