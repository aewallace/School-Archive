import java.util.Scanner;

/**
*This program is the "front end" for
* creating a user ID and password. It accepts the necessary input
* and provides feedback to the user during the process.
*
*@author	Albert Wallace - section 003
*@version 9/14/2011
*/

public class GenerateUserID {

	/**
	*The main method will invoke/create/feedback the information
	* during the user ID creation process.
	*
	*@param args Not used with main methods.
	*/
	public static void main(String[] args) {
	
		Scanner newInput = new Scanner(System.in);
		String firstNameTemp, lastNameTemp;
		String changePswd;
		char changePswd2;
		String newPasswordTemp;
		
		System.out.print("Please insert your first name: ");
		firstNameTemp = newInput.nextLine();
		System.out.print("Please insert your last name: ");
		lastNameTemp = newInput.nextLine();
		
		UserID genericPerson;
		genericPerson = new UserID(firstNameTemp, lastNameTemp);
		
		System.out.print("\n\r" + genericPerson);
		
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
			
		
	
	}

}