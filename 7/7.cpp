#include <iostream>
#include <math.h>

bool isPrime(int N) {
  int limit = (int) ceil(sqrt(N));
  for (int i=2; i<limit+1; i++) {
    if (N % i == 0) {
      return false;
    }
  }
  return true;
}

int nthPrime(int N) {
  int current = 3;
  int count = 1;

  while (true) {
    if (isPrime(current)) {
      count++;
    }

    if (count == N) {
      return current;
    }

    current += 2;
  }
}

int main() {
  int result = nthPrime(10001);
  std::cout << result;
}
