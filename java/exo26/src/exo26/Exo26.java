package exo26;

import java.util.Scanner;

public class Exo26 {

	public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer le nombre à deviner");
		int n = sc.nextInt();
		int x =0;
		System.out.println("Entrer un nombre : ");
		do {
			 x = sc.nextInt();
			 if(x>n)
				 System.out.println("Trop grand");
			 else if (x<n) {
				System.out.println("Trop petit");
			}else {
				System.out.println("Bravo !!!!");
			}
		} while (x!=n);
		
		sc.close();

	}

}
