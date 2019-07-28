from fractions import Fraction
def is_bouncy(n):
	n_str = str(n)
	length = len(n_str)
	if length <= 2:
		return False
	ctr = 1
	inc = None
	dec = None
	'''
	if n_str[0] < n_str[1]:
		inc = True
	elif n_str[0] > n_str[1]:
		dec = True
	'''

	while ctr < length-1:
		if n_str[ctr] > n_str[ctr - 1] and inc == None:
			inc = True
		elif n_str[ctr] < n_str[ctr - 1] and inc == None:
			dec = True
		if inc:
			if n_str[ctr] > n_str[ctr+1]:
				return True
		elif dec:
			if n_str[ctr] < n_str[ctr+1]:
				return True
		ctr += 1
	return False

def main(limit):
	num = 1
	count = 0
	while num <= limit:
		if is_bouncy(num):
			count += 1
		num += 1
	return Fraction(count, limit)

def main2(target):
	num = 1
	count = 0
	val = None
	while val != target:
		if is_bouncy(num):
			count += 1
		val = Fraction(count, num)
		num += 1
	return num-1

print main2(Fraction(99, 100))
#print main(21780)


