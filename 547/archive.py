def S3():
    T1 = 2*E(2,1) - E(1,1)
    T2 = (E(2,2) - E(1,1)/4. - T1/2.)*4.
    #print T2
    S3 = (81./64)*(E(3,3) - 8./81*T1 - 8./81*T2 - 1./81*E(1,1))

    return S3


def sim_T1(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(1, 2)
        y2 = random.uniform(0, 1)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)

def sim_T2(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(1, 2)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        y2 = random.uniform(1, 2)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)


# Simulates D(2,1,1,1)
def sim_D2(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(1, 3)
        x2 = random.uniform(1, 2)
        y2 = random.uniform(0, 1)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)


# Simulates D(2,2,1,1)
def sim_D21(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(1, 3)
        y2 = random.uniform(1, 3)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)

def D2(m, n, i, j):
    val = (m+j)*i*T2(m, j, i) ** 2 + (n+i)*m*T2(n, i, m) ** 2
    val /= (m+n)*(i+j)
    val = sqrt(val)
    return val

def sim_T1(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(1, 2)
        y2 = random.uniform(0, 1)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)

def sim_T2(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(1, 2)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        y2 = random.uniform(1, 2)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)


# Simulates D(2,1,1,1)
def sim_D2(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(1, 3)
        x2 = random.uniform(1, 2)
        y2 = random.uniform(0, 1)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)


# Simulates D(2,2,1,1)
def sim_D21(num_iter):
    dists = []

    for _ in xrange(num_iter):
        x1 = random.uniform(0, 1)
        y1 = random.uniform(0, 1)
        x2 = random.uniform(1, 3)
        y2 = random.uniform(1, 3)

        P1 = (x1, y1)
        P2 = (x2, y2)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)

def D2(m, n, i, j):
    val = (m+j)*i*T2(m, j, i) ** 2 + (n+i)*m*T2(n, i, m) ** 2
    val /= (m+n)*(i+j)
    val = sqrt(val)
    return val


def S4():
    val = E(4, 4)
    A = 4 * 4


def test_S4_1():
    val = E(4,4)

    val -= 2./256*T2(1,1,1)
    val -= 2./256*T2(1,1,1)
    val -= 4./256*T2(1,2,1)
    val -= 4./256*T2(1,2,1)
    val -= 2./256*D(1,1,1,1)
    val -= 4./256*D(1,1,2,1)
    val -= 8./256*D(1,1,2,2)
    val -= 4./256*D(1,1,1,2)

    val -= 1./256*E(1,1)

    val *= 256./225
    return val

def sim_S4_1(num_iter):

    def get_point(N):
        x = random.uniform(0, N)
        y = random.uniform(0, N)
        return (x, y)

    def is_valid(P):
        x = P[0]; y = P[1]
        if 1<=x<=2 and 1<=y<=2:
            return False
        return True

    dists = []

    for _ in xrange(num_iter):

        P1 = get_point(4)
        P2 = get_point(4)

        while not(is_valid(P1)):
            P1 = get_point(4)

        while not(is_valid(P2)):
            P2 = get_point(4)

        dists.append(dist(P1, P2))

    return sum(dists)/float(num_iter)
    #return sum(dists)/float(len(dists))


def S(s):
    e = 0
    A = s * s

    iters = 0
    for x1 in range(1, s - 1):
        for y1 in range(1, s - 1):
            for x2 in range(x1 + 1, s):
                for y2 in range(y1 + 1, s):
                    e += E(s, s)
                    m = x2 - x1
                    n = y2 - y1

                    print m, n
                    #Left and Right adjacent
                    e -= 2 * T2(m, x1, n) * (m * n) / A * (x1 * n) / A #T(m, n, x1)
                    e -= 2 * T2(m, s - x2, n) * (m * n) / A * ((s - x2) * n) / A
                    #Top and Bottom adjacent
                    e -= 2 * T2(n, y1, m) * (n * m) / A * (y1 * m) / A
                    e -= 2 * T2(n, s - y2, m) * (n * m) / A * ((s - y2) * m) / A
                    #Top Left
                    e -= 2 * D(m, n, x1, y1) * (m * n) / A * (x1 * y1) / A
                    #Top Right
                    e -= 2 * D(m, n, s - x2, y1) * (m * n) / A * ((s - x2) * y1) / A
                    #Bottom Left
                    e -= 2 * D(m, n, x1, s - y2) * (m * n) / A * (x1 * (s - y2)) / A
                    #Bottom Right
                    e -= 2 * D(m, n, s - x2, s - y2) * (m * n) / A * ((s - x2) * (s - y2)) / A
                    #Center
                    e -= E(m, n) * (m * n) / A * (m * n) / A
                    #iters += 1
    #print iters
    return e * (A ** 2) / ((A - 1) ** 2)


