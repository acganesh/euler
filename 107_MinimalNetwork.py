import networkx as nx

def dijkstra(nodes, distances, source):
	'''
	nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
	distances = {
	    'B': {'A': 5, 'D': 1, 'G': 2},
	    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
	    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
	    'G': {'B': 2, 'D': 1, 'C': 2},
	    'C': {'G': 2, 'E': 1, 'F': 16},
	    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
	    'F': {'A': 5, 'E': 2, 'C': 16}}
	'''

	unvisited = {node: None for node in nodes} #using None as +inf
	visited = {}
	current = source
	currentDistance = 0
	unvisited[current] = currentDistance

	while True:
	    for neighbour, distance in distances[current].items():
	        if neighbour not in unvisited: continue
	        newDistance = currentDistance + distance
	        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
	            unvisited[neighbour] = newDistance
	    visited[current] = currentDistance
	    del unvisited[current]
	    if not unvisited: break
	    candidates = [node for node in unvisited.items() if node[1]]
	    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

	return visited


nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
	'A': {'B':16, 'D':21, 'C':12},
	'B': {'A':16, 'D':17, 'E':20},
	'C': {'A':12, 'D':28, 'F':31},
	'D': {'A':21, 'B':17, 'C':28, 'E':18, 'F':19, 'G':23},
	'E': {'B':20, 'D':18, 'G':11},
	'F': {'D':19, 'G':27, 'C':31},
	'G': {'E':11, 'D':23, 'F':27}
}
#edges = [[16,1,2], [12, 1, 3], [21, 1, 4], [17, 2, 4], [20, 2, 5], [28, 3, 4], [18, 4, 5], [31, 3, 6], [19,4, 6], [23, 4,6],[11,5,7], [27, 7,6]]
edges = [[16, 'A', 'B'], [12, 'A', 'C'], [21, 'A', 'D'], [17, 'B', 'D'], [20, 'B', 'E'], [28, 'C', 'D'], [18, 'D', 'E'], [31, 'C', 'F'], [19, 'D', 'F'], [23, 'D', 'G'], [11, 'E', 'G'], [27, 'G', 'F']]

def convert_edges(edges):
	nodes = []
	distances = {}

	for item in edges:
		val0 = item[0]; val1 = item[1]; val2 = item[2]
		if val1 not in nodes:
			nodes.append(val1)
		if val2 not in nodes:
			nodes.append(val2)
		try:
			distances[val1][val2] = val0
		except KeyError:
			distances[val1] = {}
			distances[val1][val2] = val0
		try:
			distances[val2][val1] = val0
		except KeyError:
			distances[val2] = {}
			distances[val2][val1] = val0
	return nodes, distances
print convert_edges(edges)


def dijkstra2(edges, source):
	nodes, distances = convert_edges(edges)
	nodes = tuple(nodes)
	return dijkstra(nodes, distances, source)

print 'EQUALITY'
print dijkstra2(edges, 'A') == dijkstra(nodes, distances, 'A')

def reverse_delete(nodes, distances):
	pass

def is_connected(edges, node1, node2):
	print 'e',edges
	sp = dijkstra2(edges, node1)
	try:
		if sp[node2] != 0:
			return True
		else:
			return False
	except:
		return False

#edges2= [[7,1,2],[8,2,3],[5,3,5],[7,2,5],[9,2,4],[5,1,4],[15,4,5],[6,4,6],[8,5,6],[9,5,7],[11,6,7]]
edges2 = [[7, 'A', 'B'], [8, 'B', 'C'], [5, 'C', 'E'], [7, 'B', 'E'], [9, 'B', 'D'], [5, 'A', 'D'], [15, 'D', 'E'], [6, 'D', 'F'], [8, 'E', 'F'], [9, 'E', 'G'], [11, 'F', 'G']]

'''
for item in edges2:
	val0 = item[0]
	val1 = item[1]
	val2 = item[2]
	edges3.append([val0, nodes[val1-1], nodes[val2-1]])
print edges3
'''

def reverse_delete(edges):
	edges = sorted(edges, key = lambda x: x[0], reverse = True)
	i = 0
	while i < len(edges):
		edge = edges[i]
		#edges[i][0] = float('Inf')
		del edges[i]
		#edges.pop(i)
		if not is_connected(edges, edge[1], edge[2]):
			edges.insert(i, edge)
		i += 1
	return edges

print reverse_delete(edges2)




