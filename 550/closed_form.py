def main_9(k):
    return (3*(8**k) - 4**k) / 2

def main_11(k):
    return (3*(10**k) - 8**k - 2**k) / 4

def main_13(k):
    return (3*(12**k) - 8**k - 4**k) / 4

# A false conjecture, but close
def main_15(k):
    return (3*(14**k) - 8**k - 4**k) / 4

for k in xrange(2, 10):
    print main_15(k)

# 11
# 122
# 1484