def S2(s):
    e = 0
    A = s * s

    num = 0

    for x1 in range(1, s - 1):
        for y1 in range(1, s - 1):
            for x2 in range(x1 + 1, s):
                for y2 in range(y1 + 1, s):
                    c = 0
                    e0 = E(s, s)
                    m = x2 - x1
                    n = y2 - y1

                    m = float(m)
                    n = float(n)

                    #Left and Right adjacent
                    c += 2 * (m * n) * (x1 * n)
                    e0 -= 2 * T2(m, x1, n) * (m * n) / A * (x1 * n) / A
                    c += 2 * (m * n) * ((s - x2) * n)
                    e0 -= 2 * T2(m, s - x2, n) * (m * n) / A * ((s - x2) * n) / A
                    #Top and Bottom adjacent
                    c += 2 * (n * m) * (y1 * m)
                    e0 -= 2 * T2(n, y1, m) * (n * m) / A * (y1 * m) / A
                    c += 2 * (n * m) * ((s - y2) * m)
                    e0 -= 2 * T2(n, s - y2, m) * (n * m) / A * ((s - y2) * m) / A
                    #Top Left
                    c += 2 * (m * n) * (x1 * y1)
                    e0 -= 2 * D(m, n, x1, y1) * (m * n) / A * (x1 * y1) / A
                    #Top Right
                    c += 2 * (m * n) * ((s - x2) * y1)
                    e0 -= 2 * D(m, n, s - x2, y1) * (m * n) / A * ((s - x2) * y1) / A
                    #Bottom Left
                    c += 2 * (m * n) * (x1 * (s - y2))
                    e0 -= 2 * D(m, n, x1, s - y2) * (m * n) / A * (x1 * (s - y2)) / A
                    #Bottom Right
                    c += 2 * (m * n) * ((s - x2) * (s - y2))
                    e0 -= 2 * D(m, n, s - x2, s - y2) * (m * n) / A * ((s - x2) * (s - y2)) / A
                    #Center
                    c += (m * n) * (m * n)
                    e0 -= E(m, n) * (m * n) / A * (m * n) / A

                    c = float(c)
                    e0 = float(e0)
                    e += e0 * A ** 2 / (A ** 2 - c)
                    #print c
                    num += 1
    print num
    return float(e)


