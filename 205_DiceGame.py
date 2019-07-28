import itertools
from fractions import Fraction
from collections import Counter

def prob_table(num_rolls, vals):
	rolls = itertools.product(vals, repeat = num_rolls)
	total = len(vals) ** num_rolls
	sums = []
	for item in rolls:
		sums.append(sum(item))
	sums = Counter(sums)
	probs = {}
	for val in sums.keys():
		probs[val] = Fraction(sums[val], total)
	return probs

def main():
	prob1 = prob_table(9,[1,2,3,4])
	prob2 = prob_table(6,[1,2,3,4,5,6])

	prob1_keys = prob1.keys()
	prob2_keys = prob2.keys()

	prob = 0
	for val1 in prob1_keys:
		val1_prob = prob1[val1]
		for val2 in prob2_keys:
			if val1 > val2:
				prob += (val1_prob)*prob2[val2]
	print float(prob)

main()
