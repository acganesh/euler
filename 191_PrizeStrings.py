from scipy.special import binom
from datetime import datetime
#unfinished, doesn't quite work.
#the intersection part isn't counted correctly.

s = datetime.now()
def dynamic(N):
	num = 1
	l = [1, 1, 0, 1, 0, 0]
	if N == 1:
		return sum(l)
	while num <= N-1:
		w = [l[0]+l[1]+l[2], l[0], l[1],l[0]+l[1]+l[2]+l[3]+l[4]+l[5],l[3],l[4]]
		l = list(w)
		num += 1
	return sum(w)

A = dynamic(30)
print 'D2', A
print datetime.now() - s

#glorious scratch work!
#l = [0L0A, 0L1A, 0L2A, 1L0A, 1L1A, 1L2A]

#0
#n = 1
#'A', 'O', 'L'
#l = [1, 1, 0, 1, 0, 0]
#w = [0,0,0,0,0,0]
#W = [l[0]+l[1]+l[2], l[0], l[1],l[0]+l[1]+l[2]+l[3]+l[4]+l[5],l[3],l[4]]
#n = 2
#[('LO', 1), ('LA', 1), ('OL', 1), ('OO', 0), ('OA', 0), ('AL', 1), ('AO', 0), ('AA', 0)]

#l = [0L0A, 0L1A, 0L2A, 1L0A, 1L1A, 1L2A]
#r = [,,0,1,0,0]

#l_counts = [0L0A+0L1A+0L2A,0L0A,0L1A+0L2A,0L0A+0L1A+1L2A,1L1A,1L1A]
#OLOA
	#L: 1LOA
	#O: OLOA
	#A: 0L1A
#OL1A
	#L: 1L0A
	#O: OL0A
	#A: OL2A
#OL2A
	#L: 1L0A
	#O: OLOA
	#A: -OL2A
#1LOA
	#L: -1LOA
	#O: 1LOA
	#A: 1L1A
#1L1A
	#L: -1L1A
	#O: 1L1A
	#A: 1L2A
#1L2A
	#L: -1L2A
	#O: 1L0A
	#A: -1L2A
#l = [, 1+1, 2, ]
#2 = ''


def num(days):
	X = 0
	Y = 0
	Z = 0

	num_A = 3
	while num_A <= days:
		X += (days-num_A+1)*(2**(days - num_A))
		num_A += 1

	num_L = 2
	while num_L <= days:
		Y += binom(days, num_L)*2**(days - num_L)
		num_L += 1

	for num_A in range(3, days-1):
		for num_L in range(2, days - num_A+1):
			Z += (days - num_A+1)*binom(days-num_A, num_L)*(2**(days-num_L - num_A))

	#print X, Y, Z
	return (3**days) - X - Y + Z
#_ _ _ _ _ 
#num_A = 3
#	val: 3*(2^2) = 12
#num_A = 4
#	val: 2*(2^1) = 4
#num_A = 5
#	val: 1*(2^0) = 1
#A = 17

#num_L = 2
#	val: 5C2*2^3 = 80
#num_L = 3
#	val: 5C3*2^2 = 40
#num_L = 4
#	val: 5C4*2^1 = 10
#num_L = 5
#	val: 5C5*2^0 = 1
#B = 131

#both:
	#num_A = 3
		#num_L = 2
		#	val: 3*2C2*(2**0) = 3
#3**5 - 131 - 17 + 3

#doesn't work for some reason, I think I'm double counting

#Let's do this dynamically.

def check_late(string):
	if string.count('L') > 1:
		return True
	else:
		return False

#print check_late('L')

def check_late2(val, L_count):
	if L_count == 1 and val == 'L':
		return True
	else:
		return False


def check_absent(string):
	if 'AAA' in string:
		return True
	else:
		return False

def check_absent2(string):
	if string[-3:] == 'AAA':
		return True
	else:
		return False
#print check_absent('L')

def check_prize(string, val, L):
	if not check_late2(val, L) and not check_absent2(string):
		return True
	else:
		return False

def check_prize2(string):
	if not check_absent(string) and not check_late(string):
		return True
	else:
		return False

def check_prize3(string):
	if not check_absent(string):
		if not check_late(string):
			return True
	return False

vals = ('L', 'O', 'A')
#works, but far too slow
def recursive(days):
	days = days + 1
	#strings = [[] for _ in range(days)]
	#strings[0] = ['']
	strings = [('', 0)]

	L_counts = [0]
	length = 0
	count = 0

	while length < days-1:
		prev_strings = strings
		strings = []
		#L_counts = []
		for string in prev_strings:
			for x in vals:
				L_count = string[1]
				cand_str = string[0] + x
				if x == 'L':
					L_count = L_count + 1
				if check_prize(cand_str, x, L_count-1):
					strings.append((cand_str, L_count))
					count += 1
		length += 1
		#print length
	print strings
	return len(strings)







