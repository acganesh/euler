#include <iostream>
#include <math.h>


bool isPrime(long N) {
  int limit = (int) ceil(sqrt(N));
  for (int i=2; i<limit+1; i++) {
    if (N % i == 0) {
      return false;
    }
  }
  return true;
}

int largestPrimeFactor(long N) {
  int limit = (int) ceil(sqrt(N));
  int largest = 0;
  for (int i=limit; i>1; i--) {
    if (N % i == 0) {
      if (isPrime(i) and i > largest) {
        largest = i;
      }
      if (isPrime(N/i) and N/i > largest) {
        largest = N/i;
      }
    }
  }
  return largest;
}


int main() {
  int result = largestPrimeFactor(600851475143);
  std::cout << result;
}
