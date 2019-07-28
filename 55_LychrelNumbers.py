def is_palindromic(n):
	my_str = str(n)
	if my_str == my_str[::-1]:
		return True
	else:
		return False

def add_to_reverse(n):
	reverse = int(str(n)[::-1])
	return n + reverse



def is_Lychrel(n):

	start = True
	ctr = 0

	while is_palindromic(n) == False or start == True:
		my_sum = add_to_reverse(n)
		n = my_sum
		start = False
		ctr += 1

		if ctr > 50: 
			return True

	return False

n = 0
num_Lychrel = 0

while n <= 10000:
	if is_Lychrel(n): num_Lychrel += 1
	n += 1

print num_Lychrel