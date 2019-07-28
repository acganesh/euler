from decimal import Context, Decimal
from math import sqrt, floor, ceil
import re
import datetime

squares = set([x**2 for x in range(105)])

start = datetime.datetime.now()

def cont_frac(N):
	context = Context(prec = 1000)
	val = Decimal(context.sqrt(N))
	init_val = floor(val)
	rep = [init_val]
	ctr = 1
	while floor(val) != 2*init_val:
		val = Decimal(context.divide(1,(context.subtract(val,Decimal(floor(val))))))
		rep.append(floor(val))
		ctr += 1
	return rep

def main(limit):
	num = 2
	num_odd = 0
	while num <= limit:
		if num not in squares:
			rep = cont_frac(num)
			freq = len(rep)-1
			if freq % 2 == 1.0:
				num_odd += 1
		num +=1 
	return num_odd

print main(10**4)
print datetime.datetime.now() - start

############ unused but interesting code ###########

#regex method
def rep_sequence(tuple):
	regex = re.compile(r'(.+ .+)( \1)+')
	string = ''
	for num in tuple:
		string += str(int(num))
		string += ' '
	match = regex.search(string)
	return match.group(2)

def source():
    return itertools.cycle((1, 0, 1, 4, 8, 2, 1, 3, 3, 1))

def guess_period(source, minlen=1, maxlen=100, trials=1000):
    for n in range(minlen, maxlen+1):
        p = [j for i, j in zip(range(n), source)]
        if all([j for i, j in zip(range(n), source)] == p
               for k in range(trials)):
            return tuple(p)
    return None

####

import itertools

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def fft_freq(vals):
	N = 300
	N = len(vals)
	X = np.array((vals))

	# Compute the FFT
	W    = np.fft.fft(X)
	freq = np.fft.fftfreq(N,1)

	# Look for the longest signal that is "loud"
	threshold = 10
	idx = np.where(abs(W)>threshold)[0][-1]

	max_f = abs(freq[idx])
	if max_f == 0:
		max_f = 1.0
	period = 1/max_f
	#print "Period estimate: ", period
	return period




