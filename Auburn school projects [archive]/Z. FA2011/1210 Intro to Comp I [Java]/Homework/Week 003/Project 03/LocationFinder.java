import java.util.Scanner;
import java.text.DecimalFormat;


/**
*This program will help a user plot a course for a specific destination
* based on current X-Y coordinates and other location-based factors.
*
*@author Albert Wallace, Section 003
*@version 9/07/2011
*/

public class LocationFinder {

	/**
	*This method will accept input for X and Y coordinates for current and 
	* target location, speed of travel, and name of location. It will then
	* calculate & display distance & angle to destination, and ETA. 
	*
	*@param args User-defined command line arguments (not used).
	*/

	public static void main(String[] args) {
		
		Scanner userInput = new Scanner(System.in);
		
		double xHere, xThere, yHere, yThere; //here = current location
		double deltaX, deltaY;
		double speedNotWarp, distanceThere, calETA, degreesFromX;
		String finalDestinationName;
		
		System.out.println("Note: this program works in arbitrary units.");
		
		System.out.println("Please enter current location coordinates:");
		System.out.print("x1 = ");
		xHere = Double.parseDouble(userInput.nextLine());
		System.out.print("y1 = ");
		yHere = Double.parseDouble(userInput.nextLine());
		
		System.out.println("Please enter your target coordinates:");
		System.out.print("x2 = ");
		xThere = Double.parseDouble(userInput.nextLine());
		System.out.print("y2 = ");
		yThere = Double.parseDouble(userInput.nextLine());
		
		
		System.out.print("Please enter your speed: ");
		speedNotWarp = Double.parseDouble(userInput.nextLine());
		
		System.out.print("Now, if you will, please enter a friendly name "
			+ "for your destination (e.g., Home, School, etc.): ");
		finalDestinationName = userInput.nextLine();
		
		//mathematical calculations
		deltaX = (xThere - xHere);
		deltaY = (yThere - yHere);
		degreesFromX = Math.atan2(deltaY, deltaX);
		distanceThere = Math.sqrt((deltaY * deltaY) + (deltaX * deltaX));
		calETA = distanceThere / speedNotWarp;
		
		DecimalFormat myFormatter = new DecimalFormat("0.0##");
		String distanceFormatted = myFormatter.format(distanceThere);
		String degreesFormatted = myFormatter.format(degreesFromX);
		String calETAFormatted = myFormatter.format(calETA);
		
		System.out.println("\n\rDistance to \"" + finalDestinationName
			+ "\": " + distanceFormatted);
		System.out.println("Angle to turn: " + degreesFormatted);
		System.out.println("Estimated time until arrival: " + calETAFormatted);
	
	}
	
}