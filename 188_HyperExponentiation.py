import sys
sys.setrecursionlimit(2000)

mod = 10**8

def hyp(a, b):
	if b == 1:
		return a
	else:
		return pow(a, hyp(a, b-1), mod)

def tests():
	print hyp(3, 2)
	print hyp(3, 3)

print hyp(1777, 1855)