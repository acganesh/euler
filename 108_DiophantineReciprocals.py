from Euler import factor

#Adds 2*(exp-1) to sieve to check only squares
def factor_sieve(n):
	sieve = [[] for x in range(n+1)]
	for x in range(2, n+1):
		if sieve[x] == []:
			for y in range(x, n+1, x):
				exp = 1
				num = y
				while num % x == 0:
					num //= x
					exp += 1
				sieve[y].append((x, 2*(exp-1)))
	return sieve

def num_div(tuples):
	num = 1
	for t in tuples:
		num *= (t[1]+1)
	return num

s = factor_sieve(10000000)

def num_sols(n):
	num = num_div(s[n])
	return (num + 1)/2

def main(limit):
	n = 1
	while True:
		if num_sols(n) > limit:
			return n
		n += 1

print main(1000)

