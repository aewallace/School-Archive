   import org.junit.Assert;
   import org.junit.Test;

  /** Very basic tests for the MultipleChoiceTest. You will need to complete
   *  the test for the equals method at the bottom and add any more test 
	*  methods that you need for full statement coverage (there will need to 
	*  be a test for getCorrectOption for valid and invalid inputs). 
	*  The '50 character rule' for the question display can be tested in the 
	*  interactions pane.
	*
	*  The Web-CAT tests will be much more extensive than the tests below;
	*  make sure that you test your program thoroughly before submitting.
   **/
   public class MultipleChoiceTest {
   
     /** Tests the overloaded constructor. **/
      @Test public void constructor1Test() {
         String index = "4A";
         MultipleChoice mc = new MultipleChoice(index);
         Assert.assertEquals(index, mc.getQuestionIndex());
      }
   
     /** Tests the setQuestionText and getQuestionText method. **/
      @Test public void setQuestionTest() {
         MultipleChoice mc = new MultipleChoice();
         String question = "What is the answer?";
         mc.setQuestionText(question);
         Assert.assertEquals(question, mc.getQuestionText());
      }
      
   	/** Tests the setIndexText return with valid and 
   	 *  invalid inputs. Should return true with a valid input
   	 *  and false with an invalid input.
   	 **/
      @Test public void setQuestionIndexReturnTest() {
         MultipleChoice mc = new MultipleChoice();
         String validInput = "1234567890"; // 10 characters or less
         String invalidInput = "1234567890z"; // more than 10 characters
         Assert.assertTrue(mc.setQuestionIndex(validInput));
         Assert.assertFalse(mc.setQuestionIndex(invalidInput));
      }
      
   	/** Tests the setIndexText functionality with valid and 
   	 *  invalid inputs. 
   	 **/
      @Test public void setQuestionIndexTest() {
         MultipleChoice mc = new MultipleChoice();
         String validInput = "1234567890"; // 10 characters or less
         String invalidInput = "1234567890z"; // more than 10 characters
         mc.setQuestionIndex(validInput);
         Assert.assertEquals(validInput, mc.getQuestionIndex());
         mc.setQuestionIndex(invalidInput); // should not change index
         Assert.assertEquals(validInput, mc.getQuestionIndex());
      }
      
   	/** Makes sure that you can't add more than 53 answers to a multiple
   	 *  choice question.
   	 **/
      @Test public void addAnswerAndDisplayTest() {
         MultipleChoice mc = new MultipleChoice();
         // add 53 answers
         for (int i = 0; i < 53; i++) {
            mc.addAnswer("Answer " + i);
         }
      	// try to add another one - it should not be added!
         mc.addAnswer("Should not be added");
         String display = mc.displayQuestion();
         // make sure a valid answer was added
         Assert.assertTrue(display.contains("Answer 5"));
      	// make sure the invalid answer was not added
         Assert.assertFalse(display.contains("Should not be added"));
      }
      
   	/** A basic test for the question display.
   	 **/
      @Test public void displayTest() {
         MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
         mc2.addAnswer("Run Java Programs");
         mc2.addAnswer("Compile Source Code");
         mc2.addAnswer("All of the above");
         mc2.setCorrectOption('B');
         String display = mc2.displayQuestion();
         Assert.assertTrue(display.contains("What does the"));
         Assert.assertTrue(display.contains("C. All of the above"));
      }
      
   	/** A basic test for the question key.
   	 **/
      @Test public void keyTest() {
         MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
         mc2.addAnswer("Run Java Programs");
         mc2.addAnswer("Compile Source Code");
         mc2.addAnswer("All of the above");
         mc2.setCorrectOption('B');
         String key = mc2.displayKey();
         Assert.assertTrue(key.contains("What does the"));
         Assert.assertTrue(key.contains("B. Compile Source Code"));
         Assert.assertFalse(key.contains("All of the above"));
			Assert.assertEquals('B', mc2.getCorrectOption());
      }
      
   	/** Checks the return of the equals method.
   	 **/
      @Test public void equalsTest() {
		
		MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		MultipleChoice mc3 = new MultipleChoice("4a");
         mc3.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		Assert.assertEquals(true, mc2.equals(mc3));
         
      }
      
   	// add more test methods below
		
		/** Checks the return of the equals method.
   	 **/
		 
		@Test public void equalsTestDos() {
		
		MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		MultipleChoice mc3 = new MultipleChoice("4a");
         mc3.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions. NEVER!");
				
		Assert.assertEquals(false, mc2.equals(mc3));
         
      }
		
		/**Checks the hashCode method.
		*/
		@Test public void testHash()
			{
			MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
			Assert.assertEquals(mc2.hashCode(), mc2.hashCode());
			}
		
		/**Checks the setCorrectOption method for failure.
		*/
		@Test public void testFailOptionSet()
			{
			MultipleChoice mc3e = new MultipleChoice("5e");
			mc3e.setQuestionText("This is not original; does it matter?");
			mc3e.addAnswer("Never!");
         mc3e.addAnswer("Actually, yes; you need a personality.");
         mc3e.addAnswer("Do YOU matter? Didn't think so.");
         mc3e.setCorrectOption('B');
			Assert.assertEquals('B', mc3e.getCorrectOption());
			Assert.assertFalse(mc3e.setCorrectOption('E'));
			}
			
		/**Checks the letter-to-index calculation with 50 answers.
		*/
		@Test public void testHugeAnswerList()
			{
			MultipleChoice mc3e = new MultipleChoice("5e");
			mc3e.setQuestionText("This is not original; does it matter?");
			for (int i = 0; i < 50; i++)
				{
				mc3e.addAnswer("This is supposedly option " + i + "...");
				}
         mc3e.setCorrectOption('d');
			Assert.assertEquals('d', mc3e.getCorrectOption());
			mc3e.setCorrectOption('g');
			Assert.assertEquals('g', mc3e.getCorrectOption());
			Assert.assertFalse(mc3e.setCorrectOption('z'));
			}
			
		/** A test for the question + key combo display. Should make
		**displayKey not include an improper correct option.
   	**/
      @Test public void displayKeyFail() {
         MultipleChoice mc2 = new MultipleChoice("4a");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
         mc2.addAnswer("Run Java Programs");
         mc2.addAnswer("Compile Source Code");
         mc2.addAnswer("All of the above");
			mc2.setCorrectOption('@');
         String display = mc2.displayQuestion();
         Assert.assertTrue(display.contains("What does the"));
         Assert.assertTrue(display.contains("C. All of the above"));
			String dKey = mc2.displayKey();
			Assert.assertFalse(dKey.contains("@"));
      }
   }
