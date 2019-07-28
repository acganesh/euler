def u(k, r):
return (900 – 3*k) * pow(r, k – 1)

lo = 1.001
hi = 1.003
eps = 1e-13
tot = -600000000000

while hi – lo > eps:
r = (hi + lo) * .5
s = sum(u(i,r) for i in xrange(1, 5001))
if s < tot:
hi = r
else:
lo = r

print "%.13f" % r