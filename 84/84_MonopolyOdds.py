import itertools
from fractions import Fraction
from collections import Counter

squares = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

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

dice_table = prob_table(2, [1,2,3,4,5,6])
dice_vals = dice_table.keys()

squares_table = {}
for square in squares:
	squares_table[square] = 0

for val in dice_vals:
	prob = dice_table[val]
	square = squares[val]
	if square[:2] == 'CH':

	elif square[:2] == 'CC':
		squares_table['CH']
	squares_table[square] += prob

def tests():
	i1 = squares.index('JAIL')
	i2 = squares.index('E3')
	i3 = squares.index('GO')
	print i1, i2, i3

def calculate_odds():
	pass
