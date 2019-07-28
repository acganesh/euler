data = []
with open('13_data.txt', 'rb') as f:
	for line in f:
		data.append(line)

data_int = [int(x) for x in data]
print str(sum(data_int))[0:10]