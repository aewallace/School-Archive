import java.text.NumberFormat;

/**
*This is used to help organize, say, a grocery store.
* It accepts categories for different items, and helps with calculation
* of total price for each given item.
*
*@author Albert Wallace -- section 003
*@version 9/28/2011
*/
public class GroceryItem {


	//...Names for categories of grocery goods.
		/**
		*General products that have no specific category.
		*/
	public static final String GENERAL = "General";
		/**
		*Represents the produce category of products.
		*/
	public static final String PRODUCE = "Produce";
		/**
		*Represents refrigerated goods.
		*/
	public static final String REFRIGERATED = "Refrigerated";
		/**
		*Represents items that need to remain fully frozen.
		*/
	public static final String FROZEN = "Frozen";
	
	//other variables
	private String nameOfItem, categorySet;
	private double basePrice, priceCalculated;
	
	/**
	*Constructor to store information about each item. Defaults to a
	* predefined item category and generic name if none are provided.
	*
	*@param potentialName the name of each given item
	*
	*@param itemCategory the category into which each item falls.
	*/
	public GroceryItem(String potentialName, String itemCategory)
		{
		setName(potentialName);
		
		if (itemCategory.equals(GENERAL) || itemCategory.equals(PRODUCE)
			|| itemCategory.equals(REFRIGERATED) || itemCategory.equals(FROZEN))
			{
			setCategory(itemCategory);
			}
		else
			{
			setCategory(GENERAL);
			}
		
		setBasePrice(0);
		}
		
		/**
		*Action method. Changes the name of the item in question.
		*
		*@param nameChange the potential new name of the item
		*/
	public void setName(String nameChange) 
		{
		nameChange = nameChange.trim();
		if (nameChange.isEmpty())
			{
			nameOfItem = "(No Name)";
			}
		else
			{
			nameOfItem = nameChange;
			}
		}
		
		/**
		*Query method. Returns the current name of the item in question.
		*
		*@return returns the name of the item in question.
		*/
	public String getName()
		{
		return nameOfItem;
		}
		
		/**
		*Action method. Sets the base price of the item in question, and
		* returns how successful the process was.
		*
		*@param potentialPrice the potential base price for the item
		*
		*@return how successful the process was, defined by integers.
		*/
	public int setBasePrice(double potentialPrice)
		{
		int successInIntegralForm;
		
		if (potentialPrice >= 0 && potentialPrice <= 500)
			{
			basePrice = potentialPrice;
			successInIntegralForm = 1;
			}
		else if (potentialPrice < 0)
			{
			successInIntegralForm = -1;
			}
		else
			{
			successInIntegralForm = 0;
			}
		
		return successInIntegralForm;
		}
		
		/**
		*Query method. Returns the base price set for a given item.
		*
		*@return returns the base price of the item in question.
		*/
	public double getBasePrice()
		{
		return basePrice;
		}
		
		/**
		*Action and calculation method. Used to calculate the
		* total price, including fees and the taxes (applied after
		* fees, where applicable).
		*
		*@param localTaxRate the local tax rate used for applying
		* the appropriate tax percentage
		*
		*@return returns the price, or a "status number" if setting
		* was not successful.
		*/
	public double calculateTotalPrice(double localTaxRate)
		{
		double multiFunctionReturn = 0, scratchWork = 0;
		double produceTaxRateMultiplier = 1.05;
		double frigidFee = 1.5, freezeFee = 3;
		
		if (localTaxRate > 1 || localTaxRate < 0)
			{
			multiFunctionReturn = -1;
			}
		else if (localTaxRate <= 1 && localTaxRate >= 0)
			{
			if (categorySet.equals(GENERAL))
				{
				scratchWork = basePrice * (1 + localTaxRate);
				}
			else if (categorySet.equals(PRODUCE))
				{
				scratchWork = basePrice * (produceTaxRateMultiplier);
				}
			else if (categorySet.equals(REFRIGERATED))
				{
				scratchWork = (basePrice + frigidFee) * (1 + localTaxRate);
				}
			else if (categorySet.equals(FROZEN))
				{
				scratchWork = (basePrice + freezeFee) * (1 + localTaxRate);
				}
			multiFunctionReturn = scratchWork;
			}
		priceCalculated = multiFunctionReturn;
		return multiFunctionReturn;
		}
		
		/**
		*Unrequested, but easily implemented. Returns the total price
		* calculated to prevent code from having to independently
		* calculate, then make use of it. (For GroceryList's summing
		* capabilities).
		*
		*@return returns the calculated price.
		*/
	public double getTotalPrice()
		{
		return priceCalculated;
		}
		
		/**
		*Action method. Sets or changes the product category applied
		* to a given item.
		*
		*@param itemCategory the potential new category being set
		*
		*@return returns how successful the setting process was
		*/
	public boolean setCategory(String itemCategory)
		{
		boolean successQuery;
		
		if (itemCategory.equals(GENERAL) || itemCategory.equals(PRODUCE)
			|| itemCategory.equals(REFRIGERATED) || itemCategory.equals(FROZEN))
			{
			categorySet = itemCategory;
			successQuery = true;
			}
		else
			{
			successQuery = false;
			}
			
		return successQuery;
		}
		
		/**
		*Query method. Used to obtain the current category for
		* a given item.
		*
		*@return returns the category currently set for the item
		*/
	public String getCategory()
		{
		return categorySet;
		}
		
		/**
		*The requisite toString method. Nicely formats output for us.
		*
		*@return returns all the information set about an item that
		* we might want to see.
		*/
	public String toString()
		{
		String output = "";
		NumberFormat currencyFmt = NumberFormat.getCurrencyInstance();
		
		output += "Name of the selected item: " + nameOfItem + ".\n\r";
		output += "Category set for this item: " + categorySet + ".\n\r";
		output += "Original base price for this item: " + basePrice + ".\n\r";
		output += "Calculated total price for this item: "
			+ currencyFmt.format(priceCalculated) + ".";
		
		return output;
		}


}