   /**
	*This program helps a user set up an online dating profile. 
	*The profile is to come replete with a number of user-
	*configurable fields. This class handles the heavy manipulation 
	*backend.
	*
	*@author	Albert Wallace - section 003
	*@version 9/13/2011
	*/
	
	public class ProfileInformation {
   
   	// declare instance variables here
      private String firstName, lastName, location;
      private int age, isOnline;
      private static final int OFFLINE = 0, ONLINE = 1;
      private int status;
		private String phoneNumber;
      
   	/**
		*Accepts input of the user's first and last name, as well
		* as constructs the rest of a given user's profile for later
		* manupulation and access.
		*
		*@param first Used to temporarily store the first name of the user
		* before being permanently stored in variable 'firstName'.
		*
		*@param last Used to temporarily store the last name of the user
		* before being permanently stores in variable 'lastName' for
		* later manipulation/use.
		*/
      public ProfileInformation(String first, String last) {
         firstName = first;
         lastName = last;
         location = "Not specified";
         age = 0;
         status = OFFLINE;
			phoneNumber = "none";
      	}
      	
   	// methods
		/**
		*Called to set the location for a given user depending on input.
		*
		*@param locationName Temporarily used to store the name of the user's
		* current location. The value input will then be stored in the variable
		* 'location' (relatively speaking) for later access.
		*/
      public void setLocation(String locationName) {
         location = locationName;
      	}
		/**
		*Determines if the age information has been set. If so, will return
		* a value of "true" so the program calling the method can access or
		* modify the age as required. If not, will return a value of "false"
		* to instruct the program to print out a corresponding 'Null' string.
		*
		*@param ageInYears Used to accept input of the user's age as
		* temporary storage. It will then be stored in the variable 'age'.
		*
		*@return Informs the item calling this method of whether or not
		* the user has set the age. If not, "false" will be returned and
		* the application calling this method can process information as
		* required.
		*/
      public boolean setAge(int ageInYears) {
   		boolean isSet = false;
   		if (ageInYears > 0) {
   			age = ageInYears;
   			isSet = true;
   			}
   		return isSet;
   		}
		/**
		*This method is called to access the value input as a
		* representation of the user's age, in years.
		*
		*@return Returns the integer value for the user's age.
		*/
   	public int getAge() {
   		return age;
   		}
		/**
		*This method is called to access the user's location after the
		* user has set it by calling the setLocation method.
		*
		*@return Returns the string that represents the user's location.
		*/
		public String getLocation() {
			return location;
			}
   	/**
		*This method is called only to set a user's online status to
		* 'Offline'.
		*
		*No parameters, no return, simply used to set online status.
		*/
		public void logOff() {
   		status = OFFLINE;
   		}
		/**
		*This method is called only to set a user's online status to
		* 'Online'.
		*
		*No parameters, no return, simply used to set online status.
		*/
   	public void logOn() {
   		status = ONLINE;
   		}
		/**
		*Returns the phone number as stores in the variable
		*	'phoneNumber'.
		*
		*@return This method returns the phone number supplied
		* or, if none has been supplied, the equivalent null statement.
		*/
		public String getPhoneNumber() {
			return phoneNumber;
			}
		/**
		*Sets the phone number as part of the information collection
		* process. Stores the number into 'phoneNumber'.
		*
		*@param number This value is used to set the phoneNumber
		* variable.
		*/
		public void setPhoneNumber(String number) {
			phoneNumber = number;
			}
   	
   	// toString method (for String output)
		/**
		*Formats all information properly and arranges said information
		* into a string for proper display or later manipulation.
		*
		*@return Returns the properly formatted output for display
		* or for further use as required.
		*/
      public String toString() {
         String output = "Name: " + firstName + " "
            + lastName + "\n";
         output += "Location: " + location + "\n";
         output += "Age: " + age + "\n";
         output += "Status: ";
         if (status == OFFLINE) {
      		output += "Offline";
      		}
      	else {
      		output += "Online";
      		}
			output += "\nPhone number: " + phoneNumber;
         return output;
      }
   }