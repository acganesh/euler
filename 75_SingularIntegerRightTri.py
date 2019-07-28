from math import ceil, sqrt
from fractions import gcd
import datetime

@profile
def main():
	start = datetime.datetime.now()

	limit = 1500000
	vals = [0]*(limit+1)


	#a = m^2 - n^2, b = 2mn, c = m^2 + n^2

	iter_limit = int(ceil(sqrt(limit)))
	for m in range(1, iter_limit):
		for n in range(1, m):
			for k in range(1, limit):
				if gcd(m, n) == 1 and m % 2 != n % 2:
					a = k*(m**2 - n**2)
					b = k*(2*m*n)
					c = k*(m**2 + n**2)
					#print a, b, c
					#assert a**2+b**2 == c**2
				try:
					if a + b + c > limit:
						break
					vals[a+b+c] += 1
				except:
					pass

	total = sum([1 for x in vals if x == 1])
	print total
	print 'time', datetime.datetime.now() - start

main()