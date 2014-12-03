import java.util.ArrayList;
/**
*Runs a VERY small subset of tests on the Quiz class to verify
* interaction with QuizQuestion, IndexCompare, and CategoryIndexCompare
* is somewhat satisfactory. Specifically, this provides visual output
* to check sorting methods. Much room is left for error or poor design.
*
*@author Albert Wallace -- section 003
*@version 11/13/2011
*/
public class TestCases
{
	public static void main(String[] args)
	{
			Quiz tester = new Quiz("Tester");
			
         String index = "4A";
         MultipleChoice mc = new MultipleChoice(index);
         String question9 = "What is the answer?";
         mc.setQuestionText(question9);
			for (int i = 0; i < 53; i++) {
            mc.addAnswer("Answer " + i);
         	}
			tester.addQuestion(mc);
         
			MultipleChoice mc15 = new MultipleChoice();
         String validInput = "1234567890";
         mc15.setQuestionIndex(validInput);
			tester.addQuestion(mc15);
       
 
         MultipleChoice mc2 = new MultipleChoice("2c");
         mc2.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
         mc2.addAnswer("Run Java Programs");
         mc2.addAnswer("Compile Source Code");
         mc2.addAnswer("All of the above");
         mc2.setCorrectOption('B');
			tester.addQuestion(mc2);
			
			MultipleChoice mc2b = new MultipleChoice("2c");
         mc2b.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions. NOT FREEDOM!!!");
         mc2b.addAnswer("Run Java Programs");
         mc2b.addAnswer("Compile Source Code");
         mc2b.addAnswer("All of the above");
         mc2b.setCorrectOption('B');
			tester.addQuestion(mc2b);
			
			MultipleChoice mc2t = new MultipleChoice();
         mc2t.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions. NOT FREEDOM!!!");
         mc2t.addAnswer("Run Java Programs");
         mc2t.addAnswer("Compile Source Code");
         mc2t.addAnswer("All of the above");
         mc2t.setCorrectOption('B');
			tester.addQuestion(mc2t);
      
         MultipleChoice mc3 = new MultipleChoice("3c");
         mc3.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
         mc3.addAnswer("Run Java Programs");
         mc3.addAnswer("Compile Source Code");
         mc3.addAnswer("All of the above");
         mc3.setCorrectOption('B');
			tester.addQuestion(mc3);
      
			MultipleChoice mc3e = new MultipleChoice("3e");
			mc3e.setQuestionText("This is not original; does it matter?");
			mc3e.addAnswer("Never!");
         mc3e.addAnswer("Actually, yes; you need a personality.");
         mc3e.addAnswer("Do YOU matter? Didn't think so.");
         mc3e.setCorrectOption('B');
			
			tester.addQuestion(mc3e);
			
			MultipleChoice mc5e = new MultipleChoice("5e");
			mc3e.setQuestionText("This is not original; does it matter?");
			for (int i = 0; i < 50; i++)
				{
				mc3e.addAnswer("This is supposedly option " + i + "...");
				}
        	tester.addQuestion(mc5e);
			
       	index = "16B";
         ShortAnswer sa = new ShortAnswer(index);
         String question0 = "What is the answer?";
         sa.setQuestionText(question0);
         tester.addQuestion(sa);
     
         ShortAnswer sa1 = new ShortAnswer("ch0_4a");
         sa1.setQuestionText("What is the name of the Java compiler?");
         sa1.addAnswer("javac");
         sa1.addAnswer("javac.exe");
			tester.addQuestion(sa1);
		
		ShortAnswer sa42 = new ShortAnswer("z");
         sa42.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions.");
			tester.addQuestion(sa42);
		
		ShortAnswer sa48e = new ShortAnswer("");
         sa48e.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly. These tests are failing.");
			tester.addQuestion(sa48e);
				
		ShortAnswer sa43 = new ShortAnswer("4a");
         sa43.setQuestionText("What does the Java compiler do? You "
            + "should also be making sure that lines with 50+ "
            + "characters are being written correctly; you can, "
            + "however, test that in interactions. FREEDOM.");
			tester.addQuestion(sa43);
		
			
			ArrayList<QuizQuestion> testersList = new ArrayList<QuizQuestion>();
			ArrayList<QuizQuestion> testersMC = new ArrayList<QuizQuestion>();
			ArrayList<QuizQuestion> testersSA = new ArrayList<QuizQuestion>();
			ArrayList<QuizQuestion> testersSAI = new ArrayList<QuizQuestion>();
			ArrayList<QuizQuestion> testersMCLE = new ArrayList<QuizQuestion>();
			ArrayList<QuizQuestion> testersMCI = new ArrayList<QuizQuestion>();
			
			testersList = tester.questionList();
			testersMC = tester.questionList(Quiz.MULTIPLE_CHOICE);
			testersSA = tester.questionList(Quiz.SHORT_ANSWER);
			testersSAI = tester.questionList(Quiz.SHORT_ANSWER, 2);
			testersMCLE = tester.questionList(1, 1);
			testersMCI = tester.questionList(Quiz.MULTIPLE_CHOICE, 2);
			
			System.out.println("//////////test 1: no sorting, all questions.");
			for (QuizQuestion question : testersList)
				{
				System.out.println(question.displayQHL());
				}
				
			System.out.println("\n\r*********One Done*************");
			System.out.println("///////////test 2: no sorting, multiple choice.");
			for (QuizQuestion question : testersMC)
				{
				System.out.println(question.displayQHL());
				}
			System.out.println("\n\r----------Two Done------------");
			System.out.println("///////////test 3: no sorting, short answer.");
			for (QuizQuestion question : testersSA)
				{
				System.out.println(question.displayQHL());
				}
			System.out.println("\n\r***********Three Done************");
			System.out.println("////////////test 4: sort by index, short answer.");
			for (QuizQuestion question : testersSAI)
				{
				System.out.println(question.displayQHL());
				}
				
			System.out.println("\n\r++++++++++++++Four Done++++++++++++++");
			System.out.println("/////////////test 5: q.length sort, multichoice.");
			for (QuizQuestion question : testersMCLE)
				{
				System.out.println(question.displayQHL());
				}
			System.out.println("\n\rooooooo....Five Done....ooooooo");
			
			System.out.println("////////////test 6: sort by index, multi choice.");
			for (QuizQuestion question : testersMCI)
				{
				System.out.println(question.displayQHL());
				}
				
			System.out.println("\n\r++++++++++++++Six Done++++++++++++++");

			

			
   }
}