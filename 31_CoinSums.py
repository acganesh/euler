from collections import Counter

def partitions(n, k, v):
    """Return partitions of n into at most k items from v, with
    repetition. v must be a tuple sorted into numerical order. Each
    partition is returned as multiset in the form of a Counter object
    mapping items from v to the number of times they are used in the
    partition.

        >>> partitions(4, 7, (1, 4))
        [Counter({1: 4}), Counter({4: 1})]

    """
    if n == 0:
        # Base case: the empty partition.
        return [Counter()]
    if k == 0 or len(v) == 0 or n < v[0]:
        # No partitions possible here.
        return []
    pp = [p.copy() for p in partitions(n - v[0], k - 1, v)]
    for p in pp:
        p[v[0]] += 1
    return pp + partitions(n, k, v[1:])

def main(num, denominations):
    print len(partitions(num, num, denominations))

num = 200
denominations = (1, 2, 5, 10, 20, 50, 100, 200)

main(num, denominations)

