from math import sqrt

def isPrime(n):
	bound = sqrt(n)
	divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True

i = 3
sum = 2
while (i < 2000000):
	if isPrime(i):
		sum += i
	i += 1
	if i % 1000 == 0: print i
print sum
