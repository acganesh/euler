from datetime import datetime
from math import sqrt

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def isPrime(n):
	'''
	if n in comp_cache:
		return False
	elif n in prime_cache:
		return True
	'''

	bound = sqrt(n)
	divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

timeneg1 = datetime.now()
print isPrime(99991)
print datetime.now() - timeneg1

time0 = datetime.now()
a = list(primes_sieve2(100000))
#print a[-1]
print datetime.now() - time0





time1 = datetime.now()
if 99991 in a:
	print "found"

print datetime.now() - time1


from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

time2 = datetime.now()

if binary_search(a, 99991):
	print "found2"

print datetime.now() - time2
