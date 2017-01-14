#include <iostream>
#include <vector>

using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    if (to <= 1)
        return to;

    long long previous = 0;
    long long current = 1;

    for (long long i = 0; i < from - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    long long sum = current;

    for (long long i = 0; i < to - from; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

long long fibonacci_fast(long long n) {
    if (n <= 1)
        return n;

    long long F1, F2, F;
    F1 = 0;
    F2 = 1;
    for (int i = 2; i <= n; i++) {
        F = F1 + F2;
        F1 = F2;
        F2 = F;
    }
    return F;
}

int get_pisano_period_length(long long m) {
    long long F1 = 0, F2 = 1, F = F1 + F2;
    for (int i = 0; i < m * m; i++) {
        F = (F1 + F2) % m;
        F1 = F2;
        F2 = F;
        if (F1 == 0 && F2 == 1) return i + 1;
    }
}

int get_fibonacci_huge_fast(long long n, long long m) {
    long long remainder = n % get_pisano_period_length(m);

    return fibonacci_fast(remainder) % m;
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

long long fibonacci_partial_sum_fast(long long from_, long long to) {
    long long from_last, to_last;
    if (from_ == to) {
        return get_fibonacci_last_digit_fast(from_ % 60);
    } else {
        from_ = from_ % 60;
        to = to % 60;

        from_last = get_fibonacci_huge_fast(from_ + 1, 10) - 1;
        to_last = get_fibonacci_huge_fast(to + 2, 10) - 1;
    }
    return (to_last - from_last) % 10;
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    std::cout << fibonacci_partial_sum_fast(from, to) << '\n';
}
