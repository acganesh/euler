import numpy as np
from numpy import polyfit

def generating_function(n):
	val = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
	return val

def cube_function(n):
	return n**3

def sum_FITs(fun, degree):
	my_sum = 0
	for i in range(2, degree+2):
		x_vals = range(1, i)
		y_vals = [fun(x) for x in x_vals]
		poly = np.poly1d(polyfit(x_vals, y_vals, i-2))
		FIT = poly(i)
		my_sum += FIT
	return my_sum

#print sum_FITs(cube_function, 3)
print sum_FITs(generating_function, 10)