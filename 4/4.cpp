#include <iostream>
#include <algorithm>
#include <string>


bool isPalindrome(int N) {
  std::string s = std::to_string(N);
  std::string s_rev(s); 
  std::reverse(s_rev.begin(), s_rev.end());
  return (s == s_rev);
}


int largestPalindrome() {
  int prod;
  int largest = 0;
  for (int a = 999; a >= 100; a -= 1) {
    for (int b = 990; b >= 110; b -= 11) {
      prod = a*b;
      if (isPalindrome(prod) and prod > largest) {
        largest = prod;
      }
    }
  }
  return largest;
}


int main() {
  int result = largestPalindrome();
  std::cout << result << '\n';
  return 0;
}
