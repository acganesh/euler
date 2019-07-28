#include <iostream>
#include <math.h>

bool isPrime(int N) {
  if (N == 2) {
    return true;
  }
  int limit = (int) ceil(sqrt(N));
  for (int i=2; i<limit+1; i++) {
    if (N % i == 0) {
      return false;
    }
  }
  return true;
}

long primeSum(long limit) {
  int current = 2;
  long sum = 0;

  while (current < limit) {
    if (isPrime(current)) {
      sum += current;
    }
    current++;
  }

  return sum;
}

int main() {
  long result = primeSum(2000000);
  std::cout << result;
  return 0;
}
