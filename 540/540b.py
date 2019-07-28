import numpy as np

def get_trips(a0 = np.array([3, 4, 5])):
    count = 0

    U = np.array([[1, 2, 2], [-2, -1, -2], [2, 2, 3]])
    A = np.array([[1, 2, 2], [2, 1, 2], [2, 2, 3]])
    D = np.array([[-1, -2, -2], [2, 1, 2], [2, 2, 3]])

    a1 = np.dot(a0, U)
    a2 = np.dot(a0, A)
    a3 = np.dot(a0, D)

    return [a1, a2, a3]

def main(limit):
    total = 4
    trips = get_trips()

    while True:
        for a0 in trips:
            trips = get_trips(a0)
            import pdb; pdb.set_trace()
            for t in trips:
                if t[2] < limit:
                    total += 1
        if trips[0][2] >= limit and trips[1][2] >= limit and trips[2][2] >= limit:
            break
    return total

print main(1000)

