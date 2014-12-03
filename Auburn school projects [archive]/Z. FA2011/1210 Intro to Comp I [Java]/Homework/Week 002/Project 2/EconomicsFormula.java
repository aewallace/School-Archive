import java.util.Scanner;
/**
*This program will calculate midpoint elasticity using a
* predefined economics formula.
*Project 002
*
*@author Albert Wallace, Section 003
*@version 8/31/2011
*/
public class EconomicsFormula {
	/**
	*This method will read in multiple price variables related to economics.
	*It will then calculate 'midpoint elasticity' for the user.
	*
	*@param args User-defined command line arguments (Not used).
	*/
	public static void main(String[] args) {
	
		Scanner userInput = new Scanner(System.in); //creates a new scanner object
	
		double price1Final, price1Initial, price2Final, price2Initial;
		double percentageElasticity;
		double numer1, numer2, denom1, denom2; //used in elasticity formula
		
		System.out.print("Please input the Final Price for Item 1: ");
		price1Final = userInput.nextDouble();
		//System.out.print("You entered " + price1Final); //check; comment out
		System.out.print("Please input the Initial Price for Item 1: ");
		price1Initial = userInput.nextDouble();
		//System.out.print("You entered " + price1Initial); //check; comment out
		
		System.out.print("\nPlease input the Final Price for Item 2: ");
		price2Final = userInput.nextDouble();
		//System.out.print("You entered " + price2Final); //check; comment out
		System.out.print("Please enter the Initial Price for Item 2: ");
		price2Initial = userInput.nextDouble();
		//System.out.print("You entered " + price2Initial); //check; comment out 
		
		//midpoint elasticity formula
		numer1 = (price1Final - price1Initial); //numerator 1
		numer2 = (price2Final - price2Initial); //numerator 2; cannot equal 0
		denom1 = ((price1Final + price1Initial) / 2); //denominator 1
		denom2 = ((price2Final + price2Initial) / 2); //denominator 2
		
		percentageElasticity = (numer1 / denom1) / (numer2 / denom2);
		//System.out.print("Num1: " + numer1 + " Num 2: " + numer2); //check; comment out
		//System.out.print(" Denom1: " + denom1 + " Denom2: " + denom2); //check; comment out
		if (numer2 == 0) {
			System.out.print("\nThe midpoint elasticity cannot be determined.");
			}
		else {
			System.out.print("\nThe midpoint elasticity is " 
			+ percentageElasticity + "%.");
			}
	}
}