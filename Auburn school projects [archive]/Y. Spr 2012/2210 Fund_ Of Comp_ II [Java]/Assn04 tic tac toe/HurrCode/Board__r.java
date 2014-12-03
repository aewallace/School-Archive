import java.util.ArrayList;
public class Board {
	
	Box[][] board;
	//All Boxes containing "X" are said to be 1, all Boxes containing "O" are said to be 0

	
	public Board()
	{
		board = new Box[3][3];
		
		for (int i=0; i<3; i++)
			for (int j=0; j<3; j++)
				board[i][j] = new QBox();
		
	}
	
	public void printBoard()
	{
		
		String[][] strBoard = new String[3][9]; //length x height
		
		for (int i=0; i<3; i++)
			for (int j=0; j<3; j++) //So, per box
			{
				Box box = board[i][j];
				if (box.getClass().equals((new QBox()).getClass())) //If we're dealing with a QBox
				{	
					QBox qbox = (QBox) box;					
					ArrayList<int[][]> values = qbox.getValues();
					int numVal = values.size();//max of 8
					
					//4568					
					
					
					
				}
				else //If we're dealing with a regular Box
				{
					if (box.getValue()==1)
					{
						strBoard[i][(3*j)+0] = "X   X";
						strBoard[i][(3*j)+1] = "  X  ";
						strBoard[i][(3*j)+2] = "X   X";
					}
					else
					{
						strBoard[i][(3*j)+0] = "OOOOO";
						strBoard[i][(3*j)+1] = "O   O";
						strBoard[i][(3*j)+2] = "OOOOO";
					}
						
				}
					
			}
		
		
	}
	
	public void collapseSquare(String collapseTo, int loc1, int loc2)
	{
		board[loc1][loc2] = new Box(collapseTo);		
		
	}
	
	//A cyclic entanglement occurs whenever there is a path from one square back to itself. In a collapse the QBoxes are replaced with Boxes.
	//when a set of boxes contain only complete pairs of themselves... sets of boxes go from 2 to 9.
	//Shit.
	//
	public void findCycleEntaglements()
	{}
	
	public void collapseCycle()
	{}
	
	public void findWin()
	{
		
	}
	
	
}
