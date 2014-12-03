/**
*
*
*@author Albert Wallace -- section 003
*@version 10/10/2011
*/

public class Scores
{	
	int[] numbers;

	/**
	*Constructor method to store the array of numbers.
	*
	*@param numbersIn accepts numbers for processing as an int array.
	*/
	public Scores(int[] numbersIn)
		{
		numbers = numbersIn;
		}
	
	/**
	*Determines all the even numbers in the list, if any.
	*
	*@return returns the int array of evens, if any were found.
	*/
	public int[] findEvens()
		{
		int numberEvens = 0;
		
		for (int i = 0; i < numbers.length; i++)
			{
			if (numbers[i] % 2 == 0)
				{
				numberEvens++;
				}
			}
		int[] evens = new int[numberEvens];
		int count = 0;
		for (int i = 0; i < numbers.length; i++)
			{
			if (numbers[i] % 2 == 0)
				{
				evens[count] = numbers[i];
				count++;
				}
			}
		return evens;
		}
	
	/**
	*Determines all the odd numbers in the list, if any.
	*
	*@return returns the int array of odds, if any were found.
	*/
	public int[] findOdds()
		{
		int numberOdds = 0;
		
		for (int i = 0; i < numbers.length; i++)
			{
			if (numbers[i] % 2 != 0)
				{
				numberOdds++;
				}
			}
		int[] odds = new int[numberOdds];
		int count = 0;
		for (int i = 0; i < numbers.length; i++)
			{
			if (numbers[i] % 2 != 0)
				{
				odds[count] = numbers[i];
				count++;
				}
			}
		return odds;
		}
		
	/**
	*Calculates the average of all numbers/scores listed.
	*
	*@return returns a double representing the average.
	*/
	public double calculateAverage()
		{
		int sum = 0;
		
		for (int i = 0; i < numbers.length; i++)
			{
			sum += numbers[i];
			}
		
		return (double)sum / numbers.length;
		}
	
	/**
	*Puts all numbers listed in a list, in reverse order AS LISTED.
	*
	*@return returns the string of the numbers in reverse listing.
	*/
	public String toReverseString()
		{
		String output = "";
		
		for (int i = numbers.length - 1; i >= 0; i--)
			{
			output += numbers[i] + " ";
			}
		
		return output;
		}
		
	/**
	*The toString method. Puts all info in a neatly formatted output.
	*
	*@return returns the formatted output.
	*/
	public String toString()
		{
		String output = "";
		
		for (int i = 0; i < numbers.length; i++)
			{
			output += numbers[i] + "\t";
			}
		
		return output;
		}

}