package exo19;

import java.util.Scanner;

public class Exo19 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int s = 0;
		
		int a;
		do {
			System.out.println("Entrer un prix");
			a = sc.nextInt();
			s += a;
		} while (a !=0);
		
		System.out.println("Le Prix ttotal est "+s);
		
		sc.close();

	}

}
