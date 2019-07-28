limit = 20000
vals = [0]*limit

import datetime
start = datetime.datetime.now()

def layer(x,y,z,n):
	#x,y,z = dim[0], dim[1], dim[2]
	#num = (2*x+2*y+4*(n-1))*z + 2*(x*y + x*(n-1)*2 + y*(n-1)*2 + 2*(n-1)*(n-2))
	num = 2*(x*y+y*z+z*x)+4*(x+y+z+n-2)*(n-1)
	return num

#print layer(3,2,1,3)

def main_refined_iteration():
	x = 1
	while layer(x,x,x,1) <= limit:
		#print x,x,x,1,layer(x,x,x,1)
		y=x
		while layer(x,y,x,1) <= limit:
			#print x,y,x,1,layer(x,y,x,1)
			z=y
			while layer(x,y,z,1) <= limit:
				#print x,y,z,1,layer(x,y,z,1)
				n = 1
				d = layer(x,y,z,n)
				while d < limit:
					vals[d] += 1
					n += 1
					d = layer(x,y,z,n)
					#print x,y,z,n,d
				z += 1
			y+= 1
		x += 1
	for d in range(limit):
		if vals[d] == 1000:
			print 'Final val',d

def main():
	x = 1
	y = 1
	z = 1
	n = 1
	for x in range(1, limit):
		if layer(x,y,z,n) < limit:
			continue
		for y in range(1, x+1):

			for z in range(1, y+1):
				n = 1
				d = layer(x,y,z,n)
				print x,y,z,n,d
				while d < limit:
					vals[d] += 1
					n += 1
					d = layer(x,y,z,n)
					print x,y,z,n,d

	for d in range(limit):
		if vals[d] == 1000:
			print d

	#print [(x, vals[x]) for x in range(1000) if vals[x] > 50]

#main()
main_refined_iteration()
#main()

print datetime.datetime.now() - start

def C(n):
	limit = n
	ctr = 0
	quads = []
	for x in range(1,limit+1):
		for y in range(x,limit+1):
			for z in range(y, limit+1):
				for L in range(1, limit+1):
					if layer(x,y,z,L) == n:
						quads.append((x,y,z,L))
						ctr += 1
						#print x,y,z,L
	return ctr, quads

#print C(118)

#print C(154)

#print C(22)
'''

def min_n(val):
	while True:
		n = 1
		if C(n) == val:
			return n
		else:
			n += 1
print min_n(10)
print C(22)
print C(46)
print C(78)
print C(118)
'''

