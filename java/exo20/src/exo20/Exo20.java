package exo20;

import java.util.Scanner;

public class Exo20 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int tab[] = new int [10];
		int g = 0;
		int p = 0;
		for (int i = 0; i < tab.length; i++) {
			System.out.println("Entrer le nombre � l'indice "+(i+1));
			tab[i] = sc.nextInt();
			if(tab[i]>g) {
				g = tab[i];
				p = i+1;
			}
		}
		
		System.out.println("Le nombre le plus grand est "+g+" sa position est "+p);
		
		sc.close();
		

	}

}
