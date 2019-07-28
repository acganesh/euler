'''
It is easily proved that no equilateral triangle exists with integral 
length sides and integral area. 
However, the almost equilateral triangle 5-5-6 
has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle 
for which two sides are equal and the third differs by no more 
than one unit.

Find the sum of the perimeters of all almost equilateral triangles 
with integral side lengths and area and whose perimeters 
do not exceed one billion (1,000,000,000).
'''
from fractions import gcd

def pythag_triples(limit, per_limit):
    total = 0
    for n in range(1, limit):
        for m in range(n+1, limit):
            if gcd(m, n) == 1 and (m-n)%2 == 1:
                a = (m**2-n**2)
                b = (2*m*n)
                c = (m**2+n**2)
                if abs(c - 2*a) == 1:
                    print c, c, 2*a
                    per = c+c+2*a
                if abs(c - 2*b) == 1:
                    print c, c, 2*b
                    per = c+c+2*b


                if abs(c - 2*a) == 1 and (c-2*b) == 1:
                    print 'both?!'
                total += per
                if per > per_limit:
                    print 'TOTAL: ', total
                    import time; time.sleep(20)

pythag_triples(30000, 1000000000)

'''
def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield m
        m = np.dot(m, uad)
'''
