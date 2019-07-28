from math import sqrt

def isPrime(n):
	if n == 1: return False
	bound = sqrt(n)
	divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True


def is_truncatable(n):
	my_str = str(n)
	n = 1
	while n <= len(my_str):
		if not(isPrime(int(my_str[:n]))):
			
			return False
		if not(isPrime(int(my_str[-n:]))):
			return False
		n += 1
	return True

num = 11
truncatable = []
while len(truncatable) < 11:
	if is_truncatable(num):
		truncatable.append(num)
	num += 1
print sum(truncatable)


