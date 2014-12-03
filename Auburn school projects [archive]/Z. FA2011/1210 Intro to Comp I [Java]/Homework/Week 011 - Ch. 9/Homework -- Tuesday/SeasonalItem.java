/**
*Class that represents a variation of Inventory called a Seasonal Item.
*
*@author Albert Wallace--section 003
*@version 11/1/11
*/
public class SeasonalItem extends InventoryItem
{
	private boolean cInSeason = false;
	/**
	*Constant variables.
	*/
	private static final boolean IN_SEASON = true, OUT_OF_SEASON = false;
	/**
	*Constructor of a seasonal item object.
	*
	*@param nameIn name of the item
	*@param priceIn price of the item
	*/
	public SeasonalItem(String nameIn, double priceIn)
	{
		super(nameIn, priceIn);
		setInSeason(IN_SEASON);
	}
	/**
	*Calculates the cost of the item; overrides InventoryItem
	* if an item is *out* of season.
	*
	*@return returns the cost calculated after taxes.
	*/
	public double calculateCost()
	{
		if (isInSeason())
			{ return super.calculateCost(); }
		else
			{
			return super.price * 0.9;
			}
	}
	/**
	*Sets whether the object is in season.
	*
	*@param inSeason Whether the object is in season (true) or not (false)
	*/
	public void setInSeason(boolean inSeason)
	{
		cInSeason = inSeason;
	}
	/**
	*A getter. Checks to see if an item is in season.
	*
	*@return returns true if in season, false otherwise
	*/
	public boolean isInSeason()
	{
		return cInSeason;
	}
	/**
	*The typical toString method.
	*
	*@return returns string with "in stock" if the item is in
	* season; returns normal output of InventoryItem otherwise.
	*/
	public String toString()
	{
		if (isInSeason())
			{
			String output = "";
		
			output += "Name of item: " + name + "\n";
			output += "Price without tax: $" + price + "\n";
			output += "Price with tax: $" + calculateCost() + "\n";
			output += "*In Stock*";
		
			return output;
			}
		else
			{ return super.toString(); }
		
	}
}