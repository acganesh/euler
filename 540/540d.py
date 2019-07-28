import math
import sys

class Problem():
    def __init__(self):
        self.mu_values = None
        self.lattice_count_cache = { }
        self.coprime_count_cache = { 1 : 0 }

    def solve(self):
        assert(self.get(10**6) == 159139)
        for n in [3141592653589793]:
            print(n, '=>', self.get(n))

    def get(self, n):
        # Prepare Möbius function for computing coprime lattice count
        self.__init_mu_values(math.floor(math.sqrt(n)))

        # P(n) = sum_{k >= 0} (-1)^k Q(n/2^k) where 
        #     P(n) = {(x,y) in A(n) : x, y coprime and odd parity}, 
        #     Q(n) = {(x,y) in A(n) : x, y coprime}
        total_count = 0
        k = 0
        while 2**k <= n:
            coprime_count = self.__get_coprime_lattice_count(n // 2**k)
            total_count += (-1)**k * coprime_count
            print('get =>', k, coprime_count, total_count)
            k += 1
        return total_count

    def __init_mu_values(self, n):
        prime_sieve = [False for i in range(n + 1)]
        m = math.floor(math.sqrt(n))
        for i in range(2, m + 1):
            if prime_sieve[i] is True:
                continue
            for j in range(i * i, n + 1, i):
                prime_sieve[j] = True

        values = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            if prime_sieve[i] is True:
                continue
            for j in range(i, n + 1, i):
                values[j] *= -1
            for j in range(i**2, n + 1, i**2):
                values[j] = 0
        self.mu_values = values

    def __get_lattice_count(self, n):
        # Let A(n) = #{(x,y) : x^2 + y^2 <= n, 0 < x < y}. 
        if n not in self.lattice_count_cache:
            total_count = 0
            x = 1
            while True:
                max_y = math.floor(math.sqrt(n - x**2))
                min_y = x + 1
                if max_y < min_y:
                    break
                else:
                    total_count += (max_y - min_y + 1)
                x += 1
            self.lattice_count_cache[n] = total_count
        return self.lattice_count_cache[n]

    def __get_coprime_lattice_count(self, n):
        # Q(n) = sum_{d <= sqrt[n]} mu(d) A(floor[n/d^2])
        if n not in self.coprime_count_cache:
            total_count = 0
            m = math.floor(math.sqrt(n))
            for i in range(1, m + 1):
                mu = self.mu_values[i]
                if mu != 0:
                    total_count += mu * self.__get_lattice_count(n // i**2)
            self.coprime_count_cache[n] = total_count
        return self.coprime_count_cache[n]

def main():
    problem = Problem()
    problem.solve()

if __name__ == '__main__':
    sys.exit(main())
