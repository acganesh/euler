from Euler import prime_sieve, factor, is_prime
import fractions
import datetime

start = datetime.datetime.now()

def coprime(x,y):
	return fractions.gcd(x,y) == 1

def rad(x):
	factors = factor(x)
	prod = 1
	for item in factors:
		prod *= item[0]
	return prod

def rads(limit):
	r = []
	for x in range(limit):
		r.append(rad(x))
	return r


limit = 120000
R = rads(limit)
#print R

ctr = 0
my_sum = 0

for a in range(1, limit):
	for b in range(a+1, limit - a):
		if R[a]*R[b]*R[a+b] < a+b:
			if coprime(a,b):
				#print a,b,a+b
				my_sum += (a+b)
				ctr += 1

print "sum", my_sum
print "count", ctr
print datetime.datetime.now() - start

#print 'count', ctr

'''
for c in range(1, limit):
	for a in range(1, limit):
		if coprime(a,c):
			b = c-a
			if b > 0 and a < b:
				if R[a]*R[b]*R[c] < c:
					print a, b, c
					ctr += 1
'''
#print 'count', ctr


