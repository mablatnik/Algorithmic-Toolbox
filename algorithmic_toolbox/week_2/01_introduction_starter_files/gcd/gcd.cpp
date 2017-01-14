#include <iostream>

using std::cin;
using std::cout;

int gcd_naive(int a, int b) {
    int current_gcd = 1;
    for (int d = 2; d <= a && d <= b; d++) {
        if (a % d == 0 && b % d == 0) {
            if (d > current_gcd) {
                current_gcd = d;
            }
        }
    }
    return current_gcd;
}

int euclid_gcd(int a, int b) {
    int divisor = a >= b ? a : b;
    int dividend = a <= b ? a : b;
    while (divisor != 0) {
        int remainder = dividend % divisor;
        dividend = divisor;
        divisor = remainder;
    }
    return dividend;
}

int main() {
    int a, b;
    // while (true) {
    //   a = rand() % 1000 + 2;
    //   b = rand() % 1000 + 2;
    //   cout << "Numbers: " << a << ' ' << b << "\n";

    //   long res1 = gcd_naive(a, b);
    //   long res2 = euclid_gcd(a, b);
    //   if (res1 != res2) {
    //     cout << "Wrong answer: " << res1 << ' ' << res2 << "\n";
    //     break;
    //   }
    //   else {
    //     cout << "OK\n";
    //   }
    // }
    std::cin >> a >> b;
    std::cout << euclid_gcd(a, b) << std::endl;
    return 0;
}
