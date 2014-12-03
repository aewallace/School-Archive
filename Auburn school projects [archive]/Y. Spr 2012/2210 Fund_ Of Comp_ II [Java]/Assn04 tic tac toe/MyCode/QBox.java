import java.util.ArrayList;

public class QBox extends Box {
	
	ArrayList<int[]> values; //Player Value, move number, counterLocation
	
	//The ArrayList values will store the values. MatchLocations store where the counterpart is located on the Board
	public QBox()
	{
		values = new ArrayList<int[]>();
		
		
	}
	
	//value passed WILL BE a 1/0, followed by the move number, then the counterLocation 1-9
	public void addMove(int[] val)
	{
		values.add(val);
	}
	
	public ArrayList<int[]> getValues()
	{
		return values;
	}
	
	public boolean isQuantum()
	{
		return true;
	}
	
}

// int[0] = type. If return 0, O. If return 1, X.
// int[1] = move. If return 1, 1. (X1), if return 2, 2. (O2, etc.)
// int[2] = corresponding location for that move. 1 through 9 = location of the box.