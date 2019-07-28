from math import sqrt
from math import floor

for i in range(1, 1000):
	for j in range(1, 1000):
		k = sqrt(i ** 2 + j ** 2)
		if k == floor(k) and i+j+k == 1000:
			print i, j, k
			print i*j*k