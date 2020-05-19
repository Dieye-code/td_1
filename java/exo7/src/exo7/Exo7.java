package exo7;

import java.util.Scanner;

public class Exo7 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer le nombre a decomposer");
		int n = sc.nextInt();
		
		int val = n;
		int n20 = val/20;
		val = val%20;
		int n10 = val/10;
		val = val%10;
		int n5 = val/5;
		val = val%5;
		int n2= val/2;
		int n1 = val%2;
		
		System.out.println("Le Nombre "+n+" est composé de");
		System.out.println(n20+" billets de 20 euros");
		System.out.println(n10+" billets de 10 euros");
		System.out.println(n5+" billets de 5 euros");
		System.out.println(n2+" piéces de 2 euros");
		System.out.println(n1+" piéces de 1 euros");
		
		sc.close();

	}

}
