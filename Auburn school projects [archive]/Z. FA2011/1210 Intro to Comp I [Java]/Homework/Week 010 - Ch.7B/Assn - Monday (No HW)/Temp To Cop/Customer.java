public class Customer implements Comparable<Customer>
{
	/**
	*Instance variables.
	*/
	private String custName, custLocation;
	private double custBalance;
	
	/**
	*Constructor method.
	*
	*@param nameIn the name of the customer to be stored.
	*/
	public Customer(String nameIn)
		{
		custName = nameIn;
		custLocation = "";
		custBalance = 0;
		}
	
	/**
	*Changes the location.
	*
	*@param locationIn the location to be assigned
	*/
	public void setLocation(String locationIn)
		{
		custLocation = locationIn;
		}
	
	public void setLocation(String city, String state)
		{
		custLocation = city + ", " + state;
		}
		
	public void changeBalance(double amount)
		{
		custBalance = custBalance+ amount;
		}
	
	public String getLocation()
		{
		return custLocation;
		}
	
	public double getBalance()
		{
		return custBalance;
		}
	
	/**
	*CompareTo method from implementing the Comparable interface.
	*/
	public int compareTo(Customer obj)
		{
		//Customer c = (Customer)obj;
		if (this.custBalance > obj.getBalance())
			{ return 1; }
		else if (this.custBalance < obj.getBalance())
			{ return -1; }
		else	{ return 0; }
		}
	
	public String toString()
		{
		String output = "";
		output += custName + "\n";
		output += custLocation + "\n";
		output += custBalance + "\n";
		
		return output;
		}
	
}