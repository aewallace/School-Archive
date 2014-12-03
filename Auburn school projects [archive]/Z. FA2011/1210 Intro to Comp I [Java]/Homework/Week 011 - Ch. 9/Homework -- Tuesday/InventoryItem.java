/**
*Class that represents an item in a store's inventory.
*
*@author Albert Wallace--section 003
*@version 11/1/11
*/
public class InventoryItem
{
	protected double price;
	protected String name;
	private static double taxRate = 0;
	/**
	*Constructor of an inventory item object.
	*
	*@param nameIn name of the item
	*@param priceIn price of the item
	*/
	public InventoryItem(String nameIn, double priceIn)
	{
		name = nameIn;
		price = priceIn;
	}
	/**
	*Returns the name of the item referenced by the InventoryItem object.
	*
	*@return returns the name of the object
	*/
	public String getName()
	{
		return name;
	}
	/**
	*Calculates the cost of the item based on a given tax rate.
	*
	*@return returns the cost calculated after taxes.
	*/
	public double calculateCost()
	{
		return price * (1 + taxRate);
	}
	/**
	*Sets the tax rate for all items in inventory.
	*
	*@param taxRateIn the tax rate to be set
	*/
	public static void setTaxRate(double taxRateIn)
	{
		taxRate = taxRateIn;
	}
	/**
	*The typical toString method.
	*
	*@return returns string with "in stock" if the item is in
	* season; returns normal output of InventoryItem otherwise.
	*/
	public String toString()
	{
		String output = "";
		
		output += "Name of item: " + name + "\n";
		output += "Price without tax: $" + price + "\n";
		output += "Price with tax: $" + calculateCost();
		
		return output;
	}
}