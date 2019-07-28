#include <iostream>
int sumOfSquares(int N) {
  return N*(N+1)*(2*N+1) / 6;
}

int squareOfSum(int N) {
  int triSum = N*(N+1)/2;
  return triSum*triSum;
}

int diff(int N) {
  return squareOfSum(N) - sumOfSquares(N);
}

int main() {
  int result = diff(100);
  std::cout << result;
}
