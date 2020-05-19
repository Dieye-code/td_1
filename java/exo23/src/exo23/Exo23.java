package exo23;

public class Exo23 {

	public static void main(String[] args) {
		
		System.out.println("Dans 12 mois nous aurons "+nbl(12));
		int x = 1;
		while (nbl(x)<=1000000000) {
			x++;
		}
		System.out.println("c'est dans "+x+" mois qu'on aura depassé les un millard de lapins");

	}
	
	public static int nbl(int n) {
		if(n<=1)
			return 2;
		else
			return nbl(n-1)+nbl(n-2);
	}

}
