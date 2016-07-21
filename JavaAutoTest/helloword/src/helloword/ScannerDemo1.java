package helloword;

import java.util.Scanner;

public class ScannerDemo1 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		double sum = 0;
		int m = 0;

		while (scanner.hasNextDouble()) {
			double x = scanner.nextDouble();
			m = m + 1;
			sum = sum + x;

		}
		System.out.println(m + "个数的和为" + sum);
		System.out.println(m + "个数的平均值是" + (sum/m));
	}
}
