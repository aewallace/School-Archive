import java.util.ArrayList;

public class QBox extends Box {
	
	ArrayList<int[][]> values; //Value, move number
	ArrayList<int[][]> matchLocations;
	
	//The ArrayList values will store the values. MatchLocations store where the counterpart is located on the Board
	public QBox()
	{
		values = new ArrayList<int[][]>();
		m