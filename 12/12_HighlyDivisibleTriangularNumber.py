from math import sqrt 

def num_divisors(n):
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
	return len(divisors)

def triangle_number(n):
	return n*(n+1)/2

n = 1
max_div = 0
while max_div < 500:
	cur_div = num_divisors(triangle_number(n))
	if cur_div > max_div:
		max_div = cur_div
	else:
		n += 1

print max_div,n, triangle_number(n)
