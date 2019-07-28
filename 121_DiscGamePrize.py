import itertools
from collections import Counter
from fractions import Fraction
from datetime import datetime
from math import factorial
from operator import mul

s = datetime.now()

def prob(string):
	p = 1
	counts = Counter({'red':1, 'blue':1, 'total':2})
	for char in string:
		if char == 'R':
			p *= Fraction(counts['red'],counts['total'])
		elif char == 'B':
			p *= Fraction(counts['blue'],counts['total'])
		counts['red'] += 1
		counts['total'] += 1
	return p

#empirical pattern observed:
#String BBRBB will have m/N! probability
#where m is the product of the indices of the R's
#N is the length of the string

def val(string):
	val = 1
	ctr = 1
	for char in string:
		if char == 'R':
			val *= ctr
		ctr += 1
	return val

def main(n):
	probability = 0
	for a in range(n/2+1,n+1):
		string = 'B'*a+'R'*(n-a)
		#print string
		perms = set([''.join(p) for p in itertools.permutations(string)])
		for perm in perms:
			probability += prob(perm)
	return probability


def main2(n):
	#probability = 0
	num = 0
	for a in range(n/2+1,n+1):
		string = 'B'*a+'R'*(n-a)
		#print string
		perms = set([''.join(p) for p in itertools.permutations(string)])
		for perm in perms:
			num += val(perm) 
			print perm, val(perm)
	return num
	#return Fraction(num, factorial(n+1))


def prod(list):
	return reduce(mul, list, 1)

#from num returned by main3, compute max prize fund
def max_fund(n, val):
	return factorial(n+1)/val

def main3(n):
	total = 0
	for a in range((n-1)/2+1):
		tuples = itertools.combinations(range(1,n+1), a)
		for t in tuples:
			num = prod(t)
			total += num
			#print t,num
	fund = max_fund(n, total)
	return fund

print main3(15)
print datetime.now() - s

