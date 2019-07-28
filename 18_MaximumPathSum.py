data = []

with open('18_data.txt', 'rb') as f:
	for line in f:
		data.append([int(x) for x in line.split()])


max_sums = data

row_ctr = -1 
col_ctr = 0

max_len = len(data)

while row_ctr >= (-1 - len(data) + 2):
	col_ctr = 0

	while col_ctr < max_len - 1:
		max_sums[row_ctr-1][col_ctr] = max(data[row_ctr][col_ctr]+data[row_ctr-1][col_ctr], data[row_ctr][col_ctr+1]+data[row_ctr-1][col_ctr])

		col_ctr += 1

	max_len -= 1

	row_ctr -= 1

print max_sums[0]

