from math import sqrt


from datetime import datetime
startTime = datetime.now()


global prime_cache
prime_cache = []

global comp_cache
comp_cache = []

def get_divisors(n):
	bound = sqrt(n)
	divisors = []

	i = 1
	while i <= bound:
		if (n % i) == 0:
			divisors.append(i)
			divisor_pair = n/i
			if not (i == n/i):
				divisors.append(n/i)
		i += 1
	return divisors

''' naive isPrime
def isPrime(n):
	if get_divisors(n) == [1, n]:
		return True
	else:
		return False
'''

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
			comp_cache.append(n)
			return False
		i += 1
	prime_cache.append(n)
	return True

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def check_problem_condition(n, my_list):
	divisors = get_divisors(n)
	divisors.sort()
	bound = sqrt(n)
	for divisor in divisors:
		if binary_search(my_list, divisor + n/divisor) == False:
			return False
		if divisor > bound:
			return True
	return True

def iterate_problem_condition_up_to(bound):
	primeList = list(primes_sieve2(bound))
	sum = 0
	num = 0
	while num <= bound:
		if check_problem_condition(num, primeList):
			#print num
			sum += num
		if num >= 10:
			if (num % 10) == 0: 
				num += 2
			elif (num % 10) == 2:
				num += 6
			elif (num % 10) == 8:
				num += 2
		else:
			num += 1

		if (num % 1000000) == 0: print num
	return sum

#print get_divisors(4)

print iterate_problem_condition_up_to(10)

endTime = datetime.now()
print datetime.now() - startTime