import java.util.ArrayList;
public class Box {

	//All Boxes containing "X" are said to be 1, all Boxes containing "O" are said to be 0
	int[] value;
	
	public Box()
	{
		value = new int[1];
	}
	public Box(int initialVal)
	{
		value = new int[1];
		this.setValue(initialVal);
	}
	public void setValue(int val)
	{
		value[0] = val;
	}
	
	public ArrayList<int[]> getValues()
	{
		ArrayList<int[]> x = new ArrayList<int[]>();
		return x;
	}
	
	public boolean isQuantum()
	{
		return false;
	}
	
	
}
