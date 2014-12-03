/**
    *Obtains a number from the user, which can then be further 
	 * analyzed by other available methods in a number of
	 * ways.
    *
    * @author Albert Wallace
    * @version 9/26/2011
    */

public class NumberOperations {
	
	/**
	*The main or master number to be used for all calculations.
	*/
	private int number;
	
	/**
	*Serves as the constructor for each object of this type of class.
	*
	*@param numberIn used to set the master number for all later
	* calculations that may be done.
	*/
	public NumberOperations(int numberIn) {
		
		number = numberIn;
		
		}
	
	/**
	*Used as a query to obtain the value of the number input, which
	* is the master number used as the reference value for all
	* calculations in the class.
	*
	*@return used to return the value of the master number used for
	* reference in all calculations
	*/
	public int getValue() {
		
		return number;
		
		}
	
	/**
	*Determines the odd numbers, if any, that may exist below
	* a predefined upper limit number.
	*
	*@return returns odd numbers under a given upper limit
	*/	
	public String oddsUnder() {
		
		String output = "";
		
		int i = 0; //our counter to control the while loop
		while (i < number) {
			if (i % 2 != 0) {
				output += i + "\t";
				}
			i++;
			}
		
		return output;
		
		}
	
	/**
	*Determines all powers of two that happen to be under a given
	* number.
	*
	*@return returns any powers of two under the number specified
	* upon initial construction.
	*/	
	public String powersTwoUnder() {
		
		String output = "";
		int powers = 1;
		
		while (powers < number) {
			output += powers + "\t"; //concatenate to output
			powers = powers * 2; //gen next power of 2
			}
		
		return output;
		
		}
	
	/**
	*Used to compare a secondary number (freshly input) to the
	* primary/master number input upon construction of the object.
	*
	*@param compareNumber the number to be compared to the master
	* number "number"
	*
	*@return returns predefined values depending on boolean statements
	*/	
	public int isGreater(int compareNumber) {
		
		if (number > compareNumber) {
			return 1;
			}
		else if (number < compareNumber) {
			return -1;
			}
		else {
			return 0;
			}
		
		}
		
	/**
	*The typical toString method. Used to return (this far) only the
	* master number used with all the comparisons/calculations.
	*
	*@return returns only the master number
	*/
	public String toString() {
		
		String output = number + "";
		
		if (number == 0) {
			output = output;
			}
		
		else if (number < 0) {
			output += ": Number is negative";
			}
		else {
			output += ": Number is positive";
			}
			
		if (number != 0) {
			
			if (number % 2 != 0) {
				output += " odd.";
				}
			else if (number % 2 == 0) {
				output += " even.";
				}
			}
			
		
		return output;	
		
		} //end of toString
		
		
}

