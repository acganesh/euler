import numpy as np
import csv

def same_side(p1,p2,a,b):
    cp1 = np.cross(b-a, p1-a)
    cp2 = np.cross(b-a, p2-a)
    if np.dot(cp1, cp2) >= 0: return True
    else: return False

def point_in_triangle(p, my_list):
	a = my_list[0]
	b = my_list[1]
	c = my_list[2]
	if same_side(p,a,b,c) and same_side(p,b, a,c) and same_side(p,c,a,b): return True
	else: return False

def split_list(chunk_size, my_list):
	return [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]

''' Test cases.
A = np.asarray([-340,495])
B = np.asarray([-153,-910])
C = np.asarray([835,-947])
O = np.asarray([0, 0])

X = np.asarray([-175,41])
Y = np.asarray([-421,-714])
Z = np.asarray([574,-645])

print point_in_triangle(np.asarray([O,A,B,C])
print point_in_triangle(np.asarray([O,X,Y,Z])
'''

f = open('102_data.txt', 'rb')
reader = csv.reader(f)

num_triangles = 0 

for row in reader:
    my_list = np.asarray(row)
    my_list_int = split_list(2, np.asarray([int(element) for element in my_list]))
    #print my_list_int
    origin = np.asarray([0,0])
    if point_in_triangle(origin, my_list_int):
    	num_triangles += 1
f.close()
print num_triangles

