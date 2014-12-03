   public class ProfileInformation {
   
   	// declare instance variables here
      private String firstName, lastName, location;
      private int age, isOnline;
      private static final int OFFLINE = 0, ONLINE = 1;
      private int status;
      
   	// constructor
      public ProfileInformation(String first, String last) {
         firstName = first;
         lastName = last;
         location = "Not specified";
         age = 0;
         status = OFFLINE;
      	}
      	
   	// methods
      public void setLocation(String locationName) {
         location = locationName;
      }
      public boolean setAge(int ageInYears) {
   		boolean isSet = false;
   		if(ageInYears > 0) {
   			age = ageInYears;
   			isSet = true;
   			}
   		return isSet;
   		}
   	public int getAge() {
   		return age;
   		}
   	public void logOff() {
   		status = OFFLINE;
   		}
   	public void logOn() {
   		status = ONLINE;
   		}
   	
   	// toString method (for String output)
      public String toString() {
         String output = "Name: " + firstName + " "
            + lastName + "\n";
         output += "Location: " + location + "\n";
         output += "Age: " + age + "\n";
         output += "Status: ";
         if(status == OFFLINE) {
      		output += "Offline";
      		}
      	else {
      		output += "Online";
      		}
         return output;
      }
   }