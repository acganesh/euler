from Euler import prime_sieve
import itertools

repo_primes = prime_sieve(1000000)
prime_repo = set(repo_primes)

primes = prime_sieve(10000)
prime_set = set(primes)

print primes

def is_prime(N):
	return N in prime_repo

def is_prime_pair_set(*args):
	for a,b in itertools.combinations(args, 2):
		if not is_prime(int(str(a)+str(b))): 
			return False
		if not is_prime(int(str(b)+str(a))):
			return False
	return True

def get_pairs(prime_set):
	pairs = set([])
	for a,b in itertools.combinations(prime_set, 2):
		if is_prime_pair_set(a,b):
			pairs.add(frozenset((a,b)))
	return pairs

pairs = get_pairs(prime_set)
print pairs

triples = set([])
for a,b in itertools.combinations(pairs, 2):
	if len(a.intersection(b)) == 1:
		union = a.union(b)
		if is_prime_pair_set(*union):
			triples.add(union)

print triples

quads = set([])
for a,b in itertools.combinations(triples, 2):
	if len(a.intersection(b)) == 2:
		union = a.union(b)
		if is_prime_pair_set(*union):
			quads.add(union)

print quads

quints = []
min_sum = 100000
for a,b in itertools.combinations(quads, 2):
	if len(a.intersection(b)) == 3:
		union = a.union(b)
		if is_prime_pair_set(*union):
			prime_sum = sum(union)
			if prime_sum < min_sum:
				min_sum = prime_sum
			quints.append(union)

#print quints
#print min_sum
