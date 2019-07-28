from math import sqrt

def is_pandigital(n):
	my_str = sorted(str(n))
	my_str = ''.join(my_str)

	length = len(my_str)

	ctr = 1
	pandigital_str = ''
	while ctr <= length:
		pandigital_str += str(ctr)
		ctr += 1

	if my_str == pandigital_str:
		return True
	else:
		return False

def isPrime(n):
        bound = sqrt(n)
        divisors = []

        i = 2
        while i <= bound:
                if (n % i) == 0:
                        return False
                i += 1
        return True

#don't need to check 8 or 9 digit pandigitals 
#because by Gauss's sums those are multiples of 3, and therefore composite

start = 7654321

n = start

while n > 0:
	if is_pandigital(n):
		if isPrime(n):
			print n
			break
	n -= 2

