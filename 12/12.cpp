#include <iostream>
#include <math.h>

int getNumDivisors(int N) {
  int num = 0;
  int limit = (int)floor(sqrt(N)) + 1;

  for (int i=1; i<limit; i++) {
    if (N % i == 0) {
      if (i != N/i) {
        num += 2;
      }
      else {
        num++;
      }
    }
  }
  return num;
}

int getTriangleNumber(int N) {
  return N*(N+1) / 2;
}

int divisibleTriNum(int threshold) {
  int current = 1;
  int triNum;
  int numDivisors;

  while (true) {
    triNum = getTriangleNumber(current);
    numDivisors = getNumDivisors(triNum);
    if (numDivisors > threshold) {
      return triNum;
    }
    current++;
  }

  return 0;
}

int main() {
  int result = divisibleTriNum(500);
  std::cout << result;
  return 0;
}
