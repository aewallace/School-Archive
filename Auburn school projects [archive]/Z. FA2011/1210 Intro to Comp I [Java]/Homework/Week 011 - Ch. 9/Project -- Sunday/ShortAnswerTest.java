   import org.junit.Assert;
   import org.junit.Test;

  /** Very basic tests for the MultipleChoiceTest. If you included 
   *  all common code in QuizQuestion, then you should only have to 
	*  add 1-2 tests to achieve statement-level coverage.
   **/
   public class ShortAnswerTest {
   
     /** Tests the overloaded constructor. **/
      @Test public void constructor1Test() {
         String index = "4B";
         ShortAnswer sa = new ShortAnswer(index);
         Assert.assertEquals(index, sa.getQuestionIndex());
      }
   
     /** Tests the setQuestionText and getQuestionText method. **/
      @Test public void setQuestionTest() {
         ShortAnswer sa = new ShortAnswer();
         String question = "What is the answer?";
         sa.setQuestionText(question);
         Assert.assertEquals(question, sa.getQuestionText());
      }
     
   	/** Tests the addAnswer return with valid and 
   	 *  invalid inputs. Should return true with a valid input
   	 *  and false with an invalid input.
   	 **/
      @Test public void addAnswerReturnTest() {
         ShortAnswer sa = new ShortAnswer();
         // the following line is 40 characters long (valid input)
         String validInput = "123456789_123456789_123456789_123456789_";
         // the following line is 41 characters long (invalid input)
         String invalidInput = "100000000_200000000_300000000_400000000_5"; 
         Assert.assertTrue(sa.addAnswer(validInput));
         Assert.assertFalse(sa.addAnswer(invalidInput));
      }
      
   	/** A basic test for the question display.
   	 **/
      @Test public void displayTest() {
         ShortAnswer sa1 = new ShortAnswer();
         sa1.setQuestionText("What is the name of the Java compiler?");
         sa1.addAnswer("javac");
         sa1.addAnswer("javac.exe");
         String display = sa1.displayQuestion();
         Assert.assertTrue(display.contains("What is the name"));
         Assert.assertFalse(display.contains("javac"));
      }
      
   	/** A basic test for the question key.
   	 **/
      @Test public void keyTest() {
         ShortAnswer sa1 = new ShortAnswer();
         sa1.setQuestionText("What is the name of the Java compiler?");
         sa1.addAnswer("javac");
         sa1.addAnswer("javac.exe");
         String key = sa1.displayKey();
         Assert.assertTrue(key.contains("What is the name"));
         Assert.assertTrue(key.contains("javac"));
      
      }
      
   	// add more test methods below
		
		
		/** Checks the return of the equals method.
   	 **/
      @Test public void equalsTest() {
		
		ShortAnswer sa42 = new ShortAnswer("4a");
         sa42.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		ShortAnswer sa43 = new ShortAnswer("4a");
         sa43.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		Assert.assertEquals(true, sa42.equals(sa43));
         
      }
		
		/** Checks the return of the equals method for falseness.
   	 **/
      @Test public void equalsTestDos() {
		
		ShortAnswer sa42 = new ShortAnswer("4a");
         sa42.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
		ShortAnswer sa43 = new ShortAnswer("4a");
         sa43.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions. NEVER!");
				
		Assert.assertEquals(false, sa42.equals(sa43));
         
      }
		
		/**Checks the hashCode method.
		*/
		@Test public void testHash()
			{
			ShortAnswer sa44 = new ShortAnswer("4a");
         sa44.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
				
			Assert.assertEquals(sa44.hashCode(), sa44.hashCode());
			}

   }
