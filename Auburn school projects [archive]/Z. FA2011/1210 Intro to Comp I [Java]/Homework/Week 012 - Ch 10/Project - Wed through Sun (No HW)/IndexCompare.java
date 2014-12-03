import java.util.Comparator;
/**
*Used to compare quiz questions based on index.
*
*@author Albert Wallace -- section 003
*@version 11/13/2011
*/

public class IndexCompare implements Comparator<QuizQuestion>
{	/**
	*Method that compares two objects. Used for sorting functions.
	*
	*@param obj1 the first object of comparison
	*@param obj2 the second object of comparison
	*
	*@return returns a positive, negative, or 0, depending on required output
	*/
	public int compare(QuizQuestion obj1, QuizQuestion obj2)
		{
		String id1 = obj1.getQuestionIndex().toLowerCase();
		String id2 = obj2.getQuestionIndex().toLowerCase();
		if (id1.equals(id2))
			{
			return 0;
			}
		else
			{/**
			if (id1.length() < id2.length())
				{
				for (int i = 0; i < id2.length() - id1.length(); i++)
					{
					id1 = "0" + id1;
					}
				}
			if (id2.length() < id1.length())
				{
				for (int i = 0; i < id1.length() - id2.length(); i++)
					{
					id2 = "0" + id2;
					}
				}*/
			return id1.compareTo(id2);
			}
		
		}
}