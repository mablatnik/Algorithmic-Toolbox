import java.util.*;

public class LCM {
  private static long lcm_naive(int a, int b) {
    for (long l = 1; l <= (long) a * b; ++l)
      if (l % a == 0 && l % b == 0)
        return l;

    return (long) a * b;
  }

  private static long euclid_gcd(long a, long b) {
    long divisor = a >= b ? a : b;
    long dividend = a <= b ? a : b;
    while (divisor != 0) {
      long remainder = dividend % divisor;
      dividend = divisor;
      divisor = remainder;
    }
    return dividend;
  }

  private static long lmc_fast(long a, long b) {
    return (a * b) / euclid_gcd(a, b);
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(lmc_fast(a, b));
  }
}
