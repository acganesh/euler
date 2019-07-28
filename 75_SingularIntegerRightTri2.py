from math import sqrt, ceil
from fractions import gcd

limit = 1500000
vals = [0]*(limit+1)

iter_limit = int(ceil(sqrt(limit)))
for m in range(1, iter_limit, 2):
	for n in range(2, iter_limit - m, 2):
		if gcd(m, n) == 1:
			my_sum = abs(m**2 - n**2) + 2*m*n + m**2 + n**2
			for x in range(my_sum, limit, my_sum):
				vals[x] += 1

total = sum([1 for x in vals if x == 1])
print total