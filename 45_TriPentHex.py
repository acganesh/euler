from math import floor, ceil, sqrt

def is_triangle_number(num):
	floored_root = floor(sqrt(2*num))
	if num == (floored_root * (floored_root + 1)/2):
		return True
	else:
		return False

def is_hexagonal_number(num):
	ceiled_root = ceil(sqrt(num/2))
	if num == (ceiled_root * (2*ceiled_root-1)):
		return True
	else:
		return False

def triangular(n):
	return n*(n+1)/2

def pentagonal(n):
	return n*(3*n-1)/2

start = 165
n = start

while True:
	num = pentagonal(n)
	if is_triangle_number(num) and is_hexagonal_number(num):
		print n, pentagonal(n)

	n += 1