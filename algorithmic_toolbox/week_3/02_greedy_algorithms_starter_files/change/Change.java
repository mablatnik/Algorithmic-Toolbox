import java.util.Scanner;

public class Change {
	private static int getChange(int m) {
		int[] coins = { 10, 5, 1 };
		int count = 0;

		for (int i = 0; m > 0; i++) {
			count += m / coins[i];
			m %= coins[i];
		}
		return count;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int m = scanner.nextInt();
		System.out.println(getChange(m));

	}
}