from math import sqrt, floor
from datetime import datetime

s = datetime.now()

squares = set([x**2 for x in range(1000)])

def is_int(x):
	if floor(x) == x:
		return True
	else:
		return False

def is_triangle(a,b,c):
	if a+b > c and b+c > a and c+a>b:
		return True
	else:
		return False

def median(a,b,c):
	return sqrt(2*a**2+2*b**2-c**2)/2

def median2(a,b,c):
	return 2*a**2+2*b**2-c**2

def is_int2(x):
	if x % 2 == 0 and x in squares:
		return True
	else:
		return False

def main(n):
	count = 0
	for c in range(2, n+1, 2):
		for b in range(1, c+1):
			for a in range(c-b+1, b+1): #to ensure that ABC is a triangle
				if is_int2(median2(a,b,c)):
					print a,b,c
					count += 1
	return count

main(20)
print 'time', datetime.now() - s
'''
for n in range(1, 50):
	print n, main(n)
'''