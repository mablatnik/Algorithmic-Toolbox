#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::min;

vector<int> optimal_sequence(int n) {
  std::vector<int> sequence;
  while (n >= 1) {
    sequence.push_back(n);
    if (n % 3 == 0) {
      n /= 3;
    } else if (n % 2 == 0) {
      n /= 2;
    } else {
      n = n - 1;
    }
  }
  reverse(sequence.begin(), sequence.end());
  return sequence;
}

vector<int> dynamic_sequence(int n) {
  vector<int> a(n+1);
  vector<int> predecessor(n+1);

  for (int i = 2; i <= n; i++) {
    a[i] = a[i-1] + 1;
    predecessor[i] = i - 1;
    if (i % 3 == 0) {
      if (a[i/3] < a[i]) {
        a[i] = a[i/3] + 1;
        predecessor[i] = i/3;
      }
    }
    if (i % 2 == 0) {
      if (a[i/2] < a[i]) {
        a[i] = a[i/2] + 1;
        predecessor[i] = i/2;
      }
    }
  }

  vector<int> sequence;

  for (int i = n; i !=0; i = predecessor[i]) {
    sequence.push_back(i);
  }
  reverse(sequence.begin(), sequence.end());
  return sequence;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> sequence = dynamic_sequence(n);
  std::cout << sequence.size() - 1 << std::endl;
  for (size_t i = 0; i < sequence.size(); ++i) {
    std::cout << sequence[i] << " ";
  }
}
