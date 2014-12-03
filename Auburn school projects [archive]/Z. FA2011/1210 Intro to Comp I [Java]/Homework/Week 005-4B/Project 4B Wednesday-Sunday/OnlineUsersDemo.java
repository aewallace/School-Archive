import java.util.Scanner;

/**
*This program is the "front end" for
* creating a user ID and password. It accepts the necessary input
* and provides feedback to the user during the process.
*
*@author	Albert Wallace - section 003
*@version 9/21/2011 (Revised from 9/14 Code)
*/

public class OnlineUsersDemo {

	/**
	*The main method will invoke/create/feedback the information
	* during the user ID creation process.
	*
	*@param args Not used with main methods.
	*/
	public static void main(String[] args) {
	
		Scanner newInput = new Scanner(System.in);
		String wholeNameP1, firstNameTempP1, lastNameTempP1;
		String wholeNameP2, firstNameTempP2, lastNameTempP2;
		String websiteOne, websiteTwo;
		char onlineStatusOne, onlineStatusTwo;
		String tempOnlineOne, tempOnlineTwo;
		int sONLINEM = 1, sOFFLINEM = 0;
		//String changePswd;
		//char changePswd2;
		//String newPasswordTemp;
		
		System.out.print("Please insert the first & last name for user one: ");
			wholeNameP1 = newInput.nextLine();
			int splitNameP1 = wholeNameP1.lastIndexOf(" ");
		System.out.print("Please insert the website for user one: ");
			websiteOne = newInput.nextLine();
		System.out.print("Is user one online? (y for yes, n for no): ");
			tempOnlineOne = newInput.nextLine();
			onlineStatusOne = tempOnlineOne.charAt(0);
		
		System.out.print("\n\rFor user two, please insert the first "
				+ "& last name: ");
			wholeNameP2 = newInput.nextLine();
			int splitNameP2 = wholeNameP2.lastIndexOf(" ");
		System.out.print("For user two, please insert user's website: ");
			websiteTwo = newInput.nextLine();
		System.out.print("Is user two online? (y for yes, n for no): ");
			tempOnlineTwo = newInput.nextLine();
			onlineStatusTwo = tempOnlineTwo.charAt(0);
			
		//online users demo requires the name to be split after input
		firstNameTempP1 = wholeNameP1.substring(0, splitNameP1);
		lastNameTempP1 = wholeNameP1.substring(splitNameP1 + 1);
		firstNameTempP2 = wholeNameP2.substring(0, splitNameP2);
		lastNameTempP2 = wholeNameP2.substring(splitNameP2 + 1);
		
		//finally constructing profiles for the users
		OnlineUserID genericPerson1, genericPerson2;
		genericPerson1 = new OnlineUserID(firstNameTempP1, lastNameTempP1);
		genericPerson2 = new OnlineUserID(firstNameTempP2, lastNameTempP2);
		
		//we have to set the website & email address for eachJane , if possible
		genericPerson1.setWebsite(websiteOne);
		genericPerson2.setWebsite(websiteTwo);
		
		
		//now to set the online status
		if (onlineStatusOne == 'y') {
			onlineStatusOne = 'Y';
			}
		if (onlineStatusOne == 'Y') {
			genericPerson1.setStatus(sONLINEM);
			}
		else {
			genericPerson1.setStatus(sOFFLINEM);
			}
		
		if (onlineStatusTwo == 'y') {
			onlineStatusTwo = 'Y';
			}
		if (onlineStatusTwo == 'Y') {
			genericPerson2.setStatus(sONLINEM);
			}
		else {
			genericPerson2.setStatus(sOFFLINEM);
			}
		
		//and hopefully printing our information out all nice and neat
		System.out.print("\n\r" 
			+ "*_____*_____*_____*_____*_____*_____*_____*_____*" 
			+ "\n\rUser # 1:\n\r" + genericPerson1);
		System.out.print("\n\r" 
			+ "*_____*_____*_____*_____*_____*_____*_____*_____*" 
			+ "\n\rUser # 2:\n\r" + genericPerson2);
		System.out.print(
			"*_____*_____*_____*_____*_____*_____*_____*_____*");
		
		//old code for setting the password follows
		/**
		System.out.print("\n\rWould you like to change your password? "
			+ "Type Y for yes, or N for no: ");
		changePswd = newInput.nextLine();
		changePswd2 = changePswd.charAt(0);
		if (changePswd2 == 'y') {
			changePswd2 = 'Y';
			}
		if (changePswd2 == 'Y') {
			System.out.print("\n\rPlease enter the proposed new password: ");
			newPasswordTemp = newInput.nextLine();
			if (genericPerson.setPassword(newPasswordTemp)) {
				System.out.print("\n\r" + genericPerson);
				}
			else {
				
				System.out.print("\n\rError: Invalid password."
					+ " Password must be 6 or more digits.");	
				System.out.print("Your information remains"
					+ " unchanged.");
				}
			}
		else {
				System.out.print("No password change requested.");
				}
	*/
		
	
	}

}