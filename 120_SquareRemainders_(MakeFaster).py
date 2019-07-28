from datetime import datetime

s = datetime.now()

cache = [[-1]*(2*a**2) for a in range(1000+1)]
def cache_pow(a, n, mod):
	try:
		val = cache[a][n]
	except:
		print 'failed', a, n
	if val != -1:
		return val
	else:
		val = pow(a, n, mod)
		cache[a][n] = val
		return val


def remainder(a, n):
	mod = a**2
	val = (pow(a-1, n, mod) + pow(a+1, n, mod)) % mod
	return val

print remainder(7, 3)

def max_remainder(a):
	max_val = 0
	max_exp = None
	for exp in range(1, a**2-7):
		val = remainder(a, exp)
		if val > max_val: 
			max_val = val
			max_exp = exp
	return max_val

def main(limit):
	val = 3
	total = 0
	while val <= limit:
		total += max_remainder(val)
		if val % 100 == 0: print 'val',val
		#print val
		val += 1
	return total

'''
for a in range(1, 20):
	print a, max_remainder(a)
'''

print main(200)
print datetime.now() - s

