from math import sqrt

def is_prime(n):
    limit = int(sqrt(n)) + 1
    for x in xrange(2, limit+1):
        if n % x == 0:
            return False
    return True

def main(n):
    pfs = []
    limit = int(sqrt(n)) + 1
    for x in xrange(limit+1, 1, -1):
        if n % x == 0:
            if is_prime(x):
                pfs.append(x)
            if n/x != x:
                if is_prime(n/x):
                    pfs.append(n/x)
    return max(pfs)


print main(600851475143)
