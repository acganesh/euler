from math import floor, sqrt

from datetime import datetime

start_time = datetime.now()

def poly(num_coeff, x):
	my_list = list(str(num_coeff))
	my_list_int = [int(element) for element in my_list]

	index = len(my_list_int) - 1

	exp = 0
	my_sum = 0

	while index >= 0:
		my_sum += my_list_int[index] * (x ** exp)
		exp += 1
		index -= 1

	return my_sum

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

def check_for_int_root(num_coeff):
	my_list = list(str(num_coeff))
	my_list_int = [int(element) for element in my_list]

	divisors_q = get_divisors(my_list_int[0])
	divisors_p = get_divisors(my_list_int[-1])

	sign_vals = [1, -1]

	for p in divisors_p:
		for q in divisors_q:
			for sign in sign_vals:
				root = float(p)/float(q)
				if poly(num_coeff, float(sign)*root) == 0 and floor(root) == root:
					return True

	if poly(num_coeff, 0) == 0:
		return True
	return False

num_int_roots = 0
n = 1
while n <= 10 ** 6:
	if check_for_int_root(n):
		num_int_roots += 1
	n += 1
	#if n % 100 == 0: print n

print num_int_roots
print datetime.now() - start_time
