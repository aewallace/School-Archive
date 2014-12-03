public class InventoryItem
{
	protected double price;
	protected String name;
	private static double taxRate = 0;
	
	public InventoryItem(String nameIn, double priceIn)
	{
		name = nameIn;
		price = priceIn;
	}
	
	public String getName()
	{
		return name;
	}
	
	public double calculateCost()
	{
		return price * (1 + taxRate);
	}
	
	public static void setTaxRate(double taxRateIn)
	{
		taxRate = taxRateIn;
	}
	
	public String toString()
	{
		String output = "";
		
		output += "Name of item: " + name + "\n";
		output += "Price without tax: $" + price + "\n";
		output += "Price with tax: $" + calculateCost();
		
		return output;
	}
}