package helloword;

import java.util.Scanner;

public class ScannerDemo {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int i = 0;
		float f = 0.0f;

		System.out.print("����������");
		if (scanner.hasNextInt()) {
			i = scanner.nextInt();
			System.out.print("�������ݣ�" + i);
		} else {
			System.out.println("����Ĳ���������");
		}
		System.out.print("\n");
		System.out.print("����С����");
		if (scanner.hasNextFloat()) {
			f = scanner.nextFloat();
			System.out.println("С�����ݣ�" + f);
		} else {
			System.out.println("����Ĳ���С����");
		}

	}

}
