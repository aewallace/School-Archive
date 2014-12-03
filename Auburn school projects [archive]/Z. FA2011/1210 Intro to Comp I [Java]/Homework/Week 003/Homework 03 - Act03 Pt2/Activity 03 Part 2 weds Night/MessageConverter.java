import java.util.Scanner;
/**
*This program will read a message input by the user and may convert it
* using 1 of 3 methods, depending on an option chosen by the user.
*
*@author Albert Wallace, Section 003
*@version 9/06/2011.CapsCaseReplaceFixed
*/
public class MessageConverter {
	/**
	*This method will actually handle the message input, the choice of
	* how the message is to be converted (with an option to not convert
	* at all), and will convert the message as the user prefers.
	*
	*@param args User-defined command line arguments (not used).
	*/
	public static void main(String[] args) { 
	
		Scanner userInput = new Scanner(System.in);
		String message;
		int outputType;
		String result = "";
		
		System.out.print("Type in a message and press enter:\r\n\t> ");
		message = userInput.nextLine();
		
		System.out.print("\r\nOutput types:"
			+ "\r\n\t1: As is"
			+ "\r\n\t2: lower case"
			+ "\r\n\t3: UPPER CASE"
			+ "\r\n\t4: v_w_ls r_pl_c_d"
			+ "\r\nEnter your choice: ");
			
		//Next, we get a string; we must convert it to an integer.
		//why we didn't get an integer, I don't know.
		//This will be useful later, I suppose. ...Mmmm, Java.
		outputType = Integer.parseInt(userInput.nextLine()); 

		//our conditional statements to decide 
		// how to slice n dice the message.
		if (outputType == 1) { // as is
			result = message;
			}
		else if (outputType == 2) { //lower case
			result = message.toLowerCase();
			}
		else if (outputType == 3) { //upper case
			result = message.toUpperCase();
			}
		else if (outputType == 4) { //replace vowels
			result = message.replace("a", "_");
			result = result.replace("A", "_");
			result = result.replace("e", "_");
			result = result.replace("E", "_");
			result = result.replace("i", "_");
			result = result.replace("I", "_");
			result = result.replace("o", "_");
			result = result.replace("O", "_");
			result = result.replace("u", "_");
			result = result.replace("U", "_");
			}
		else { //invalid input
			result = "Error: Invalid choice input.";
			}
		
		//print out the result
		System.out.println("\r\n" + result);
	}
}