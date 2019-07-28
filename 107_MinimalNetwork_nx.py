import networkx as nx
import csv

def parse():
	data = []
	with open('107_data.txt', 'rb') as f:
		reader = csv.reader(f)
		for item in reader:
			data.append(item)

	G = nx.Graph()

	for i in range(40):
		for j in range(40):
			if data[i][j] != '-':
				G.add_edge(i, j, weight = int(data[i][j]))

	return G

def main(G):
	init_cost = 0
	for start, end, weight in G.edges(data=True):
		init_cost += weight['weight']
	print 'Initial cost: ', init_cost

	MST = nx.minimum_spanning_tree(G)

	final_cost = 0
	for start, end, weight in MST.edges(data=True):
		final_cost += weight['weight']
	print 'Final cost: ', final_cost

	print 'Savings: ', init_cost - final_cost

def test():
	nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	G = nx.Graph()

	for node in nodes:
		G.add_node(node)

	G.add_edge('A','B',weight=16)
	G.add_edge('A','C',weight=12)
	G.add_edge('A','D',weight=21)
	G.add_edge('B','D',weight=17)
	G.add_edge('B','E',weight=20)
	G.add_edge('C','D',weight=28)
	G.add_edge('C','F',weight=31)
	G.add_edge('D','E',weight=18)
	G.add_edge('D','F',weight=19)
	G.add_edge('D','G',weight=23)
	G.add_edge('E','G',weight=11)
	G.add_edge('F','G',weight=27)

	total = 0
	for start, end, weight in G.edges(data=True):
		print start, end, weight
		total += weight['weight']
	print 'Total cost: ', total

	total = 0
	MST = nx.minimum_spanning_tree(G)
	for start, end, weight in MST.edges(data=True):
		print start, end, weight
		total += weight['weight']
	print 'Total cost: ', total

G = parse()
main(G)