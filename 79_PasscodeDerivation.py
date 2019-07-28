def parse():
	data = []
	with open('79_data.txt', 'rb') as f:
		for line in f:
			data.append(line.replace('\n', ''))
	return set(data)

data = parse()
print data

def create_dict_map(data):
	graph = {}
	for key in range(10):
		graph[str(key)] = set([])
	for num in data:
		d1 = num[0]; d2 = num[1]; d3 = num[2]
		graph[d1].add(d2)
		graph[d1].add(d3)
		graph[d2].add(d3)
	return graph

print create_dict_map(data)

#73162890



