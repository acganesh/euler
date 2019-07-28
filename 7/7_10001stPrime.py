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

primes = []
i = 2
while (len(primes) < 10001):
	if isPrime(i):
		primes.append(i)
	i += 1
print primes[-1]
