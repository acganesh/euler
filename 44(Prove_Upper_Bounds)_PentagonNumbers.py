#n(3n-1)/2 - m(3m-1)/2
#(3n^2 - n)/2 - (3m^2 -m) /2
#[3(n^2-m^2) - (n-m)]/2
#[3(n-m)(n+m-1)]/2

import sys
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def pentagonal(n):
	return n*(3*n-1)/2

pent_list = []
pent_set = set()
pent_range = range(1, 20000)

for i in pent_range:
	pent_list.append(pentagonal(i))
	pent_set.add(pentagonal(i))

n_range = range(1, 10000)
m_range = range(1, 10000)

min_diff = sys.maxint
min_n = None
min_m = None

for n in n_range:
	for m in m_range:
		n_pent = pent_list[n-1]
		m_pent = pent_list[m-1]

		my_sum = m_pent + n_pent
		my_diff = abs(m_pent - n_pent)
		#if not(binary_search(pent_list, my_sum) == -1) and not(binary_search(pent_list, my_diff) == -1):
		if my_sum in pent_set and my_diff in pent_list:
			print m_pent, n_pent
			if my_diff < min_diff:
				min_diff = my_diff
				min_n = n_pent
				min_m = m_pent
				
print min_diff, min_n, min_m

#Kind of just brute force: Need to set more rigorous bounds




