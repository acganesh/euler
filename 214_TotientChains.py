from datetime import datetime
from Euler import prime_sieve
import fractions

#primes = prime_sieve(40000000)

cache = [-1]*40000000
len_cache = [-1]*40000000
def phi(n):
	val = cache[n]
	if val != -1:
		return val
	else:
	    amount = 0
	    for k in range(1, n + 1):
	        if fractions.gcd(n, k) == 1:
	            amount += 1
	    cache[n] = amount
	    return amount
	    
def totient_chain(n):
	chain = [n]
	ctr = 1
	while n > 1:
		chain.append(phi(n))
		n = phi(n)
		val = len_cache[n]
		if val != -1:
			return val
		ctr += 1
	for ind, num in enumerate(chain):
		len_cache[num] = ctr - ind
	return ctr

print totient_chain(5)

def main(limit,length):
	n = 2
	count = 0
	while n <= limit:
		if totient_chain(n) == length:
			count += 1
		n += 1
		if n % 1000 == 0:
			print n
	return count

main(4000000, 25)

s = datetime.now()

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

#totient_vals = totient_sieve(40000000)
print datetime.now() - s