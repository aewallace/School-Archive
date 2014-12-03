   import java.util.Random;

/**
*This program creates a user ID and password based on input
* when objects are created.
*
*@author	Albert Wallace - section 003
*@version 9/21/2011 (Revised from 9/14 Code)
*/
   public class OnlineUserID {
   
   //instance variables
      private String firstName, lastName;
      private String userIdFull;
      private String pswdCurrent;
      private String emailAddress, websiteAddress, truncatedWebAddress;
      private int onlineStatus, numberOfLogins;
      private String verboseUserStatus;
      private boolean onlineStatBOOL;
   /**
   *Constant variables. Used to set the online status.
   */
      public static final int OFFLINE = 0, ONLINE = 1;
   
   /**
   *Constructor: 
   *Accepts input of the user's first and last name to create an ID.
   *
   *@param first Used to temporarily store the first name of the user
   * before being used to create a relecant user ID.
   * Also necessary to actually run the ID and password constructor.
   *
   *@param last Used to temporarily store the last name of the user
   * before being used to create a relevant user ID.
   * Also necessary to actually run the ID and password constructor.
   */
      public OnlineUserID(String first, String last) {
         int numeralA, numeralB, numeralC;
         String numeralFull;
         String firstF3, lastF3;
         
         Random generateThree = new Random();
      	
         numeralA = generateThree.nextInt(1);
         numeralB = generateThree.nextInt(7);
         numeralB = numeralB + 3;
         numeralC = generateThree.nextInt(10);
         numeralFull = numeralA + "" + numeralB + ""
             + numeralC;
      	
         firstName = first; //set so all other methods can see the name
         lastName = last; //set so all other methods can see the name
      	
      	
      	
      	
         int countF = firstName.length(); //required for if statements
         int countL = lastName.length(); //required for if statements
      	
         if (countF < 4) {
            firstF3 = firstName;
         }
         else {
            firstF3 = first.substring(0, 3); //old method commented out
         	//firstF3 = firstName.charAt(0)
         	//	+ "" + firstName.charAt(1) + "" + firstName.charAt(2);
         }
         if (countL < 4) {
            lastF3 = lastName; 
         }
         else {
            lastF3 = last.substring(0, 3); //old method commented out
         	//lastF3 = lastName.charAt(0) + "" + lastName.charAt(1)
         	//	+ "" + lastName.charAt(2);
         }
         String userIdUncor;	
         userIdUncor = lastF3 + "" + firstF3 + "" + numeralFull;
         userIdFull = userIdUncor.toLowerCase(); //replaces upper with lower
      		
         generateNewPassword(); //called to initialize a new random password
         
         emailAddress = "Not specified";
         websiteAddress = "Not specified";
         onlineStatus = OFFLINE;
         verboseUserStatus = "Offline";
         numberOfLogins = 0;
      	
      }
   
   /**
   *Used to set the user's website URL/website address & email address. If input
   * does not follow guidelines, returns false and neither is set.
   *
   *@param websiteInput accepts potential website address/URL
   *
   *@return returns whether or not the address has been set successfully
   */
      public boolean setWebsite(String websiteInput) {
         boolean hasWWW = false, sRequiredForEmail = true;
         int sCharForWWW = 4, sCharForHTTPWWW = 11;
         String checkWWW = websiteInput.substring(0, sCharForWWW);
         String checkHTTPWWW = websiteInput.substring(0, sCharForHTTPWWW);
         String compareWWW = "www.";
         String compareHTTPWWW = "http://www.";
      
         if (checkHTTPWWW.equals(compareHTTPWWW)) {
            hasWWW = true;
            websiteAddress = websiteInput;
            truncatedWebAddress = websiteInput.substring(sCharForHTTPWWW);
         }
         else if (checkWWW.equals(compareWWW)) {
            hasWWW = true;
            websiteAddress = websiteInput;
            truncatedWebAddress = websiteInput.substring(sCharForWWW);
         }
         else {
            truncatedWebAddress = "Not used; setting website and email failed.";
         }
      	
         if (hasWWW == sRequiredForEmail) {
            emailAddress = userIdFull + "@" + truncatedWebAddress;
         }
         else {
            emailAddress = emailAddress;
         }
         return hasWWW;
      }
   	
   /**
   *Used to obtain the user's website URL/website address. If not previously
   * set, will just return what the constructor put in for the website.
   *
   *@return returns the website address/URL in the user's profile
   */
      public String getWebsite() {
         return websiteAddress;
      }
   	
   /**
   *Used to obtain the user's email address. If not previously
   * set, will just return "Not specified".
   *
   *@return returns the email address stored in the user's profile
   */
      public String getEmail() {
         return emailAddress;
      }
   		
   /**
   *Returns the user ID that has been created, based on prior input,
   * by the constructor.
   *
   *@return returns the user ID that has been created by the constructor.
   */
      public String getId() {
         return userIdFull;
      }
   	
   /**
   *Sets the user's online status, based on one of two predefined statuses,
   * with no return type.
   *
   *@param statusInput passes the user's online status to be set/stored
   */
      public void setStatus(int statusInput) {
         if (statusInput == OnlineUserID.ONLINE) {
            onlineStatus = ONLINE;
            verboseUserStatus = "Online";
            numberOfLogins++;
            onlineStatBOOL = true;
         }
         else {
            onlineStatus = OFFLINE;
            verboseUserStatus = "Offline";
            onlineStatBOOL = false;
         }
      }
   	
   /**
   *Used as a QUERY, not a SETTER. 
   *Returns the online status for the user, based on prior input,
   * after checking for status in a previously set variable.
   *
   *@return returns true if the user is online
   */
      public boolean isOnline() {
         return onlineStatBOOL;
      }
   	
   /**
   *Returns the login count for the user, based on calculation relative
   * to the number of times the status has been set to online.
   *
   *@return returns the number of logins fitting the criteria
   */
      public int getLoginCount() {
         return numberOfLogins; //edit from here
      }
   	
   /**
   *Accepts input for a potential new password. The potential password is
   * then checked for proper length and, if the input is valid,
   * is set as the new password. If the input is not a valid new password,
   * no new password is set and the method returns "false".
   *
   *@param pswdInput The potential password being checked for validity.
   *
   *@return Informs the program whether or not the password
   * has actually been created successfully.
   */
      public boolean setPassword(String pswdInput) {
         boolean pswdSetOK = false;
      
         int indexValue;
         indexValue = pswdInput.length(); //needed to check for length
      
         if (indexValue < 6) { //if the password is too short
            pswdSetOK = false;
         }
         else { //if the password is of the right length
            pswdSetOK = true;
            pswdCurrent = pswdInput;
         }
         return pswdSetOK; //if true, input was fine for use
      }
   	
   /**
   *
   *@return returns the password created to whatever is calling
   * the method.
   */
      public String getPassword() {
         return pswdCurrent;
      }
   	
   /**
   *
   *No parameters or return type.
   */
      public void generateNewPassword() {
         String pswdGenerated;
         int nA, nB, nC, nD, nE, nF;
         Random generateSix = new Random();
      
      		//used to generate each.separate.digit.
         nA = generateSix.nextInt(10);
         nB = generateSix.nextInt(10);
         nC = generateSix.nextInt(10);
         nD = generateSix.nextInt(10);
         nE = generateSix.nextInt(10);
         nF = generateSix.nextInt(10);
      
      		//used to combine each.darn.digit.
         pswdGenerated = nA + "" + nB + "" + nC + "" + nD + "" + nE + "" + nF;
      
         pswdCurrent = pswdGenerated;
      }
   
   /**
   *Used to share properly formatted user information.
   * Typically combined with println to print to the screen.
   *
   *@return Returns the properly formatted information
   */
      public String toString() {
         String output = "Name: " + firstName + " "
            + lastName + "\n";
         output += "User ID: " + userIdFull + "\n";
         output += "Password: " + pswdCurrent + "\n";
         output += "Website: " + websiteAddress + "\n";
         output += "E-mail: " + emailAddress + "\n";
         output += "Status: " + verboseUserStatus + "\n";
         return output;
      }
   	
   	
   	
   	
   }