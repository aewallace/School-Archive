   import java.util.Scanner;
	import java.util.ArrayList;
   
   /**
    * Obtains a set of numbers from the user until the user enters
    * 0. Information is then printed about each number that was entered 
    * including whether it was even or odd, and positive or negative.
    *
    * @author Albert Wallace
    * @version 9/26/2011
    */
   public class NumberList {
   
      /**
       * Obtains a set of numbers from the user until the user enters
   	 * 0. Information is then printed about each number that was entered 
    	 * including whether it was even or odd, and positive or negative.
   	 *
       * @param args - Standard commandline arguments
       */
      public static void main(String[] args) {
         /*
      	Delete this multi-line comment.
      	The comments below are meant to help you, but Web-CAT will only
      	grade the output of your program. You must use an ArrayList, however,
      	for full credit. Each comment below does not necessarily correspond
      	to a single line of code.
      	*/
      	
         String input = "";
			int inputIntegerForm = 0;
			int iterationPrint = 0;
         Scanner in = new Scanner(System.in);
         
         // declare and instantiate ArrayList 
			//with generic type <NumberOperations>
			ArrayList<NumberOperations> fancyArray = 
				new ArrayList<NumberOperations>();
              
         // prompt user for set of numbers
			System.out.print("Enter a set of non-zero, non-decimal "
				+ "numbers (enter 0 to end):\n\r");
         // get first line of user input
			input = in.nextLine();
         // while the input is not "0"
			int comparison = 0;
			inputIntegerForm = Integer.parseInt(input);
			
			while (inputIntegerForm != comparison) {
            // add NumberOperations object to array based on user input
            // get new user input
				fancyArray.add(new NumberOperations(inputIntegerForm));
				input = in.nextLine();
				inputIntegerForm = Integer.parseInt(input);
         		}
         
         // iterate through ArrayList from 
			// beginning to end and print each object
			System.out.print("\n\r");
			
			while (iterationPrint < fancyArray.size()) {
				
				System.out.print(fancyArray.get(iterationPrint) + "\n\r");
				iterationPrint++;
				
					}
      }
   }