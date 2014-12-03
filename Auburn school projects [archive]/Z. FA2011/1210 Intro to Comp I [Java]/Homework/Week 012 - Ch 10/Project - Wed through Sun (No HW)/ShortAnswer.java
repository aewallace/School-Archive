/**
*Represents questions that are multiple choice.
*
*@author Albert Wallace -- section 003
*@version 11/2/2011
*/
public class ShortAnswer extends QuizQuestion
{	
		
	/**
	*Parameterless constructor for a short answer question.
	*/
	public ShortAnswer()
		{
		}
		
	/**
	*Constructor for a short answer question, with an index assigned
	* from initialization.
	*
	*@param index the index to be assigned.
	*/
	public ShortAnswer(String index)
		{
		setQuestionIndex(index);
		}
	
	
	/**_____________________________________________________________*
	*Used to set a potential answers (typically for multi-choice).
	*
	*@param pAns represents the answer choices.
	*@return returns true if the answer is between 1 and 40 chars.
	____________
	public boolean addAnswer(String pAns)
		{
		boolean isSet = false;
		
		isSet = super.addanswer(pAns);
		
		return isSet;
		}
	__________________________________________________________________*
	*/
	
	/**______________________________________________________________*
	*Used to display a properly formatted question, and
	*, if applicable, the answer options (multi-choice only).
	*
	*@return Returns the appropriate text.
	______
	public String displayQuestion()
		{
		return null;
		}
	__________________________________________________________________*
	*/
		
	/**
	*Abstract method. Will return a string representing the key
	* (aka the actual answer).
	*
	*@return returns the key
	*/
	public String displayKey()
		{
		String output = "";
		
		output += displayQuestion();
		
		for (String answer : answers)
			{
			output += "\n" + answer;
			}
		
		return output;
		}
}