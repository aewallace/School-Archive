/**
*Represents questions that are multiple choice.
*
*@author Albert Wallace -- section 003
*@version 11/2/2011
*/
public class MultipleChoice extends QuizQuestion
{
	
	/**
	*Parameterless constructor for a multiple choice question.
	*/
	public MultipleChoice()
		{
		}
		
	/**
	*MultipleChoice variables.
	*/
	private char correctAnswerLetter;
	protected int totalAnswers;
	protected static final int ABIG = 65, 
		ZBIG = 90, ASMALL = 97, ZSMALL = 122;
	
		
	/**
	*Constructor for a multiple choice question, with an index assigned
	* from initialization.
	*
	*@param index the index to be assigned.
	*/
	public MultipleChoice(String index)
		{
		super.setQuestionIndex(index);
		}
		
	/**
	*Used to set a potential answers (typically for multi-choice).
	*
	*@param pAns represents the answer choices.
	*@return returns true if the answer is between 1 and 40 chars.
	*/
	public boolean addAnswer(String pAns)
		{
		boolean isSet = false;
		int maxSize = 52;
		
		if (answers.size() >= maxSize)
			{ isSet = false; }
		else
			{
			isSet = super.addAnswer(pAns);
			totalAnswers++;
			}
		
		return isSet;	
		}
	
	
	/**
	*Used to display a properly formatted question, and
	*, if applicable, the answer options (multi-choice only).
	*
	*@return Returns the appropriate text.
	*/
	public String displayQuestion()
		{
		int iterator = 65;
		String output = "";
		output += super.displayQuestion();
		
		
		for (String answer : answers)
			{
			output += "\n" + (char) iterator + ". " + answer;
			if (iterator == 90)
				{
				iterator = 97;
				}
			else
				{	iterator++; }
			}
		
		
		return output;
		}
	/**
	*Converts alphabet characters to integer indices.
	*
	*@param letterIn the letter being input.
	*@return the integer index (from 1 to 52)
	*/
	public int charToInt(char letterIn)
		{
		int shiftFromCaps = 64, shiftFromLC = 96 - 26, indexR;
		int i = (int) letterIn;
		if (i <= ZBIG && i >= ABIG)
			{
			indexR = (char) (i - shiftFromCaps);
			}
		else // if (letterIn <= ZSMALL && letterIn >= ASMALL)
			{
			indexR = (char) (i - shiftFromLC);
			}
		return indexR;
		}
		
	/**
	*Will return a string representing the question &
	* the actual answer.
	*
	*@return returns the key
	*/
	public String displayKey()
		{
		String output = "";
		output += super.displayQuestion();
		int i = (int) correctAnswerLetter;
		
		if (i >= ABIG)
			{
			output += "\n" + correctAnswerLetter + ". "
				+ answers.get(charToInt(correctAnswerLetter) - 1);
			}
		
		return output; //edit from here
		}
	
	/**
	*Used to set the correct answer/option.
	*
	*@param selection the answer to be set as "correct"
	*@return returns true if it can be set
	*/
	public boolean setCorrectOption(char selection)
		{
		boolean isSet = false;
		int selectionAsInt = charToInt(selection);
		if (selectionAsInt <= totalAnswers)
			{
			correctAnswerLetter = selection;
			isSet = true;
			}
		return isSet;
		}
	
	/**
	*Returns the correct option for a given question.
	*
	*@return returns the correct option as a character
	*/
	public char getCorrectOption()
		{
		return correctAnswerLetter;
		}
}