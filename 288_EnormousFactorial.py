def S(n):
    length = 1
    S_vals = [290797]
    while length < n:
        S_vals.append((S_vals[-1]**2) % 50515093)
        length += 1
    return S_vals[-1]


def T(p, n):
    return S(n) % p
