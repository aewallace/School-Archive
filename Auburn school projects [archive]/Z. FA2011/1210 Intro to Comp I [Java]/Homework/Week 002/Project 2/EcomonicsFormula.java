   import java.util.Scanner;
/**
*This program will calculate midpoint elasticity using a
* predefined economics formula.
*Project 002
*
*@author Albert Wallace, Section 003
*@version 9/02/2011
*/
   public class EcomonicsFormula { //apparently this name is correct
   /**
   *This method will read in multiple price variables related to economics.
   *It will then calculate 'midpoint elasticity' for the user.
   *
   *@param args User-defined command line arguments (Not used).
   */
      public static void main(String[] args) {
      
         Scanner userInput = new Scanner(System.in);
      	
			//initializing variables used in calculations
         int price1Final, price1Initial, price2Final, price2Initial;
         double percentageElasticity;
         
			//reading in price data for item 1 
         System.out.print("Please input the Final Price for Item 1: ");
         price1Final = userInput.nextInt();
         System.out.print("Please input the Initial Price for Item 1: ");
         price1Initial = userInput.nextInt();
      	
			//reading in price data for item 2
         System.out.print("\nPlease input the Final Price for Item 2: ");
         price2Final = userInput.nextInt();
         System.out.print("Please enter the Initial Price for Item 2: ");
         price2Initial = userInput.nextInt();
      
      	//actual elasticity formula
      	percentageElasticity = ((double) (price1Final - price1Initial)  
               / ((double) (price1Final + price1Initial) / 2)) 
               / (((double) (price2Final - price2Initial)) 
               / (((double) (price2Final + price2Initial) / 2)));    
      	System.out.print("\nThe midpoint elasticity is " 
               + percentageElasticity + " %.");
					
			//end of program. I think.
         
      }
   }