from math import floor

def max_weighted_product(m):
	my_list = []

	num = 1.0
	triangle_sum = m*(m+1)/2

	while num <= m:
		my_list.append(float(m)*float(num)/float(triangle_sum))
		num += 1

	ctr = 1
	prod = 1
	for item in my_list:
		prod *= (item ** ctr)
		ctr += 1

	return prod

num = 2
my_sum = 0
while num<= 15:
	my_sum += floor(max_weighted_product(num))
	num += 1

print my_sum


