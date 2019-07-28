def main(l, k):
    """Works when all coeffcients are 1."""
    S = 0
    T = product(xrange(2), repeat=k)
    for ts in T:
        tmp = []

        for t, c in zip(ts, cs):
            tmp.append(((-1)*c)**t)

        S += (sum(tmp)**l)
        val = (sum(tmp)**l)
        print val
    return S / float(2**(k))


def ref_main(l, k):
    """Simplified sum when all coefficients are 1."""
    S = sum(binomial(k, z)*(2*z-k)**l for z in range(k+1))
    return S / 2**k


def main(l, k):
    """Works when all coeffcients are 1."""
    S = 0
    T = product(xrange(2), repeat=k)
    for ts in T:
        tmp = []

        for t, c in zip(ts, cs):
            tmp.append(((-1)*c)**t)

        S += (sum(tmp)**l)
        val = (sum(tmp)**l)
        print val
    return S / float(2**(k))


def ref_main(l, k):
    """Simplified sum when all coefficients are 1."""
    S = sum(binomial(k, z)*(2*z-k)**l for z in range(k+1))
    return S / 2**k
