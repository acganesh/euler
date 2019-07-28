#include <iostream>
#include <vector>

std::vector<int> fibonacci(int limit) {
  int f1 = 0;
  int f2 = 1;
  int next;
  std::vector<int> vals;
  
  while (f1 <= limit) {
    vals.push_back(f1);
    next = f1 + f2;
    f1 = f2;
    f2 = next;
  }

  return vals;
}

int main() {
  std::vector<int> fibs = fibonacci(4000000);
  int sum = 0;
  for (int i : fibs) {
    if (i % 2 == 0) {
      sum += i;
    }
  }

  std::cout << sum;
  return 0;
}
