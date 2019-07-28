from fractions import gcd
import datetime
from math import sqrt

start = datetime.datetime.now()

squares = set([x**2 for x in range(1000)])

N = 101
lattice_cache = [[-1]*N for i in range(N)]
#print lattice_cache
def area(p1,p2,p3,p4):
	#x = [p1[0], p1[1], p1[2], p1[3]]
	#y = [p2[0], p2[1], p2[2], p2[3]]
	#val = 1/2*abs(p1[0]*p2[1] + p1[1]*p2[2] + p1[2]*p2[3] + p1[3]*p2[0] - p1[1]*p2[0] - p1[2]*p2[1] - p1[3]*p2[2] - p1[0]*p2[3])
	vals = 1./2*abs(p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p4[1]+p4[0]*p1[1] - p2[0]*p1[1] - p3[0]*p2[1] - p4[0]*p3[1] - p1[0]*p4[1])
	return vals

def area_2(a,b,c,d):
	return (a+c)*(b*d)/2


def lattice(p1, p2):
	a = abs(p2[0] - p1[0])
	b = abs(p2[1] - p1[1])
	if lattice_cache[a][b] == -1:
		lattice_cache[a][b] = (gcd(a,b)+1)
	return lattice_cache[a][b]

def boundary(p1, p2, p3, p4):
	return (lattice(p1, p2) + lattice(p2, p3) + lattice(p3, p4) + lattice(p4, p1) - 4)

def interior(p1, p2, p3, p4):	
	A = area(p1, p2, p3, p4)
	#A = area_2(a,b,c,d)
	# A
	B = boundary(p1, p2, p3, p4)
	I = A - B/2 + 1
	return I

def tests():
	c1 = (0,5)
	c2 = (-1,1)
	c3 = (3,-7)
	c4 = (-6,2)

	c1 = (0,0)
	c2 = (4,2)
	c3 = (4,0)
	c4 = (1,-3)
	print 'area',area(c1,c2,c3,c4)
	print 'interior',interior(c1,c2,c3,c4)
	print 'boundary',boundary(c1,c2,c3,c4)

#tests()
#print lattice((0,0),(1,2))

ctr = 0
M = 100
for a in range(1,M+1):
	for b in range(1,M+1):
		for c in range(1,M+1):
			for d in range(1,M+1):
				p1 = (a,0)
				p2 = (0,-d)
				p3 = (-c, 0)
				p4 = (0, b)
				'''
				p2 = (0,b)
				p3 = (-c, 0)
				p4 = (0, -d)
				'''
				I = interior(p1, p2, p3, p4)
				if I in squares:
					#print a,b,c,d, I
					ctr += 1
print ctr
print datetime.datetime.now() - start

#tests()