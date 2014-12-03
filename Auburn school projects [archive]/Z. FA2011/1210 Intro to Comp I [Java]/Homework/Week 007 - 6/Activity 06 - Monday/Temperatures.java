import java.util.ArrayList;
import java.util.Scanner;
/**
*Holds a set of integer values representing daily temperatures.
*
*@author Albert Wallace - section 003
*@version 10/03/2011
*/
public class Temperatures
{
	/**
	*Stores our list of temperatures.
	*/
	ArrayList<Integer> temperatures = new ArrayList<Integer>();
	
	/**
	*Constructor.
	*
	*@param temperaturesIn accepts a set of temperatures
	*/
	public Temperatures(ArrayList<Integer> temperaturesIn)
	{
		temperatures = temperaturesIn;
	}
	
	/**
	*Returns the low temperature in the list.
	*
	*@return returns the lowest temperature as an integer
	*/
	public int getLowValue()
	{
		if (temperatures.isEmpty())
			{
			return 0;
			}
		int low = temperatures.get(0);
		for (int i = 1; i < temperatures.size(); i++)
			{
			if (temperatures.get(i) < low)
				{
				low = temperatures.get(i);
				}
			}
		return low;
	}
	
	/**
	*Returns the highest temperature in the list.
	*
	*@return returns the highest temp as an integer
	*/
	public int getHighValue()
	{
		if (temperatures.isEmpty())
			{
			return 0;
			}
		int high = temperatures.get(0);
		for (Integer currentTemp : temperatures)
			{
			if (currentTemp > high)
				{
				high = currentTemp;
				}
			}
		return high;
	}
	
	/**
	*EDIT FROM HERE.
	*
	*@param temp EDIT FROM HERE
	*
	*@return EDIT FROM HERE
	*/
	public int lowerMinimum(int lowIn)
	{
		return lowIn < getLowValue() ? lowIn : getLowValue();
	}
	
	/**
	*EDIT FROM HERE.
	*
	*@param temp EDIT FROM HERE
	*
	*@return EDIT FROM HERE
	*/
	public int higherMaximum(int highIn)
	{
		return highIn > getHighValue() ? highIn : getHighValue();
	}
	
	/**
	*The standard toString method.
	*
	*@return returns formatted output, most likely
	*/
	public String toString()
	{
		return "Low: " + getLowValue() + "\r\nHigh: "
			+ getHighValue();
	}
}