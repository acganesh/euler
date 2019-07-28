from fractions import Fraction

def totient_sieve(n):
	t = list(range(n+1))
	sieve = [False]*(n+1)
	for x in range(2, n+1):
		if sieve[x] == False:
			t[x] = x-1
			for y in range(x, n+1, x):
				sieve[y] = True
				if y != x:
					t[y] = t[y]*(x-1) // x
	return t

t_vals = totient_sieve(10000000)
#print t_vals
def resilience(d):
	return Fraction(t_vals[d], d-1)

'''
for d in range(2, 20):
	print resilience(d)
'''

def main(limit):
	ctr = 2
	while True:
		frac = Fraction(t_vals[ctr], ctr-1)
		if frac < limit:
			return ctr, frac
		ctr += 1

print main(Fraction(15499, 94744))

#print main(Fraction(4, 10))
#print main(12)