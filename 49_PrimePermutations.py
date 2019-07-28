import itertools
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

def find_subsets(S, m):
	return set(itertools.combinations(S, m))

def int_perms(n):
	perms = itertools.permutations(str(n))
	return [int(''.join(x)) for x in perms]

#Only works for three element progressions
#Ignores elements that are all the same
def check_if_arith_prog(my_list):
	diff1 = my_list[1] - my_list[0]
	diff2 = my_list[2] - my_list[1]
	return diff1 == diff2 and not(diff1 == 0)

num = 1001
checked_vals = set()

while num <= 10000:
	if not num in checked_vals:
		if isPrime(num):
			perms = int_perms(num)
			checked_vals.update(perms)

			prime_perms = []

			for item in perms:
				if isPrime(item):
					prime_perms.append(item)
			prime_perms_ss = find_subsets(prime_perms, 3)
			for item2 in prime_perms_ss:
				if check_if_arith_prog(sorted(item2)):
					print item2
					break
	num += 2


