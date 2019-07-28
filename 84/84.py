import re
from random import shuffle, randint
from collections import Counter

squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

n_squares = len(squares)

CC = ['GO', 'JAIL']
CH = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'R+', 'R+', 'U+', '3-']

special_CH = set(['R+', 'U+', '3-'])

# If applicable, get the new square that results from
# the current position

def get_square(pos):
    if re.search('^CC.$', pos):
        val = randint(1, 16)
        if 1<=val<=2:
            pos = draw_CC()
        ind = squares.index(pos)
    if re.search('^CH.$', pos):
        val = randint(1, 16)
        if 1<=val<=10:
            card = draw_CH()
            if card in special_CH:
                ind, pos = get_CH_pos(card, pos)
            else:
                pos = card
                ind = squares.index(pos)
        ind = squares.index(pos)
    if pos == 'G2J':
        pos = 'JAIL'
        ind = squares.index(pos)
    else:
        ind = squares.index(pos)
    return ind, pos

def draw_CC():
    card = CC.pop(0)
    CC.append(card)
    return card

def draw_CH():
    card = CH.pop(0)
    CH.append(card)
    return card

def get_CH_pos(card, pos):
    if card == 'R+':
        # Compute the position of the next railroad
        # Current idx
        ind = squares.index(pos)
        sqs = squares[ind:] + squares[:ind]

        ind2, pos2 = next((ind+i, p) for (i, p) in enumerate(sqs) if re.search('^R.$', p))
        return ind, pos

    if card == 'U+':
        ind = squares.index(pos)
        sqs = squares[ind:] + squares[:ind]

        ind2, pos2 = next((ind+i, p) for (i, p) in enumerate(sqs) if re.search('^U.$', p))
        return ind2, pos2

    if card == '3-':
        ind = squares.index(pos)
        ind2 = ind-3
        return ind2, squares[ind2]

def is_double():
    return True

def roll(N, ind):
    ind2 = (ind+N) % n_squares
    pos = squares[ind2]
    new_pos = get_square(pos)
    return new_pos


def is_double(d1, d2):
    return d1 == d2

def simulate(n_iter):
    ind = 0

    c = Counter()

    double_count = 0
    for _ in xrange(n_iter):

        d1 = randint(1, 4)
        d2 = randint(1, 4)

        if is_double(d1, d2):
            double_count += 1
        else:
            double_count = 0

        N = d1 + d2

        if double_count == 3:
            pos = 'JAIL'
            ind = squares.index(pos)
        else:
            ind, pos = roll(N, ind)

        c[pos] += 1

    return c


shuffle(CC)
shuffle(CH)

n_iter = 10**6
C = simulate(n_iter)



print C['JAIL']/float(n_iter)
print C['E3']/float(n_iter)
print C['GO']/float(n_iter)

sorted_C = sorted(C.items(), key = lambda x: x[1], reverse=True)

vals = sorted_C[0:3]
for v in vals:
    print squares.index(v[0])

import pdb; pdb.set_trace()
