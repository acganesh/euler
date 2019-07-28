from math import sqrt, floor, ceil
lower_limit = int(floor(sqrt(1020304050607080900)))
upper_limit = int(ceil(sqrt(1929394959697989990)))

#print lower_limit, upper_limit

def check_if_form(n):
	my_list = list(str(n))
	try:
		if my_list[0] == '1' and my_list[2] == '2' and my_list[4] == '3' and my_list[6] == '4' and my_list[8] == '5' and my_list[10] == '6' and my_list[12] == '7' and my_list[14] == '8' and my_list[16] == '9' and my_list[18] == '0':
			return True
	except:
		pass
	return False


n = lower_limit
while n <= upper_limit:
	if check_if_form(n**2):
		print n
	n += 10
	#if n % 100000000 == 0:
		#print n

'''
i = 10**9
while i < 1.1*(10**9):
	if check_if_form(10*i):
		print 10*i
	i += 1
	if i % 10000000 == 0:
		print n
'''