from math import sqrt, floor

def get_triangles(perimeter_limit):

	a_range = range(1, perimeter_limit+1)
	b_range = range(1, perimeter_limit+1)

	triangles = [[] for x in range(perimeter_limit+1)]
	

	for a in a_range:
		for b in b_range:
			c = sqrt(float(a**2) + float(b**2))
			if floor(c) == c:
				perimeter = int(a+b+c)
				if perimeter <= perimeter_limit:
					triangles[perimeter].append([a,b,c])

	return triangles

triangles = get_triangles(1000)
num_of_triangles = map(len, triangles)
my_max = max(num_of_triangles)
#print my_max
print num_of_triangles.index(my_max)



