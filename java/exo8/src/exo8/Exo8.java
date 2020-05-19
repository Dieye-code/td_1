package exo8;

import java.util.Scanner;

public class Exo8 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("entrer la valeur de a");
		int a = sc.nextInt();
		System.out.println("entrer la valeur de b");
		int b = sc.nextInt();
		System.out.println("entrer la valeur de c");
		int c = sc.nextInt();
		double d = Math.pow(b, 2)-4*a*c;
		if(d<0) {
			System.out.println("la solution n'existe pas");
		}else if (d==0) {
			System.out.println("x={"+-b/2*a+"}");
		}else {
			System.out.println("x={"+(-b-Math.sqrt(d))/2*a+","+(-b+Math.sqrt(d))/2*a+"}");
		}
		sc.close();

	}

}
