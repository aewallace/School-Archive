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
					int[][] values = (int[][]) qbox.getValues().toArray();
					int numVal = values.length;//max of 9
					strBoard[i][(j*3)+0] = "";
					strBoard[i][(j*3)+1] = "";
					strBoard[i][(j*3)+2] = "";
					
					for (int m = 0; m<numVal; m++)
					{
						String val;
						if (values[m][0] == 1)
							val = "X" + values[m][1] + "  ";
						else
							val = "O" + values[m][1] + "  ";
						//first entry, mid box
						if (m%3 == 0)
							strBoard[i][(j*3)+1] = strBoard[i][(j*3)+1]+val;
						//second entry, bottom box
						else if(m%3==1)
							strBoard[i][(j*3)+2] = strBoard[i][(j*3)+2]+val;
						//third entry, top box
						else 	
							strBoard[i][(j*3)+0] = strBoard[i][(j*3)+0]+val;
					}
						
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
		
		
		for (int i=0; i<3; i++)
		{	
			System.out.println(strBoard[0][3*i] + "/t |" + strBoard[1][3*i]+ "/t |" + strBoard[2][3*i]);
			System.out.println(strBoard[0][(3*i)+1] + "/t |" + strBoard[1][(3*i)+1]+ "/t |" + strBoard[2][(3*i)+1]);
			System.out.println(strBoard[0][(3*i)+2] + "/t |" + strBoard[1][(3*i)+2]+ "/t |" + strBoard[2][(3*i)+2]);
			System.out.println("--------------------------");
			
		}
		
	}
	
	//player is either "X" or "O"
	//moveNum aka the subscript for a 'spooky' move
	//boardPlacement, 1-9 indcates the box in which you will move
	
	//	1	|	2	|	3
	// -------------------
	//	4	|	5	|	6
	// -------------------
	//	7	|	8	|	9
	//Will return true if the move is completed
	public boolean quantumMove(String player, int moveNum, int place1, int place2)
	{
		//valid move?
		int[] loc1 = {(place1%3)-1,place1/3};
		int[] loc2 = {(place2%3)-1,place2/3};
		
		int playerI;
		
		
		if (player.equalsIgnoreCase("x"))
			playerI = 1;
		else if (player.equalsIgnoreCase("o"))
			playerI = 0;
		else
		{
			System.out.println("Invalid move");
			return false;
		}
		
		//place move
		
		Box box1 = board[loc1[0]][loc1[1]];
		Box box2 = board[loc2[0]][loc2[1]];
		QBox q = new QBox();
		
		if (box1.getClass().equals(q.getClass()) && box1.getClass().equals(q.getClass()));
		{
			
			box1 = (QBox) box1;
			box2 = (QBox) box2;
			
			box1.addValue();
			
		}
		else
		{
			System.out.println("Invalid move placement");
			return false;
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
	
	//return where it happens too, yo
	public int[] findCycleEntaglements()
	{
		/*Alright, bro, here's the plan.
		 * You're going to have a method that will generate an 2D arrays, which will be a set of all possible 
		 * permutaions of 1-9, of length <passed number>
		 * 
		 * Now, given such, you'll have sets of this. FOR EACH of these you will:
		 * 	go through each box, looking at the moves it contains.
		 * 	there will be an array, 'moves', when you find move 2, moves[2]++, etc
		 * 	look through moves; if anything of besides value 0 and 2, it doesn't count 
		 * 	return the set of boxes found
		 */
		
		return null;
	}
	
	public void collapseCycle()
	{
		
	}
	
	public void findWin()
	{
		
	}

	public void accessBox()
	{
	}
	
	/*
	My addition, to get access to the board.
	*/
	/*public void setBox(int row, int column, Box box)
	{
		board[1][1] = 1
		board[1][2] = 2
		board[1][3] = 3
		board[2][1] = 4
		board[2][2] = 5
		board[2][3] = 6
		board[3][1] = 7
		board[3][2] = 8
		board[3][3] = 9
	}*/
	/*
	End Albert's addition.
	*/

	public int[][] permuteationsOf(int n)
	{
		
	}
	
	
}
