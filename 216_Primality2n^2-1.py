from Euler import is_prime, factor

def main(limit):
	num = 1
	vals = []
	while num < limit:
		val = 2*num**2-1
		vals.append(val)
		if not is_prime(val):
			print val, factor(val)
		num += 1
	return vals

print main(100)
