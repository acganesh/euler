from Euler import prime_sieve
from itertools import product
from itertools import chain
from math import log, ceil

def factor_sieve(n, limit):
	#sieve = [1 for k in range(n+1)]
	sieve = [False]*(n+1)
	for x in range(2, n+1):
		if sieve[x] == False:
			for y in range(x, n+1, x):
				if x <= limit:
					sieve[y]=(True)
				else:
					sieve[y]=(False)
	return sieve


'''
my_list = factor_sieve(10**8, 5)
length = len(my_list)
print length
ctr = 0
total = 0
while ctr < length:
	if my_list[ctr]: 
		total += 1
	ctr += 1
print total
'''
def mult(primes, limit):
	length = len(primes)
	ctr = 0
	val = 1
	while ctr < length:
		val *= (primes[ctr] ** exps[ctr])
		if val > limit:
			return 0
		ctr += 1
	return val

def tests():
	print main(5, 10**7)

def prod(vals, limit):
	val = 1
	for factor in vals:
		val *= factor
		if val > limit:
			return 0
	return val



def main(N, limit):
	def fn(reps):
		return product(primes, repeat = reps)

	primes = prime_sieve(N+1)
	rep_limit = int(ceil(log(limit, 2)))
	#print list(product(primes, repeat=reps))
	#print map(lambda reps: list(product(primes, repeat = reps)), range(1, rep_limit))
	filtered = set([])
	my_list = chain.from_iterable(map(fn, range(1, rep_limit)))
	#prods = [x for x in my_list if x < limit]
	ctr = 0
	for item in my_list:
		prod_val = prod(item, limit)
		if prod_val > 0 and prod_val not in filtered:
			filtered.add(prod_val)
			ctr += 1

	#prods = [x for x in chain.from_iterable(map(lambda reps: product(primes, repeat = reps), range(1, rep_limit))) if prod(x, limit) > 0]
	#print prods
	print ctr+1

tests()



'''
primes = prime_sieve(5)
prod = product(primes, repeat=3)
print list(prod)
'''

