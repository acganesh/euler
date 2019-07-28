#include <iostream>
#include <map>


int CollatzLength(int start) {
  long current = start;
  int length = 0;

  while (current != 1) {
    if (current % 2 == 0) {
      current /= 2;
    }
    else {
      current = 3*current + 1;
    }
    length++;
  }

  return length + 1;
}


int longestCollatz(int limit) {
  int length;
  int max_length = 0;
  int max_num;

  for (int i = 1; i < limit; i++) {
    length = CollatzLength(i);
    if (length > max_length) {
      max_length = length;
      max_num = i;
    }
  }
  return max_num;
}

int main() {
  int result = longestCollatz(1000000);
  std::cout << result;
}
