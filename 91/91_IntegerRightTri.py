from math import floor, log

# Tried to derive a closed form solution --
# this doesn't quite work
def main(N=50):
    total = 3*(N**2)
    total += (2**floor(log(N, 2)))
    return total

if __name__ == '__main__':
    print main(1)
    print main(2)
    print main(3)
    print main(4)
    print main(9)
    print main()
