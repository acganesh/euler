from math import sqrt

def isPrime(n):
	bound = sqrt(n)
	#divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True

def get_primes(n):
	prime_list = []
	num = 2
	while len(prime_list) <= n:
		if isPrime(num):
			prime_list.append(num)
		num += 1
	return prime_list

def get_squares(n):
	squares_list = []

	num = 1
	while num <= n:
		squares_list.append(num ** 2)
		num += 1
	return squares_list

def get_goldbach_nums(prime_list, squares_list):
	goldbach_nums = []
	for prime in prime_list:
		for square in squares_list:
			goldbach_num = prime + 2*square
			if isPrime(goldbach_num) == False and goldbach_num % 2 == 1 and not goldbach_num in goldbach_nums:
				goldbach_nums.append(goldbach_num)
				#print goldbach_num
	return goldbach_nums

prime_list = get_primes(1000)
#print prime_list
squares_list = get_squares(100)

goldbach_list = sorted(get_goldbach_nums(prime_list, squares_list))

#print goldbach_list[-1]
#print prime_list[-1]
#print squares_list[-1]

n = 3
while n <= 10000:
	if n % 2 == 1 and isPrime(n) == False:
		if not n in goldbach_list:
			print n
			break
	n += 1

