import sys
import datetime

start = datetime.datetime.now()

def is_permutation(a, b):
	if sorted(str(a)) == sorted(str(b)):
		return True
	else:
		return False

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def totient(n):
	factors = set(prime_factors(n))
	#print factors
	prod = 1
	for factor in factors:
		prod *= (1.0 - 1.0/(float(factor)))

	prod *= n

	return prod

print totient(5)
print totient(583200)
print totient(87109)
print is_permutation(int(totient(87109)), 87109)
print is_permutation(int(totient(989537)), 989537)
print round(totient(989537))
print totient(989537)
print totient(783169)
print int(round(totient(783169)))


n = 2
limit = 10**7
min_ratio = float('Inf')
min_n = 0

while n <= limit:
	if is_permutation(int(round(totient(n))), n):
		ratio = float(n)/totient(n)
		if ratio < min_ratio:
			min_ratio = ratio
			min_n = n
			print min_ratio, min_n
	if n % 1000000 == 0:
		print "count: ", n
	n += 1

print min_ratio, min_n
'''
n = 2
limit = 10000000

min_ratio = float('Inf')
min_n = 0

while n <= limit:
	totient_val = totient(n)

	if is_permutation(int(totient_val), n):
		ratio = float(n)/totient(n)
	 	if ratio < min_ratio:
			min_ratio = ratio
			min_n = n
			print min_ratio, n

	n += 1
	if n % 1000000 == 0: print n

print min_ratio, min_n

now = datetime.datetime.now()
print "Time elapsed: " + str(now - start) 
'''
