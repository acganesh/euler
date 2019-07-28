from math import sqrt, ceil
from datetime import datetime

s = datetime.now()

#returns a**2 + (a+1)**2 + ... + b**2
def is_palindromic(n):
	n = str(n)
	return n == n[::-1]

def consec_sq(a, b):
	return (b*(b+1)*(2*b+1) - (a-1)*(a)*(2*a-1))/6

def tests():
	print consec_sq(6, 12)
	total = main(1000)
	print 'total', total

def main(limit):
	pal_set = set([])
	a = 1
	b = 1
	ctr = 0
	total = 0
	var_limit = int(ceil(sqrt(limit)))
	for a in range(1, var_limit+1):
		for b in range(a+1, var_limit+1):
			val = consec_sq(a,b)
			if val > limit:
				break
			elif is_palindromic(val) and val not in pal_set:
				pal_set.add(val)
				ctr += 1
				total += val
	return total

print main(10**8)

print datetime.now() - s