def digital_sum(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)


# Val and exp set limits on iteration to generate perfect powers
def main(val, exp, ind):
    pows = {}
    seq = []
    for m in range(1, val):
        for k in range(2, exp):
            result = m**k
            if result >= 10:
                if digital_sum(result) == m:
                    seq.append(result)
                pows[result] = (m, k)
    return sorted(seq)[ind]

print main(100, 50, 29)
