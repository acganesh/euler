def collatz(n):
	ctr = 0
	while (n > 1):
		if n % 2 == 0: n /= 2
		else: n = 3*n + 1
		ctr += 1
		#print n
	return ctr

max_len = 0
max_val = 0
n = 0
while n < 1000000:
	collatz_len = collatz(n)
	if collatz_len > max_len:
		max_len = collatz_len
		max_val = n
	n += 1
print max_len
print max_val



