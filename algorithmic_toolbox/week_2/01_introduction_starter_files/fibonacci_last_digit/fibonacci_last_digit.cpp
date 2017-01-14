#include <iostream>
#include <assert.h>

int get_fibonacci_last_digit_naive(long long n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int get_fibonacci_last_digit_fast(long long n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous % 10;
        previous = current % 10;
        current = tmp_previous + current % 10;
    }
    return current % 10;
}

// void test_solution() {
//     assert(get_fibonacci_last_digit_fast(3), 2);
//     assert(get_fibonacci_last_digit_fast(3), 2);
//     for (int n = 0; n < 20; ++n)
//         assert(get_fibonacci_last_digit_fast(n) == get_fibonacci_last_digit_naive(n));
// }

int main() {
    int n;
    std::cin >> n;

    // test_solution();
    int c = get_fibonacci_last_digit_fast(n);
    std::cout << c << '\n';
}
