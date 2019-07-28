#include <iostream>
#include <math.h>

bool isPerfectSquare(int candidate) {
  double root = sqrt(candidate);
  return root == floor(root);
}


int getPythagProduct(int sum) {
  int csq;

  double c;
  for (int a = 1; a <= sum; a++) {
    for (int b = 1; b <= sum - a; b++) {
      csq = a*a+b*b;
      c = sqrt(csq);
      if (c == floor(c)) { // Check if perfect square

      }
      if (isPerfectSquare(csq) and a+b+c == 1000) {
        return a*b*c;
      } 
    }
  }

  return 0;
}

int main() {
  int result = getPythagProduct(1000);
  std::cout << result;
}
