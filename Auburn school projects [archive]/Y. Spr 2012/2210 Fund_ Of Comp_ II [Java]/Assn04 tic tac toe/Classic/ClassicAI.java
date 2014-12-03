   import java.util.Random;
   import java.util.ArrayList;

/**
*AI for the game's moves
*
*@author: Christina Grajales & Albert Wallace
*@ver: b004.021.20120426.0730P
*/

//this will not be pretty	
//0 = no move, 1 = X, 2 = O.
public class ClassicAI{

	int X = 1, O = 2, blank = 0;
	int human = 2, computer = 1;
	
	//handles making an unintelligent first computer move
	  public ClassicBoard firstMove()
      {
         ClassicBoard b = new ClassicBoard();
         int topLeft = 1;
         b.makeMove(1, topLeft);
         return b;
      }
		
		//handles the third move (the computer's second move, or X3)
		//goal after the first move is to make sure that whereever O goes
		//the third move (X3) is done in the corner opposite
		//unless that corner is occupied
		public ClassicBoard thirdMove(ClassicBoard boardIn)
		{
		boolean moveOn9 = boardIn.makeMove(X, 9);
		if (moveOn9)
			{
			return boardIn;
			}
		else //if we couldn't move on 9
			{
			boardIn.makeMove(X, 3);
			return boardIn;
			}
		}//end of specialized 3rd move method
		
		//handles all other computer moves
		public ClassicBoard fiSeNineMove(ClassicBoard brdIn, int humansLastMove)
		{
			//have preference of checking to see if O is about to have 3 in a row
			//if so, block
			//checks to make for 3 in a row
			//get the last move
			switch (humansLastMove){
			case 2:
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(8);
				if (brdIn.getMove(8) == human)
					brdIn.makeAltMove(5);
					break;
			case 3:
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(7);
				if (brdIn.getMove(6) == human)
					brdIn.makeAltMove(9);
					
				if (brdIn.getMove(7) == human)
					brdIn.makeAltMove(5);
					
				if (brdIn.getMove(9) == human)
					brdIn.makeAltMove(6);
					break;
			case 4:
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(6);
				
				if (brdIn.getMove(6) == human)
					brdIn.makeAltMove(5);
					break;
			case 5:
				if (brdIn.getMove(2) == human)
					brdIn.makeAltMove(8);
					
				if (brdIn.getMove(3) == human)
					brdIn.makeAltMove(7);
					
				if (brdIn.getMove(4) == human)
					brdIn.makeAltMove(6);
					
				if (brdIn.getMove(6) == human)
					brdIn.makeAltMove(4);
					
				if (brdIn.getMove(7) == human)
					brdIn.makeAltMove(3);
					break;
			case 6:
				if (brdIn.getMove(3) == human)
					brdIn.makeAltMove(9);
					
				if (brdIn.getMove(4) == human)
					brdIn.makeAltMove(5);
					
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(4);
					
				if (brdIn.getMove(9) == human)
					brdIn.makeAltMove(3);
					break;
			case 7:
				if (brdIn.getMove(3) == human)
					brdIn.makeAltMove(5);
					
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(3);
					
				if (brdIn.getMove(8) == human)
					brdIn.makeAltMove(9);
					
				if (brdIn.getMove(9) == human)
					brdIn.makeAltMove(8);
					break;
			case 8:
				if (brdIn.getMove(2) == human)
					brdIn.makeAltMove(5);
					
				if (brdIn.getMove(5) == human)
					brdIn.makeAltMove(2);
					
				if (brdIn.getMove(7) == human)
					brdIn.makeAltMove(9);
					
				if (brdIn.getMove(9) == human)
					brdIn.makeAltMove(8);
					break;
			case 9:
				if (brdIn.getMove(3) == human)
					brdIn.makeAltMove(6);
					
				if (brdIn.getMove(6) == human)
					brdIn.makeAltMove(3);
					
				if (brdIn.getMove(7) == human)
					brdIn.makeAltMove(8);
					
				if (brdIn.getMove(8) == human)
					brdIn.makeAltMove(7);
					break;
				}//end switch
			return brdIn;
		
		}
		
		//chooses which method to use depending on the move and makes it
		public ClassicBoard makeComputerMove(ClassicBoard boardIn, int moveNumber, int humansLastMove)
		{
		ClassicBoard tBrd = new ClassicBoard();
		switch (moveNumber){
			case 1: tBrd = firstMove();
				break;
			case 3: tBrd = thirdMove(boardIn);
				break;
			case 5: tBrd = fiSeNineMove(boardIn, humansLastMove);
				break;
			case 7: tBrd = fiSeNineMove(boardIn, humansLastMove);
				break;
			case 9: tBrd = fiSeNineMove(boardIn, humansLastMove);
				break;
			default: System.out.println("Invalid move");
				break;
				}
		return tBrd;
		}
}