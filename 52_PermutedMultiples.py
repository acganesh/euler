'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def check_if_same_digits(x, y):
	x_list = list(str(x)); x_list.sort()
	y_list = list(str(y)); y_list.sort()
	return x_list == y_list

def smallest_permuted_mult():
	x = 1
	while (True):
		if check_if_same_digits(x, 2*x) and check_if_same_digits(x, 3*x) and check_if_same_digits(x, 4*x) and check_if_same_digits(x, 5*x) and check_if_same_digits(x, 6*x):
			print x
			return x 
		else: 
			
			print "Failed:" + str(x)
			x += 1

print smallest_permuted_mult()



