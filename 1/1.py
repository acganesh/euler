'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import tensorflow as tf


def main(N):
    lim1, lim2, lim3 = (N-1)/3, (N-1)/5, (N-1)/15
    total = (3*lim1*(lim1+1) + 5*lim2*(lim2+1) - 15*lim3*(lim3+1))/2
    return total

print main(1000)
