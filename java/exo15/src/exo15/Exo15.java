package exo15;

import java.util.Scanner;

public class Exo15 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer le nombre");
		int a = sc.nextInt();
		int s = 0;
		
		for (int i = 0; i <= a; i++) {
			s += i;
		}
		
		System.out.println("La Somme des "+a+" Premiers Nombres est "+s);
		sc.close();

	}

}
