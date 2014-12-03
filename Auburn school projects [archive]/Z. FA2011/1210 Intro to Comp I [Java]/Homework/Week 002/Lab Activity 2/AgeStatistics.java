import java.util.Scanner;
/**
*This program will calculate statistics based on the age of the user.
*Activity 002
*
*@author Albert Wallace, Section 003
*@version 8/29/2011
*/
public class AgeStatistics {
	/**
	*This method will read in the name and age of the user.
	*It will then feed the determined statistics to the user.
	*
	*@param args User-defined command line arguments.
	*/
	public static void main(String[] args) {
	
	String name;
	int ageInYears;
	int gender = 0; // 1 will represent female
	double maxHeartRate = 0;
	
	Scanner userInput = new Scanner(System.in);
	
	System.out.print("Enter your name: "); //prompts the user to enter name
	name = userInput.nextLine(); //allows user to follow name prompt
	
	System.out.print("Enter your age in years: "); //prompts user to enter age
	ageInYears = userInput.nextInt(); //allows the user to follow age prompt
	
	System.out.print("Enter your gender "
			+ "(1 for female, 0 for male): "); //prompts user to enter gender
	gender = userInput.nextInt();
	
	//convert and display age
	System.out.println("\t Your age in minutes is "
		+ ageInYears * 525600 + " minutes."); //printing age in minutes
		
	System.out.println("\t Your age in centuries is "
		+ (double) ageInYears / 100 + " centuries."); //printing age in centuries
	
	//display max heart rate
	System.out.print("Your max heart rate is ");
	
	if (gender == 1) { //gender would be female; use this calculation
		maxHeartRate = 209 - (0.7 * ageInYears);
		}
	else { //must be a male; use this calculation
		maxHeartRate = 214 - (0.8 * ageInYears);
		}
	System.out.println(maxHeartRate + " beats per minute.");
	}

}