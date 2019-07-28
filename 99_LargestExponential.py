import csv
from math import log

my_max = 0
max_line_number = 0

def log_val(my_list):
	base = my_list[0]
	exp = my_list[1]
	return exp*log(base)

with open('99_data.txt', 'rb') as f:
	
	my_reader = csv.reader(f)

	line_num = 1

	for my_list in my_reader:
		my_list_int = [int(x) for x in my_list]
		my_log_val = log_val(my_list_int)

		if my_log_val > my_max:
			my_max = my_log_val
			max_line_number = line_num
		line_num += 1

print my_max
print max_line_number



