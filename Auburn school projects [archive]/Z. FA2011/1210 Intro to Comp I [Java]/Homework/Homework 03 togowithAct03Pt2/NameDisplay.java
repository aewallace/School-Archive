import java.util.Scanner;
/**
*This program will ask the user for basic data, and reformat the data
* (to be displayed on the screen) in a specific output format/order.
*
*@author Albert Wallace, Section 003
*@version 9/06/2011
*/
public class NameDisplay {
/**
	*This method will ask the user for required data,
	* format the information into a specific order (first name, middle
	* name, last name, birth year), and displays the information.
	*
	*@param args User-defined command line arguments (not used).
	*/
	public static void main(String[] args) {
      
		String name, nickname = "", firstName = "",
			 lastName = "", result = "";
		int age, year, birthyear;
		int indexR;
		
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Enter the current year: ");
		//year = scan.nextInt(); //old method
		year = Integer.parseInt(scan.nextLine()); //new method
      
		System.out.print("Enter your age (the age you will turn "
			+ "this year): ");
		//age = scan.nextInt(); //old method
		age = Integer.parseInt(scan.nextLine()); //new method
		
		birthyear = year - age; //figuring out the user's birth year
      
		System.out.print("Enter your first and last name, "
			+ "separated by a space: ");
		name = scan.nextLine(); //no need to convert from string
		
		System.out.print("Enter your nickname: ");
		nickname = scan.nextLine(); //no need to convert from string
		
		//figuring out how to split the user's name.
		//assuming only 2 words to your name; else, split at the first space
		indexR = name.indexOf(" ");
		//System.out.println("The index is " + indexR); //learning indexOf
		
		firstName = name.substring(0, indexR); //covers the first name
		lastName = name.substring(indexR); //covers the last name
			
		result = firstName + " \"" + nickname + "\"" + lastName 
			+ " " + birthyear;
		
		System.out.println("\r\nYour information is " + result);
		
		//end of program
      }
   }