def S_sim2(s, num_iter):
    e = 0
    A = s * s

    num = 0
    for x1 in range(1, s - 1):
        for y1 in range(1, s - 1):
            for x2 in range(x1 + 1, s):
                for y2 in range(y1 + 1, s):
                    c = 0
                    e0 = E(s, s)
                    m = x2 - x1
                    n = y2 - y1

                    m = float(m)
                    n = float(n)

                    #Left and Right adjacent
                    c += 2 * (m * n) * (x1 * n)
                    e0 -= 2 * T2(m, x1, n) * (m * n) / A * (x1 * n) / A
                    c += 2 * (m * n) * ((s - x2) * n)
                    e0 -= 2 * T2(m, s - x2, n) * (m * n) / A * ((s - x2) * n) / A
                    #Top and Bottom adjacent
                    c += 2 * (n * m) * (y1 * m)
                    e0 -= 2 * T2(n, y1, m) * (n * m) / A * (y1 * m) / A
                    c += 2 * (n * m) * ((s - y2) * m)
                    e0 -= 2 * T2(n, s - y2, m) * (n * m) / A * ((s - y2) * m) / A
                    #Top Left
                    c += 2 * (m * n) * (x1 * y1)
                    e0 -= 2 * Ds(m, n, x1, y1, num_iter) * (m * n) / A * (x1 * y1) / A
                    #Top Right
                    c += 2 * (m * n) * ((s - x2) * y1)
                    e0 -= 2 * Ds(m, n, s - x2, y1, num_iter) * (m * n) / A * ((s - x2) * y1) / A
                    #Bottom Left
                    c += 2 * (m * n) * (x1 * (s - y2))
                    e0 -= 2 * Ds(m, n, x1, s - y2, num_iter) * (m * n) / A * (x1 * (s - y2)) / A
                    #Bottom Right
                    c += 2 * (m * n) * ((s - x2) * (s - y2))
                    e0 -= 2 * Ds(m, n, s - x2, s - y2, num_iter) * (m * n) / A * ((s - x2) * (s - y2)) / A
                    #Center
                    c += (m * n) * (m * n)
                    e0 -= E(m, n) * (m * n) / A * (m * n) / A

                    c = float(c)
                    e0 = float(e0)
                    e += e0 * A ** 2 / (A ** 2 - c)

                    num += 1
                    if num % 1000 == 0: print num, time.time() - start
    return float(e)

def integrand(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


# Tried to numerically integrate with law of cosines - didn't really work.
def D_int(a, b):
    E = Dc(a,b)
    print 'E', E
    def fn(x):
        return sqrt(E**2 + E**2 - 2*E*E*cos(x))

    vals = np.arange(0, np.pi, 0.0001)
    fvals = map(fn, vals)

    int_val = 1./(2)*np.trapz(fvals, vals)

    return int_val


#@profile
def S_sim(s, num_iter):
    e = 0
    A = s * s

    num = 0
    for x1 in range(1, s - 1):
        for y1 in range(1, s - 1):
            for x2 in range(x1 + 1, s):
                for y2 in range(y1 + 1, s):
                    c = 0
                    e0 = E(s, s)
                    m = x2 - x1
                    n = y2 - y1

                    m = float(m)
                    n = float(n)

                    #Left and Right adjacent
                    c += 2 * (m * n) * (x1 * n)
                    e0 -= 2 * T2(m, x1, n) * (m * n) / A * (x1 * n) / A
                    c += 2 * (m * n) * ((s - x2) * n)
                    e0 -= 2 * T2(m, s - x2, n) * (m * n) / A * ((s - x2) * n) / A
                    #Top and Bottom adjacent
                    c += 2 * (n * m) * (y1 * m)
                    e0 -= 2 * T2(n, y1, m) * (n * m) / A * (y1 * m) / A
                    c += 2 * (n * m) * ((s - y2) * m)
                    e0 -= 2 * T2(n, s - y2, m) * (n * m) / A * ((s - y2) * m) / A
                    #Top Left
                    c += 2 * (m * n) * (x1 * y1)
                    e0 -= 2 * D_main(m, n, x1, y1, num_iter) * (m * n) / A * (x1 * y1) / A
                    #Top Right
                    c += 2 * (m * n) * ((s - x2) * y1)
                    e0 -= 2 * D_main(m, n, s - x2, y1, num_iter) * (m * n) / A * ((s - x2) * y1) / A
                    #Bottom Left
                    c += 2 * (m * n) * (x1 * (s - y2))
                    e0 -= 2 * D_main(m, n, x1, s - y2, num_iter) * (m * n) / A * (x1 * (s - y2)) / A
                    #Bottom Right
                    c += 2 * (m * n) * ((s - x2) * (s - y2))
                    e0 -= 2 * D_main(m, n, s - x2, s - y2, num_iter) * (m * n) / A * ((s - x2) * (s - y2)) / A
                    #Center
                    c += (m * n) * (m * n)
                    e0 -= E(m, n) * (m * n) / A * (m * n) / A

                    c = float(c)
                    e0 = float(e0)
                    e += e0 * A ** 2 / (A ** 2 - c)

                    num += 1
                    #if num % 1 == 0: print num, time.time() - start
    return float(e)
