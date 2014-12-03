public class CustomerDriver
{
	public static void main(String[] args)
		{
		Customer cstmr1 = new Customer("John");
		cstmr1.changeBalance(30);
		cstmr1.setLocation("Boston, MA");
		System.out.println(cstmr1);
		
		Customer cstmr2 = new Customer("JoAnn");
		cstmr2.changeBalance(30);
		cstmr2.setLocation("Auburn, AL");
		System.out.println(cstmr2 + "\r\n");
		
		if (cstmr1.compareTo(cstmr2) == 1)
			{ System.out.println("Higher balance: " + cstmr1); }
		else if (cstmr1.compareTo(cstmr2) == -1)
			{ System.out.println("Higher balance: " + cstmr2); }
		else
			{ System.out.println("Balances are equal."); }
		}
}