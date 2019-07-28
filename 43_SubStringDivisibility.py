#d_4 == 0 mod 2
#d_3 + d_4 + d_5 == 0 mod 3
#d_6 = 0, 5

import itertools

def is_sub_string_divisible(n):
	my_str = str(n)
	if (int(my_str[3]) % 2 == 0 and sum([int(x) for x in my_str[2:5]]) % 3 == 0
	and int(my_str[5]) % 5 == 0 and int(my_str[4:7]) % 7 == 0
	and int(my_str[5:8]) % 11 == 0 and int(my_str[6:9]) % 13 == 0
	and int(my_str[7:10]) % 17 == 0):
		return True
	else:
		return False
	
six_cands = [0, 5]
four_cands = [0, 2, 4, 6, 8]

ssd_nums = []

for d6 in six_cands:
	for d4 in four_cands:
		if not (d4 == d6):
			my_list = range(0, 10)
			my_list.remove(d4)
			my_list.remove(d6)

			perms = itertools.permutations(my_list)
			for item in perms:
				str_1 = str(item[0]) +str(item[1]) + str(item[2])
				d4_str = str(d4)
				str_2 = str(item[3])
				d6_str = str(d6)
				str_3 = str(item[4]) + str(item[5]) + str(item[6]) + str(item[7])

				num = str_1 + d4_str + str_2 + d6_str + str_3

				if is_sub_string_divisible(num):
					ssd_nums.append(num)

print sum([int(x) for x in ssd_nums]) 

