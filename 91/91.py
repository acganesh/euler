from math import sqrt

# Square distance between P1 and P2
def sdist(P1, P2):
    return sum( (x1 - x2)**2 for x1, x2 in zip(P1, P2))

# Check if OP_1P_2 forms a valid right triangle
def is_right(P1, P2):
    O = 0, 0
    d1 = sdist(O, P1)
    d2 = sdist(O, P2)
    d3 = sdist(P1, P2)

    # Ensure that OP_1P_2 forms a triangle
    if d1 + d2 < d3 or d2 + d3 < d1 or d3 + d1 < d2:
        return False

    # Ensure that the points are distinct
    if P1 == P2 or P1 == O or P2 == O:
        return False

    ds = sorted([d1, d2, d3])
    return ds[0] + ds[1] == ds[2]

def main(n):
    total = 0
    for x1 in range(0, n+1):
        for y1 in range(0, n+1):
            for x2 in range(0, n+1):
                for y2 in range(0, n+1):
                    P1 = x1, y1
                    P2 = x2, y2

                    if is_right(P1, P2):
                        total += 1

    return total / 2

print main(50)
