package exo13;

import java.util.Scanner;

public class Exo13 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer Le Jour");
		int j = sc.nextInt();
		System.out.println("Entrer Le Mois");
		int m = sc.nextInt();
		System.out.println("Entrer L'ann�e");
		int a = sc.nextInt();
		
		if(j>31 && j<1 || m <1 && m>12 || a<0 || a>2020) {
			System.out.println("La date "+j+"/"+m+"/"+a+" n'est pas valide");
		}else {
			switch (m) {
			case 1: {
			}
			case 3: {
			}
			case 5: {
			}
			case 7: {
			}
			case 8: {
			}
			case 10: {
			}
			case 12: {
				System.out.println("La date "+j+"/"+m+"/"+a+" est valide");
				break;
			}
			case 4: {
			}
			case 6: {
			}
			case 9: {
			}
			case 11: {
				if(j>30)
					System.out.println("La date "+j+"/"+m+"/"+a+" n'est pas valide");
				else
					System.out.println("La date "+j+"/"+m+"/"+a+" est valide");
				break;
			}
			case 2: {
				if(a%400==0 || a%4==0 && a%100!=0) {
					if(j>29)
						System.out.println("La date "+j+"/"+m+"/"+a+" n'est pas valide");
					else
						System.out.println("La date "+j+"/"+m+"/"+a+" est valide");
				}else {
					if(j>28)
						System.out.println("La date "+j+"/"+m+"/"+a+" n'est pas valide");
					else
						System.out.println("La date "+j+"/"+m+"/"+a+" est valide");
				}
				break;
			}
			default:
				System.out.println("La date "+j+"/"+m+"/"+a+" n'est pas valide");
			}
		}
		
		
		sc.close();

	}

}
