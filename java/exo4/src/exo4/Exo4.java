package exo4;

import java.util.Scanner;

public class Exo4 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int a = 0;
		int b = 0;

		System.out.println("Enter la valeur de a");
		do {
			try {
				a = Integer.parseInt(sc.next());
			} catch (Exception e) {
				System.out.println("vous devez entrer un entier");
			}
		} while (a == 0);

		System.out.println("Enter la valeur de b");
		do {
			try {
				b = Integer.parseInt(sc.next());
			} catch (Exception e) {
				System.out.println("vous devez entrer un entier");
			}
		} while (b == 0);

		float p = 1;

		for (int i = 0; i < Math.abs(b); i++) {
			p = p * a;
		}

		if (b < 0) {
			p = 1 / p;

		}

		System.out.println(a + " puissance " + b + " est egale � " + p);
		sc.close();
	}

}
