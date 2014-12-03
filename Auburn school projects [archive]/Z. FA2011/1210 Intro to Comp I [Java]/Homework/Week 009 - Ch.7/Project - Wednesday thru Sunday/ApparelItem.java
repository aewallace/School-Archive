/**
*This class represents items of apparel as would be represented in
* an inventory list. The class keeps up with various information,
* such as cost, sales, and revenue, related to the items.
*
*@author Albert Wallace, section 003
*@version 10/23/2011
*/

public class ApparelItem
{
	/**
	*Variables.
	*/
	private String[] itemInformation;
	private double itemCost = 0, itemSalesRevenue = 0;
	private int idReturn, itemSalesCount = 0;
	private static double multiSalesRevenue = 0;
	private static int multiSalesCount = 0, apparelLength = 0;
	private static ApparelItem[] arrayOfApparel = new ApparelItem[0];
	
	/**
	*Constant variables.
	*/
	private static final int NAMEINDEX = 0, IDINDEX = 1, PRICEINDEX = 2;
	
	/**
	*The constructor method. Sets up the initial object for
	* each apparel item.
	*
	*@param itemInfo The name of the item for which an object is created,
	* the inventory code for the item, &
	* the price for the given item, separated by commas.
	*/
	public ApparelItem(String itemInfo)
		{
		setItemCode(itemInfo);
		apparelLength++;
		ApparelItem[] tempA = new ApparelItem[apparelLength];
		for (int i = 0; i < apparelLength - 1; i++)
			{ tempA[i] = arrayOfApparel[i]; }
		tempA[apparelLength - 1] = this;
		arrayOfApparel = tempA;
		}
	
	/**
	*Allows the user to set the item's name, inventory code,
	* and price.
	*
	*@param itemInfo List of information to be parsed.
	*@return returns true if information can be correctly parsed
	* from the string input parameter.
	*/
	public boolean setItemCode(String itemInfo)
		{
		//if item has 1 comma, and 2nd comma matches index, proceed
		//else, throw a false and move on
		boolean aCommaExists = itemInfo.contains(",");
		if (!aCommaExists)
			{ return false; }
		else
			{
			int indexCommaOne = itemInfo.indexOf(",");
			int indexCommaTwo = itemInfo.lastIndexOf(",");
			
			if (indexCommaOne == indexCommaTwo)
				{ return false; }
			}
		String[] infoArray = new String[3];
		infoArray = itemInfo.split(",");
		
		for (int i = 0; i < 3; i++)
			{
			infoArray[i] = infoArray[i].trim();
			}
		itemInformation = infoArray;
		itemCost = castAsDouble(itemInformation[PRICEINDEX]);
		idReturn = (int) castAsDouble(itemInformation[IDINDEX]);
		return true;
		}
		
	/**
	*Returns the name of the item represented by an ApparelItem object.
	*
	*@return returns the name of the item as a string.
	*/
	public String getName()
		{
		return itemInformation[NAMEINDEX];
		}
	
	/**
	*Converts/casts a virtual double--currently stored as a string--
	* to an actual Java double-type for calculations.
	*
	*@param amountAsString value to be cast as a double.
	*@return value being cast as a double.
	*/
	public double castAsDouble(String amountAsString)
		{
		double castDoubleAmount = Double.parseDouble(amountAsString);
		return castDoubleAmount;
		}
	
	
	/**
	*Returns the inventory ID/code for a given item.
	*
	*@return returns the ID/code of the item as an integer.
	*/
	public int getId()
		{
		return idReturn;
		}
		
	/**
	*Returns the price of a given item.
	*
	*@return returns the price of the item as a double.
	*/
	public double getPrice()
		{
		return itemCost;
		}
	
	/**
	*Makes one sale of the item, and adds the current price to the
	* total sales of that item. (Basically increment the price
	* and the count).
	*/
	public void sellItem()
		{
		itemSalesCount++;
		multiSalesCount++;
		itemSalesRevenue = itemSalesRevenue + itemCost;
		multiSalesRevenue = multiSalesRevenue + itemCost;
		}
	
	/**
	*Returns the total sales (in dollars) for a given item.
	*
	*@return Returns the total sales for a given item.
	*/
	public double totalItemSales()
		{
		return itemSalesRevenue;
		}

	/**
	*Returns the cumulative sales (in dollars) for all items.
	*
	*@return Returns the cumulative sales for all items.
	*/
	public static double allItemSales()
		{
		return multiSalesRevenue;
		}
	
	/**
	*Returns the ApparelItem object (item) that has made the
	* largest amount of money in sales. Returns null if no items
	* exist.
	*
	*@return returns the highest grossing item
	*/
	public static ApparelItem highestSeller()
		{
		ApparelItem churnOut = new ApparelItem("temp, 000000, 0.00");
		if (multiSalesCount == 0)
			{ return null; }
		double tops = 0;
		for (int i = 0; i < arrayOfApparel.length; i++)
			{
			if (arrayOfApparel[i].totalItemSales() > tops)
				{ churnOut = arrayOfApparel[i]; }
			}
			
		return churnOut;
		}
	
	/**
	*The standard toString method. Returns properly formatted
	* output containing info about the apparel item queried.
	*
	*@return returns output relating to the apparel item.
	*/
	public String toString()
		{
		String output = "Output for this apparel item: \n\r";
		output += "Name: " + itemInformation[NAMEINDEX] + "\n\r";
		output += "Item ID: " + itemInformation[IDINDEX] + "\n\r";
		output += "Current cost associated: "
			+ itemInformation[PRICEINDEX] + "\n\r";
		output += "Total revenue from sales of this item: "
			+ itemSalesRevenue + "\n\r";
			
		return output;
		}
}