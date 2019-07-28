from math import sqrt, floor
import sys

def counting_rectangles(my_list):
	m = my_list[0]
	n = my_list[1]

	''' Iterative method
	result = 0

	m_range = range(1, m+1)
	n_range = range(1, n+1)

	for m in m_range:
		for n in n_range:
			result += m*n
	'''

	#Using triangular number formula:
	return n*(n+1)*m*(m+1)/4

def get_factor_pairs(n):
	threshold = int(floor(sqrt(n)))
	pairs = []

	for i in range(1, threshold+1):
		if n % i == 0:
			pairs.append([i, n/i])

	return pairs

def prod(my_list):
	prod = 1
	for item in my_list:
		prod *= item
	return prod

def get_closest_tuple(n):

	root = round(sqrt(4*n))
	root_range = range(int(root)-100, int(root)+100)

	min_dist = sys.maxint
	min_dim = None

	for root in root_range:
		pairs = get_factor_pairs(root)

		for item in pairs:
			item2 = []
			for element in item:
				item2.append(element-1)
			
			dist = abs(counting_rectangles(item) - n)

			dist2 = abs(counting_rectangles(item2) - n)

			if dist < min_dist:
				min_dist = dist
				min_dim = item

			if dist2 < min_dist:
				min_dist = dist2
				min_dim = item2

	return prod(min_dim)

print get_closest_tuple(2000000)
