package exo14;

import java.util.Scanner;

public class Exo14 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("Entrer Le Jour");
		int j = sc.nextInt();
		System.out.println("Entrer Le Mois");
		int m = sc.nextInt();
		System.out.println("Entrer L'ann�e");
		int a = sc.nextInt();
		if (a % 400 == 0 || a % 4 == 0 && a % 100 != 0)
			System.out.println("L'Ann�e " + a + " est bissextile");
		else
			System.out.println("L'Ann�e " + a + " n'est pas bissextile");
		sc.close();

	}

}
