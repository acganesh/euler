from math import e
from fractions import Fraction
from datetime import datetime

start = datetime.now()

cache = [None]*100000
def prod(N, k):
	r = Fraction(N,k)
	P = r ** k
	return P

#Closest value to e - inspired from IMO problem
def prod_max(N):
	k = int(round(N/e))
	r = Fraction(N, k)
	P = r ** k
	return P, r.denominator

#Doesn't do unnecessary exponentiation
#much, much faster than prod_max()
def prod_max2(N):
	k = int(round(N/e))
	r = Fraction(N, k)
	return r.denominator

def factor_sieve(n):
	sieve = [[] for x in range(n+1)]
	for x in range(2, n+1):
		if sieve[x] == []:
			for y in range(x, n+1, x):
				sieve[y].append(x)
	return sieve

sieve = factor_sieve(100000)

#checks if 1/D is a terminating decimal
def is_terminating(D):
	val = cache[D]
	if val != None:
		return val
	else:
		while D > 1:
			if (D%2 == 0): D /= 2
			elif (D%5 == 0): D /= 5
			else:
				cache[D] = False
				return False
		cache[D] = True
		return True

#check if terminating with a precalculated sieve
def is_terminating2(D):
	val = cache[D]
	if val != None:
		return val
	else:
		while D > 1:
			factors = sieve[D]

			if factors ==[2,5] or factors == [2] or factors == [5]:
				cache[D] = True
				return True
			else:
				cache[D] = False
				return False

#Tests: Terminating 2 is slightly faster, but not by much
'''
t1s = datetime.now()
for a in range(2, 100000):
	is_terminating(a)
print datetime.now() - t1s

t2s = datetime.now()
for a in range(2, 100000):
	is_terminating2(a)
print datetime.now() - t2s
'''


#D function as defined in problem
def D(N):
	k = prod_max2(N)
	if is_terminating(k):
		#print P.denominator,k,'term'
		return -N
	else: 
		#print P.denominator,k, 'non_term'
		return N

def main(limit):
	total = 0
	for N in range(5, limit+1):
		total += D(N)
		if N % 100 == 0: print N
	return total


print main(10000)
print datetime.now() - start

#print prod_max(100)
