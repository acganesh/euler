#tangent line to arbitary curve:
#y - y_0 = dy/dx(x - x_0)
#Performing implicit differentiation:
#8x + 2y*dy/dx = 0
#dy/dx = -8x/(2y) = -4(x/y)

#normal line slope: 4*(y/x)

#Calculating the intersection between line and ellipse
#y = mx + b
#4x^2 + (mx+b)^2 = 100
#4x^2 + m^2x^2 + 

import numpy as np
from math import pi
from math import sqrt


#|u||v| cos(x) = u dot v
def angle(v1, v2):
	v1 = np.asarray(v1); v2 = np.asarray(v2)
	return np.arccos(float(np.dot(v1, v2)) / (np.linalg.norm(v1)*np.linalg.norm(v2)))

#print angle((0,1), (1,0))

def intersection(v, p):
	#y - p[1] = slope(x - p[0])
	#b = slope*p[0] + p[1]
	M = float(v[1])/v[0] #slope
	b = M*p[0]+p[1]

	print M, b

	val1 = (-2*b*M + sqrt(4*(b*M)**2 - 4*(4+M**2)*(b**2-100)))/(2*(4+M**2))
	val2 = (-2*b*M - sqrt(4*(b*M)**2 - 4*(4+M**2)*(b**2-100)))/(2*(4+M**2))

	print 'VALS!',val1, val2

def normal_angle(p, p0):
	vec = [a-b for a,b in zip(p, p0)]
	x = float(p[0]); y = float(p[1])
	normal = (4*y/x, p)
	vec_normal = (x+normal[0], y+normal[0])
	return angle(vec, vec_normal)

def rotate_vec(v, theta):
	R = np.asarray([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
	v = np.asarray(v)
	return np.dot(R, v)


def main():
	p1 = [0, 10.1]
	p2 = [1.4, -9.6]
	theta = normal_angle(p2, p1)
	print 'theta', theta*180/pi
	v = [b-a for a,b in zip(p1, p2)]
	v_r = rotate_vec(v, 2*theta)
	print 'v_r', v_r
	v_r2 = [-v_r[0], -v_r[1]]
	intersection(v_r, p2)


main()

def tests():
	print angle((0,1), (1,0))*180/pi
	print rotate_vec([1,0], pi/2)
	print intersection([1.4, -9.6-10.1], [0, 10.1])

#tests()
