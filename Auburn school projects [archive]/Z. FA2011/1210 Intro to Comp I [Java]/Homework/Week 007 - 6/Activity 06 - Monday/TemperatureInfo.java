import java.util.Scanner;
import java.util.ArrayList;

/**
*Front-end for dealing with the input of temperatures.
*
*@author Albert Wallace - section 003
*@version 10/03/2011
*/
public class TemperatureInfo
{
	/**
	*The main method that handles input and output of information.
	*
	*@param args Not used.
	*/
	public static void main(String[] args)
	{
		ArrayList<Integer> tempList = new ArrayList<Integer>();
		Scanner userInput = new Scanner(System.in);
		
		int tempInput = -1;
		do
			{
			System.out.print("Enter a positive temperature "
				+ "(-1 to stop): ");
			tempInput = userInput.nextInt();
			if (tempInput > -1)
				{
				tempList.add(tempInput);
				}
			}
		while (tempInput > -1);
		Temperatures temps = new Temperatures(tempList);
		System.out.println(temps);
	}
}