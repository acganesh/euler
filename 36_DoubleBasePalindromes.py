def is_palindromic(n):
	my_str = str(n)
	if my_str == my_str[::-1]:
		return True
	else:
		return False

def double_base_pal(n):
	if is_palindromic(n) and is_palindromic(bin(n)[2:]):
		return True
	else:
		return False

limit = 1000000

num = 0
my_sum = 0

while num <= limit:
	if double_base_pal(num): my_sum += num
	num += 1

print my_sum