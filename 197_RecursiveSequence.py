from math import floor
import sys
import matplotlib

def f(x):
	return floor(pow(2, 30.403243784) - pow(x, 2))*pow(10, -9)

def u(n):
	if n == 0:
		return -1
	else:
		return f(u(n-1))

for a in range(1, 1000):
	print a, u(a)

for exp in range(1, 10):
	try:
		print '%.15f' % u(10**exp)
	except RuntimeError:
		'failed'
