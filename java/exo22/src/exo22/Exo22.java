package exo22;

import java.util.Scanner;

public class Exo22 {

	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		
		int n;
		System.out.println("entrer la taille du tableau");
		n = sc.nextInt();
		
		
		while(n<10) {
			System.out.println("vous devez saisir un nombre compris entre 10 et 50");
			n = sc.nextInt();
		}
		
		
		int tab [] = new int[n];
		
		for (int i = 0; i < tab.length; i++) {
			System.out.println("entrer la valeur � l'indice "+i);
			int a  = sc.nextInt();
			while(a<1 || a>100) {
				System.out.println("vous devez saisir un nombre compris entre 1 et 100");
				a= sc.nextInt();
			}
		}
		
		int d =0;
		int l =0;
		
		for (int i = 0; i < tab.length-1; i++) {
			
			int k=i;
			int j =i+1;
			while (tab[k]<tab[j]) {
				k++;
				j++;
			}
			if(j-i<l) {
				l= j - i;
				d = i;
				
			}
			i = j;
		}
		
		System.out.println("La sequence la plus longue est \n");
		for (int i = 0; i < tab.length; i++) {
			System.out.println(tab[i]+"- ");
		}
		
		System.out.println("\nelle commence par "+d+" sa longeur est "+l);
		
		
		sc.close();
	}

}
