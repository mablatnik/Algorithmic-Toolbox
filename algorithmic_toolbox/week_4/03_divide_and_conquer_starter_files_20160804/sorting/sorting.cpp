#include <iostream>
#include <vector>
#include <cstdlib>

using std::vector;
using std::swap;

int quick_sort_partition3(vector<int> &a, int l, int r) {
  if (l < r) {
    int pivot = l + rand() % (r - l + 1);
    int pivot_vale = a[pivot];
    int p_l1 = l;
    int p_l2 = l;
    int p_e = r;
    while (p_l2 < p_e) {
      if (a[p_l2] < pivot_vale) {
        swap(a[p_l1], a[p_l2]);
        p_l1++;
        p_l2++;
      } else if (a[p_l2] == pivot_vale) {
        p_l2++;
      } else {
        p_e -= 1;
        swap(a[p_l2], a[p_e]);
      }
    }
    quick_sort_partition3(a, l, p_l1);
    quick_sort_partition3(a, p_e, r);
  }
}

int partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      j++;
      swap(a[i], a[j]);
    }
  }
  swap(a[l], a[j]);
  return j;
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  int m = quick_sort_partition3(a, l, r);

  randomized_quick_sort(a, l, m - 1);
  randomized_quick_sort(a, m + 1, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
}
