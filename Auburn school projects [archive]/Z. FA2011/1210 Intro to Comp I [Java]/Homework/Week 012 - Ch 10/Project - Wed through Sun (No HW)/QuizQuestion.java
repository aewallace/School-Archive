import java.util.ArrayList;
import java.util.Scanner;

/**
*Represents the basic, common elements of all questions on a
* given quiz. Specific variations of questions use this as
* a base.
*
*@author Albert Wallace - section 003
*@version 11/2/2011
*/

//Include Comparable because it already has natural ordering
// with compareTo.
public abstract class QuizQuestion implements Comparable<QuizQuestion>
{
	//Class variables.
	protected String questionText, questionIndex, correctAnswer;
	protected ArrayList<String> answers = new ArrayList<String>();
	
	/**
	*Static variables.
	*/
	public static final int MULTIPLE_CHOICE = 1, SHORT_ANSWER = 2,
		ALL_QUESTIONS = 3, QUESTION_LENGTH = 1, INDEX = 2, CATEGORY = 3;
	
	/**
	*Parameterless constructor.
	*/
	public QuizQuestion()
		{
		questionText = "";
		questionIndex = "";
		}
	
	/**
	*Used to set the text displayed as the actual question.
	*
	*@param qText String of text to be displayed.
	*/
	public void setQuestionText(String qText)
		{
		questionText = qText;
		}
	
	/**
	*Used to call up the text that represents the question.
	*
	*@return returns the question text
	*/
	public String getQuestionText()
		{
		return questionText;
		}
		
	/**
	*Used to set the external index that corresponds to a given question.
	*
	*@param indexIn the index to be applied
	*@return returns true if the index has length of 0 to 10 characters
	*/
	public boolean setQuestionIndex(String indexIn)
		{
		indexIn = indexIn.trim();
		if (indexIn.length() >= 0 && indexIn.length() <= 10)
			{
			questionIndex = indexIn;
			return true;
			}
		else
			{
			return false;
			}
		}
	
	/**
	*Used to obtain the external index that corresponds to a given question.
	*
	*@return Returns the index for the question.
	*/
	public String getQuestionIndex()
		{
		return questionIndex;
		}
	
	/**
	*Used to set a potential answers (typically for multi-choice).
	*
	*@param pAns represents the answer choices.
	*@return returns true if the answer is between 1 and 40 chars.
	*/
	public boolean addAnswer(String pAns)
		{
		pAns = pAns.trim();
		if (pAns.length() >= 1 && pAns.length() <= 40)
			{
			answers.add(pAns);
			return true;
			}
		else
			{
			return false;
			}
		}
	
	/**
	*Used to display a properly formatted question, and
	*, if applicable, the answer options (multi-choice only).
	*
	*@return Returns the appropriate text.
	*/
	public String displayQuestion()
		{
		String output = "";
		output = displayQHL();
		return output;
		}
		
	/**
	*Used to display a properly formatted question, for
	* displayQuestion & displayKey.
	*
	*@return Returns formatted text to aid in output.
	*/
	public String displayQHL()
		{
		String output = "";
		int minLength = 0, maxLength = 50, iterator = 0;
		
		if (questionIndex.length() > minLength)
			{
			output += "Question " + questionIndex + ":\n";
			}
		
		Scanner qIn = new Scanner(questionText);
		String temp = "";
		
		while (qIn.hasNext())
			{
			temp = qIn.next();
			
			if (iterator + temp.length() > maxLength)
				{
				iterator = 0;
				output += "\n";
				}
			output += temp + " ";
			iterator = iterator + temp.length() + 1;
			}
		output.trim();
		return output;
		}	
	
	
	/**
	*Abstract method. Will return a string representing the key
	* (aka the actual answer).
	*
	*@return returns the key
	*/
	public abstract String displayKey();
	
	/**
	*The compareTo method from Comparable.
	* Compares questions based on length of the question in characters.
	*
	*@param objectIn the 2nd quizQuestion object to be compared.
	*
	*@return returns an integer depending on the comparison. 
	* If the local question
	* is longer, returns a positive integer. If the foreign question is longer,
	* returns a negative integer. If equal, returns 0.
	*/
	public int compareTo(QuizQuestion objectIn)
		{
		int lengthNotMe = (objectIn.getQuestionText()).length();
		int lengthMe = getQuestionText().length();
		
		if (lengthMe == lengthNotMe)
			{ return 0; }
		if (lengthMe > lengthNotMe)
			{ return 1; }
		else // (lengthMe < lengthNotMe)
			{ return -1; }
		
		}
	
	/**
	*Compares two QuizQuestion objects and compares them.
	*
	*@param qIn the second QuizQuestion object to be compared.
	*@return returns true if both question text and index are the same
	*/
	public boolean equals(QuizQuestion qIn)
		{
		boolean checkIndexTrue
			= this.getQuestionIndex().equals(qIn.getQuestionIndex());
		boolean checkQuestionTrue
			= this.getQuestionText().equals(qIn.getQuestionText());
	
		return (checkQuestionTrue && checkIndexTrue);
		}
	
	/**
	*The hashCode method. Must be researched more.
	*
	*@return returns some unknown integer value.
	*/
	public int hashCode()
		{
		return questionText.hashCode();
		}
	
}