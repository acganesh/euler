from itertools import permutations
from math import sqrt
import numpy as np


def is_valid(x, w):
    val = sqrt(w**2 + x**2)
    return val == int(val)

# Number of integer partitions of w
# such that x+y = w and 1<=x<=y<=M

def num_partitions(w, M):
    return max(0, w/2 - max(0, w-M-1))


def main(M):
    count = 0
    for z in range(1, M+1):
        for w in range(2, 2*M+1):
            if is_valid(z, w):
                count += num_partitions(w, z)
    return count


print main(1818)
