from math import sqrt

def isPrime(n):
	if n == 1:
		return False

	bound = sqrt(n)
	divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True

def get_square_corners(side_limit):
	side_length = 1
	start = 1
	ctr = 0
	my_list= []

	primes = 0
	total = 0
	ratio = 1

	while side_length <= side_limit:
		while ctr <= 4:
			num = start + side_length * 2 * ctr
			my_list.append(num)
			if isPrime(num):
				primes += 1
			total += 1
			ctr += 1
		start = my_list[-1]
		ctr = 1
		side_length += 1
		ratio = float(primes)/float(total)
		#print primes, total
		#print ratio
		if ratio <= 0.1 and not(side_length == 2):
			print side_length*2 - 1
			break
		if side_length % 100 == 0:
			print side_length, ratio
	return my_list

get_square_corners(1000000000)
