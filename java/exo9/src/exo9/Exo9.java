package exo9;

import java.util.Scanner;

public class Exo9 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer l'heure de depart");
		System.out.println("H:");
		int hd = sc.nextInt();
		System.out.println("Mn:");
		int md = sc.nextInt();
		System.out.println("Entrer l'heure d'arriv�");
		System.out.println("H:");
		int ha = sc.nextInt();
		System.out.println("Mn:");
		int ma = sc.nextInt();
		
		int h1 = hd*60+md;
		int h2 = ha*60+ma;
		
		int d = h2-h1;
		
		System.out.println("La dur�e de vol est : "+d/60+"H"+d%60+"Mn");
		
		sc.close();

	}

}
