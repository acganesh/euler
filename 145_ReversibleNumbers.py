from datetime import datetime

s = datetime.now()

cache = set([])
def is_reversible(n):
	n_str = str(n)
	n_str_rev = n_str[::-1]
	if n_str_rev[0] == '0':
		return False
	val = n + int(n_str_rev)
	for num in str(val):
		if int(num) % 2 == 0:
			return False
	return True

def main(limit):
	val = 1
	count = 0
	while val <= limit:
		if is_reversible(val):
			count += 1
			#print val
		val += 1
		#if val % 1000000 == 0: print val
	return count

count = main(10**8)
#if exp is a multiple of 4, main(10**exp) = main(10**(exp+1))
print count

print datetime.now() - s

