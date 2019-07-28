from Euler import is_pandigital
from math import sqrt, log10

def main(limit):
	count = 2
	fibs = [0, 1]
	while count < limit:
		val = sum(fibs) % (10**9)
		fibs[0] = fibs[1]
		fibs[1] = val
		val_str = str(val)
		if is_pandigital(val_str):
			if is_pandigital(str(top9_digits(count))):
				print count
		count += 1

def top9_digits(n):
	phi = (1 + sqrt(5)) / 2.0
	t = n*log10(phi) - log10(sqrt(5))
	return int(pow(10, t - int(t) + 8))

print main(1000000)