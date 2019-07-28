m = var('m')
n = var('n')
i = var('i')
j = var('j')

x1 = var('x1')
x2 = var('x2')
y1 = var('y1')
y2 = var('y2')

assume(m>0)
assume(n>0)
assume(i>0)
assume(j>0)

assume(x1>0)
assume(x2>0)
assume(y1>0)
assume(y2>0)

assume(y2-y1>0)

assume(x2-m>0)
assume(y2-n>0)

i0 = sqrt((x2-x1)**2 + (y2-y1)**2)
i1 = i0.integrate(x1, 0, m)
print 'done with i0!'
print i1
i2 = i1.integrate(y1, 0, n)
print 'done with i1!'
print i2
i3 = i2.integrate(x2, m, m+i)
print 'done with i2!'
print i3
i4 = i3.integrate(y2, n, n+j)
print 'done with i3!'
print i4
