def partitions(n, k, l=1):
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l, n+1):
        for result in partitions(n-i, k-1, i):
            yield (i,)+result


def partitions_prime(n, k, l=1):
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in primes:
        if i > l:
            for result in partitions2(n-i, k-1, i):
                yield (i,)+result
