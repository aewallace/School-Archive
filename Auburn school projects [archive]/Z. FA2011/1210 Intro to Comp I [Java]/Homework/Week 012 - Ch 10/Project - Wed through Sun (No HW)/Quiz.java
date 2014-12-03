   import java.util.ArrayList;
	import java.util.Collections;
/**
*Represents a virtual quiz. Used to store quiz questions, which can be
* sorted at a later time using associated methods and classes.
*
*@author Albert Wallace -- section 003
*@version 11/13/2011
*/
   public class Quiz
   {	
   	
		/**
		*Constants used for flipping switches on overloaded methods.
		*/
      public static final int MULTIPLE_CHOICE = 1, SHORT_ANSWER = 2,
			ALL_QUESTIONS = 3, QUESTION_LENGTH = 1, INDEX = 2, CATEGORY = 3;
   
   	/**
		*Other class variables.
		*/
      protected String quizName = "";
      protected ArrayList<QuizQuestion> arrayOfQQ 
			= new ArrayList<QuizQuestion>();
   
		/**
		*Parameterless constructor. Sets the name of the quiz to Today's Quiz.
		*/
      public Quiz()
      {
         setName("Today's Quiz");
      }
   	
		/**
		*Constructor. Sets the name of the quiz to Today's Quiz if
		* the parameter is invalid.
		*
		*@param nameOfQuiz potential name of quiz.
		*/
      public Quiz(String nameOfQuiz)
      {
         boolean nameSetTrue = setName(nameOfQuiz);
         if (nameSetTrue)
         {
            quizName = quizName;
         }
         else
         {
            setName("Today's Quiz");
         }
      }
		
		/**
		*Sets the name of the quiz. Returns true if set was successful.
		*
		*@param nameOfQuiz name of the quiz (potential)
		*@return returns true if the set worked; false if set failed.
		*/
      public boolean setName(String nameOfQuiz)
      {
			try
			{
         	boolean booleanQ = false;
         	int minLength = 1;
      
     	   	nameOfQuiz = nameOfQuiz.trim();
         	if (nameOfQuiz.length() >= minLength)
         	{
           		quizName = nameOfQuiz;
           		booleanQ = true;
         	}
         	else
         	{
          	  booleanQ = false;
         	}
         	return booleanQ; //edit from here
			}
			
			catch(NullPointerException errorDetail)
			{
				return false;
			}
      }
   	
		/**
		*Returns the name of the quiz set by one of the methods above.
		*
		*@return the name of the quiz.
		*/
      public String getName()
      {
         return quizName;
      }
   
		/**
		*Adds a question to the ArrayList of questions, if possible.
		*
		*@param questionIn the question to potentially be added.
		*@return returns true if set was successful; false if failed.
		*/
      public boolean addQuestion(QuizQuestion questionIn)
      {
         int minLength = 0;
			
			if ((questionIn.getQuestionIndex()).isEmpty())
            {
               return false;
            }
				
			if ((questionIn.getQuestionIndex()).length() <= minLength)
            {
               return false;
            }
			
         for (int i = 0; i < arrayOfQQ.size(); i++)
         {
            if (((arrayOfQQ.get(i)).getQuestionText()).equals
					(questionIn.getQuestionText()))
            {
               return false;
            }
            
         }
         arrayOfQQ.add(questionIn);
         return true;
      }
   	
		/**
		*Allows the removal of a question from the ArrayList.
		*
		*@param indexOfQ the index of the questions to potentially be removed
		*@return the number of questions with the corresponding index to have
		* been removed.
		*/
      public int removeQuestion(String indexOfQ) //int = # removed THIS TIME
      {
         int counter = 0;
         for (int i = 0; i < arrayOfQQ.size(); i++)
         {
            if ((arrayOfQQ.get(i)).getQuestionIndex().equals(indexOfQ))
            {
               arrayOfQQ.remove(i);
               counter++;
            }
         }
      
         return counter;
      }
   	
		/**
		*Allows the user to obtain the list of questions as stored in the array
		* UNSORTED.
		*
		*@return the unsorted array of QuizQuestion objects
		*/
      public ArrayList<QuizQuestion> questionList()
      {
         return arrayOfQQ;
      }
   	
		/**
		*Returns a sorted or unsorted array of questions in the quiz list
		* depending on preference.
		*
		*@param questionType the type of question to include in the return.
		*@return the array of questions of the prior type.
		*/
      public ArrayList<QuizQuestion> questionList(int questionType)
      {
         ArrayList<QuizQuestion> arrayToR = new ArrayList<QuizQuestion>();
         if (questionType == MULTIPLE_CHOICE)
         	{
            for (QuizQuestion question : arrayOfQQ)
            {
               if (question instanceof MultipleChoice)
               {
                  arrayToR.add(question);
               }
            }
         	}
         else if (questionType == SHORT_ANSWER)
         	{
            for (QuizQuestion question : arrayOfQQ)
            {
               if (question instanceof ShortAnswer)
               {
                  arrayToR.add(question);
               }
            }
         	}
         else //if (questionType == ALL_QUESTIONS)
         	{
            for (QuizQuestion question : arrayOfQQ)
            	{
            	arrayToR.add(question);
            	}
         	}
         return arrayToR;
      }
		
  		/**
		*Returns a sorted or unsorted array of questions in the quiz list
		* depending on preference.
		*
		*@param questionType the type of question to include in the return.
		*@param sortType how the questions are to be sorted--based on Index,
		* question length, or category.
		*
		*@return the array of questions of the prior type.
		*/
      public ArrayList<QuizQuestion> 
			questionList(int questionType, int sortType)
      {
			ArrayList<QuizQuestion> arrayWorking = new ArrayList<QuizQuestion>();
			//ArrayList<QuizQuestion> arrayToR = new ArrayList<QuizQuestion>();
			
			arrayWorking = questionList(questionType);
			
			if (sortType == CATEGORY)
				{
				Collections.sort(arrayWorking, new CategoryIndexCompare());
				}
			else if (sortType == INDEX)
				{
				Collections.sort(arrayWorking, new IndexCompare());
				}
			else //if (sortType == QUESTION_LENGTH)
				{
				Collections.sort(arrayWorking);
				}
			
			//return arrayToR;
			return arrayWorking;
      }
   }