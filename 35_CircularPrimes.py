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

def get_perms(str):
	list = []
	length = len(str)

	ctr = 0
	while ctr <= length - 1:
		list.append(str[ctr:]+str[0:ctr])
		ctr += 1
	return list


def circular_prime(n):
	my_str = str(n)

	my_list = get_perms(my_str)
	my_int_list = [int(x) for x in my_list]


	for item in my_int_list:
		if isPrime(item) == False:
			return False

	return True

N = 2
num_circ_primes = 0
while N <= 1000000:
	if circular_prime(N):
		num_circ_primes += 1
	N += 1
	if N % 100000 == 0: print N

print num_circ_primes





