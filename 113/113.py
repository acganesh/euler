def is_bouncy(n):
    n_inc = ''.join(sorted(str(n)))
    n_dec = ''.join(reversed(n_inc))

    n_inc, n_dec = int(n_inc), int(n_dec)
    return n != n_inc and n != n_dec

def is_inc(n):
    n_inc = int(''.join(sorted(str(n))))
    return n == n_inc


def validate():
    assert not is_bouncy(134468)
    assert not is_bouncy(66420)
    assert is_bouncy(155349)

# Manually compute the proportion of bouncy numbers
# below L.
def P(L):
    count = 0
    for n in xrange(1, L):
        if not is_bouncy(n):
            count += 1
    return count


def binomial(n, k):
    nt = 1
    for t in xrange(min(k, n-k)):
        nt *= (n-t) // (t+1)
    return nt

# Number of increasing numbers under L
def I(L):
    return sum(map(is_inc, xrange(1, L)))

# Number of increasing numbers with <=d digits
def I2(d):
    return sum(binomial(10, k) for k in xrange(1, d))

def P2(d):
    return 2*I2(d)

for _ in xrange(130, 160):
    print I(_)
