import math
from math import floor
import numpy as np

#global verbose = True

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

#Gets coefficient of X^N in (1+x+x^2+...+x^r)^n
def binomial_coeff_sum(n, N, r):
	sum = 0
	upper_bound = min(n, (N/(r+1)))

	for i in range(0, upper_bound+1):
		sum += ((-1) ** i) * nCr(n, i) * nCr(N - i*(r+1) + n-1, n-1)

	return sum

def simulate(n):
	'''
	num_colors = 7
	num_draws = 20
	num_of_each_ball =10
	'''
	num_colors = 3
	num_draws = 3
	num_of_each_ball = 2

	lengths = []
	simulation_ctr = 0

	freqs = [0, 0, 0, 0, 0, 0, 0]

	while simulation_ctr < n:

		balls_in_urn = [num_of_each_ball for x in range(num_colors)]
		balls_drawn = [0 for x in range(num_colors)]

		#print balls_in_urn
		#print balls_drawn

		ctr = 0
		while ctr < num_draws:
			draw = np.random.randint(num_colors)
			if balls_in_urn[draw] >= 1:
				balls_in_urn[draw] -= 1
				balls_drawn[draw] += 1
				ctr += 1
				#print balls_drawn

		#print balls_drawn
		#print "NEXT"

		#print balls_drawn


		#vals = [[2,1,1],[1,2,1],[1,1,2],[0,2,2],[2,0,2],[2,2,0]]

		vals = [[1,1,1],[2,1,0],[2,0,1],[1,2,0],[1,0,2],[0,2,1],[0,1,2]]

		index = vals.index(balls_drawn)
		#print index
		
		freqs[vals.index(balls_drawn)] += 1

		if (simulation_ctr % 100000) == 0: print freqs
		#print freqs

		while 0 in balls_drawn:
			balls_drawn.remove(0)

		length = len(balls_drawn)
		lengths.append(length)

		simulation_ctr += 1

		if (simulation_ctr % 100000) == 0: print simulation_ctr
	#print lengths

	print float(sum(lengths))/(len(lengths))
	#print freqs

def search_for_rational_approx(n):
	candidates = []
	for i in range(1,100):
		j = i*n
		if ((j - floor(j)) <= 0.01) or ((floor(j) + 1 - j) <= 0.01):
			candidates.append([j,i])
	print candidates



def compute_expected_value():
	#first range argument is 2, since for n = 1 there are clearly no possibilities.  
	upper_bound = 6

	weighted_totals = []
	totals = []
	my_sum = 0

	N = [18, 17, 16, 15, 14, 13]
	r = 9
	n = [2, 3, 4, 5, 6, 7]

	#print binomial_coeff_sum(n[0], N[0], r)
	#print 

	for i in range(0, upper_bound):
		val = binomial_coeff_sum(n[i], N[i], r)
		totals.append(val)
		weighted_val = (i+2) * val
		weighted_totals.append(weighted_val)
		my_sum += val
	print totals
	print weighted_totals
	print my_sum
	print sum(totals)

	#print my_sum

	print float(sum(weighted_totals))/float(my_sum)
	

	'''
	for i in range(1, upper_bound+1):
		val = binomial_coeff_sum(i, 20, 10)
		weighted_val = i * val
		weighted_totals.append(weighted_val)
		my_sum += val
	print weighted_totals
	print my_sum
	print float(sum(weighted_totals))/float(my_sum)
	'''

#compute_expected_value()
#search_for_rational_approx(2.611107)
simulate(10000000)

'''
print binomial_coeff_sum(2, 18, 9)
print binomial_coeff_sum(3, 17, 9)
print binomial_coeff_sum(4, 16, 9)
print binomial_coeff_sum(5, 15, 9)
print binomial_coeff_sum(6, 14, 9)
print binomial_coeff_sum(7, 13, 9)
'''

#compute_expected_value()

