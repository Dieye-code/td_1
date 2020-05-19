package exo11;

import java.util.Scanner;

public class Exo11 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("Entrer la valeur de a");
		int a = sc.nextInt();
		System.out.println("Entrer l'opération");
		String op = sc.next();
		System.out.println("Entrer la valeur de b");
		int b = sc.nextInt();
		
		if(op=="1")
			System.out.println("salut");
		
		switch (op) {
		case "+": {
			
			System.out.println(a+" + "+b+" = "+(a+b));
			break;
		}
		case "-": {
			
			System.out.println(a+" - "+b+" = "+(a-b));
			break;
		}
		case "*": {
					
					System.out.println(a+" X "+b+" = "+a*b);
					break;
				}
		case "/": {
			
			System.out.println(a+" / "+b+" = "+a/b);
			break;
		}

		default:
			System.out.println("Votre choix n'existe pas");
		}
	

	}

}
