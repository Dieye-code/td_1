package exo6;

import java.util.Scanner;

public class Exo6 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("Entrer les cordonnés du point A ");
		System.out.println("X");
		int x1 = sc.nextInt();		
		System.out.println("X");
		int y1 = sc.nextInt();	
		System.out.println("Entrer les cordonnés du point B ");
		System.out.println("X");
		int x2 = sc.nextInt();		
		System.out.println("Y");
		int y2 = sc.nextInt();	
		double d = Math.sqrt(Math.pow(x1-x2, 2)+Math.pow(y1-y2, 2));
		System.out.println("La distance entre A("+x1+","+y1+") et B("+x2+","+","+y2+") est "+d);
		sc.close();
	}

}
