from fractions import gcd

def order(n, a):
	if not gcd(n, a) == 1:
		return 0
	else:
		k = 1
		while not (a ** k) % n == 1:
			k += 1
			#print k
		return k

max_result = 0
max_num = 0
num = 1000

while num > 1:
	result = order(num, 10)
	if result > max_result:
		max_result = result
		max_num = num
	#print num
	if max_result > num - 1:
		break
	num -= 1

print max_result, max_num