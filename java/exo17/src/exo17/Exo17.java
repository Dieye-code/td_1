package exo17;

import java.util.Scanner;

public class Exo17 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer a");
		int a = sc.nextInt();
		System.out.println("Entrer b");
		int b = sc.nextInt();
		int c = a;
		int d = b;
		while(c!=d) {
			if(c>d)
				c = c-d;
			else
				d = d-c;
		}
		System.out.println("PGCD("+a+","+b+") = "+c);
		
		sc.close();

	}

}
