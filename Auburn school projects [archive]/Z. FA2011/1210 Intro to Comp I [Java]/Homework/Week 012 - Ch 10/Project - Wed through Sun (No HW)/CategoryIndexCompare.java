import java.util.Comparator;

/**
*Used to compare quiz questions based on a predefined ordering.
*
*@author Albert Wallace -- section 003
*@version 11/13/2011
*/
public class CategoryIndexCompare implements Comparator<QuizQuestion>
{
/**
*Method that compares two objects. Used for sorting functions.
*
*@param obj1 the first object of comparison
*@param obj2 the second object of comparison
*
*@return returns a positive, negative, or 0, depending on required output
*/
public int compare(QuizQuestion obj1, QuizQuestion obj2)
	{
	if (obj1 instanceof MultipleChoice && obj2 instanceof MultipleChoice
		|| obj1 instanceof ShortAnswer && obj2 instanceof ShortAnswer)
		{
		String id1 = obj1.getQuestionIndex().toLowerCase();
		String id2 = obj2.getQuestionIndex().toLowerCase();
		if (id1.equals(id2))
			{
			return 0;
			}
		else
			{
			return obj1.getQuestionIndex().compareTo(obj2.getQuestionIndex());
			}
		}
	else if (obj1 instanceof MultipleChoice && obj2 instanceof ShortAnswer)
		{
		return 1;
		}
	else //if (obj1 instanceof ShortAnswer && obj2 instanceof MultipleChoice)
		{
		return -1;
		}
	
	}
}