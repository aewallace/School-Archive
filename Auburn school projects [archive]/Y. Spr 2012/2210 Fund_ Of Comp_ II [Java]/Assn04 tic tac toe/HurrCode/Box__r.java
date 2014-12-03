
public class Box {

	//All Boxes containing "X" are said to be 1, all Boxes containing "O" are said to be 0
	int value;
	
	public Box()
	{}
	public Box(int initialVal)
	{
		this.setValue(initialVal);
	}
	public void setValue(int val)
	{
		value = val;
	}
	
	public int getValue()
	{
		return value;
	}
	
	
}
