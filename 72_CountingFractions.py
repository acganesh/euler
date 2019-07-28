from fractions import Fraction
import fractions

from datetime import datetime

start = datetime.now()
frac_list = set()

def main(limit):
	denom = 1
	while denom <= limit:
		num = 1
		while num < denom:
			frac = Fraction(num, denom)
			if not frac in frac_list:
				frac_list.add(Fraction(num, denom))
				#frac_list.append(Fraction(num, denom))
			num += 1
		denom += 1

	#print sorted(frac_list)
	return len(frac_list)

def factor_sieve(n):
	t = list(range(n+1))
	sieve = [[] for x in range(n+1)]
	for x in range(2, n+1):
		if sieve[x] == []:
			t[x] = x-1
			for y in range(x, n+1, x):
				exp = 1
				num = y
				while num % x == 0:
					num //= x
					exp += 1
				sieve[y].append((x, exp-1))
				if y != x:
					t[y] = t[y]*(x-1) // x
	return sieve, t

def main2(n):
	t = factor_sieve(n)[1]
	return sum(t) - 1

print main2(10**6)

print datetime.now() - start