import java.util.ArrayList;
import java.text.NumberFormat;

/**
*Will produce virtual cable service accounts for
* a residence with one or more owners.
*
*@author Albert Wallace - section 003
*@version 10/05/2011
*/ 

public class CableAccount
{
	/**
	*These are constant variables represent the type
	* of cable service being provided.
	*/
	public static final int NO_CABLE = 0, BASIC = 1, 
		EXTENDED = 3, PREMIUM = 5, PREMIUM_PLUS = 7, BEST_DEAL = 9, 
		MAX_BOXES = 15, MIN_BOXES = 0, MIN_OWNERS = 1;
	/**
	*Static prices/price increases.
	*/
	public static final double COST_OF_FIRST_BOX = 10, C_NC = 0,
		C_BA = 50, C_EX = 20, C_PR = 15.50, C_PRPL = 20.7, C_BD = 30.5;
		
		
	//____Other variables associated with the class.
	private ArrayList<String> listOfOwners = new ArrayList<String>();
	private int serviceType = 0, cableBoxes;
	private double totalPrice, splitPerOwner;
	private String serviceTypeString = "No Cable";
		
	/**
	*The constructor method. Sets up the basic account
	* structure to be edited.
	*
	*@param nameOfFirstOwner name of the first owner assigned
	* to the account (at least one owner must be identified.
	*/
	public CableAccount(String nameOfFirstOwner)
		{
		listOfOwners.add(nameOfFirstOwner);
		costPerOwner();
		}
	
	/**
	*Adds an owner's name to an account (for multiple owners).
	*
	*@param additionalOwner used to add the new name.
	*
	*@return returns true if the additional owner was successfully
	* added to the list of owners for an account.
	*/
	public boolean addOwner(String additionalOwner)
		{
		additionalOwner = additionalOwner.trim();
		if (additionalOwner.isEmpty())
			{
			return false;
			}
		else if (listOfOwners.contains(additionalOwner))
			{
			return false;
			}
		else
			{
			listOfOwners.add(additionalOwner);
			costPerOwner();
			return true;
			}
		}
	
	/**
	*Removes an owner's name from the account, unless that
	* name represents the sole owner left on the account.
	*
	*@param removeOwner name of person/owner to be removed.
	*/
	public void deleteOwner(String removeOwner)
		{
		if (listOfOwners.size() > MIN_OWNERS)
			{
			listOfOwners.remove(removeOwner);
			}
		costPerOwner();
		}
		
	/**
	*Sets the service type provided to a given residence.
	*
	*@param service type of service for the residence
	*/
	public void setService(int service)
		{
		switch (service)
		 	{
         case BEST_DEAL:
         	serviceTypeString = "Best Deal";
				serviceType = service;
				break;
         case PREMIUM_PLUS:
            serviceTypeString = "Premium Plus";
				serviceType = service;
				break;
         case PREMIUM:
            serviceTypeString = "Premium";
				serviceType = service;
				break;
         case EXTENDED:
            serviceTypeString = "Extended";
				serviceType = service;
				break;
         case BASIC:
            serviceTypeString = "Basic";
				serviceType = service;
				break;
			case NO_CABLE:
				serviceTypeString = "No Cable";
				serviceType = service;
				break;
         default:
            serviceTypeString = serviceTypeString;
				serviceType = serviceType;
         }
			costPerOwner();

		}
	
	/**
	*Sets the number of cable boxes assigned to a residence.
	* The number must be between 0 and 15, inclusive.
	*
	*@param numberOfBoxes the number of cable boxes assigned
	*/
	public void setCableBoxes(int numberOfBoxes)
		{
		if (numberOfBoxes <= MAX_BOXES && numberOfBoxes >= MIN_BOXES)
			{
			cableBoxes = numberOfBoxes;
			}
		else
			{
			cableBoxes = cableBoxes;
			}
		costPerOwner();
		}
	
	/**
	*Returns the name of the service type provided to a residence.
	*
	*@return returns the service type provided as a string.
	*/
	public String getServiceString()
		{
		return serviceTypeString;
		}
	/**
	*Returns the total cost of services provided to a residence.
	* This amount is not split across all owners.
	*
	*@return returns the total cost incurred for the whole residence.
	*/
	public double totalCost()
		{
		totalPrice = COST_OF_FIRST_BOX;
		
		switch (serviceType)
		 	{
         case BEST_DEAL:
         	totalPrice += C_BD;
         case PREMIUM_PLUS:
            totalPrice += C_PRPL;
         case PREMIUM:
            totalPrice += C_PR;
         case EXTENDED:
            totalPrice += C_EX;
         case BASIC:
            totalPrice += C_BA;
			case NO_CABLE:
				totalPrice += C_NC;
				break;
         default:
            totalPrice = 0;
         }
		double compoundPercentage = 0.90;
		double compoundPrice = COST_OF_FIRST_BOX;
			
		for (int i = 2; i <= cableBoxes; i++)
			{
			compoundPrice = compoundPrice * compoundPercentage;
			totalPrice = totalPrice + compoundPrice;
			}
		return totalPrice;
		}
	
	/**
	*Returns the cost of the service provided at the residence,
	* divided evenly between the given owners.
	*
	*@return returns the per owner cost of service (so, if 
	* the service cost 99 dollars total, across 3 owners, the method 
	* would return 33 dollars.
	*/
	public double costPerOwner()
		{
		totalCost();
		int divisor = listOfOwners.size();
		splitPerOwner = (totalPrice / divisor);
		return splitPerOwner;
		}
	
	/**
	*The standard toString that returns user names, total cost, and
	* cost per user at a given residence.
	*
	*@return returns a formatted string of the above information.
	*/
	public String toString()
		{
		costPerOwner();
		String output = "Name of owners: \n\r";
		int i = 0;
		while (i < listOfOwners.size())
			{
			output += listOfOwners.get(i) + "\n\r";
			i++;
			}
		output += "\n\rService type: " + serviceTypeString + ".\n\r";
		
		NumberFormat currencyFmt = NumberFormat.getCurrencyInstance();
		String costOut = currencyFmt.format(totalPrice);
		
		output += "\n\rOverall cost of services: " + costOut + ".";
		
		output += "\n\rCost per user in residence: " + splitPerOwner + ".";
		return output;
		}
}