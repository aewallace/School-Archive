import java.util.Arrays;
import java.text.DecimalFormat;

public class ScoreTabulation
{
	public static void main(String[] args)
	{
	int[] nums = {5, 4, 3, 2, 7, 10};
	Scores chunk = new Scores(nums);
	
	String returnOne = Arrays.toString(chunk.findEvens());
	System.out.println(returnOne);
	System.out.println("\n");
	String returnTwo = Arrays.toString(chunk.findOdds());
	System.out.println(returnTwo);
	System.out.println("\n");
	
	DecimalFormat Currency = new DecimalFormat("#.###");

	double averageOf = chunk.calculateAverage();
	System.out.println(Currency.format(averageOf) + "\n");
	
	System.out.println(chunk.toString());
	System.out.println("\n" + chunk.toReverseString());
	}
}