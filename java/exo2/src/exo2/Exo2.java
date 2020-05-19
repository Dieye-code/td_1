package exo2;

import java.util.Scanner;

public class Exo2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("entrer le rayon du cercle ");
		
		int r = 0;
		
		do {
			try {
				r = Integer.parseInt(sc.next());
			} catch (Exception e) {
				System.out.println("Le rayon du cercle ne peut pas etre inferieur � 0");
			}
		} while (r <= 0);
		
		int p = (int) ((int) 2*Math.PI*r);
		int s = (int) ((int) Math.PI*Math.pow(r, 2));
		
		System.out.println("Le perimetre du cercle est "+p);
		System.out.println("\nLa surface du cercle est "+s);
		
		sc.close();

	}

}
