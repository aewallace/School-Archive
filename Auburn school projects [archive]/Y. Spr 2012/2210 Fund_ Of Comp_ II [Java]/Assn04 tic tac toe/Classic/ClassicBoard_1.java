   import java.util.Arrays;
  
  /**
   * Creates a classic board for tic-tac-toe.
	*
	* @author Christina Grajales
	* @version 4-25-2012
	*/
   public class ClassicBoard
   {
      int numberOfMovesPlayed = 0;
      int lastMove = 0;
      int[][] board;
   
   	/**
   	 * Creates a ClassicBoard using a 2D array of int(s).
   	 * X-1s, O-2s
   	 */
      public ClassicBoard()
      {
         board = new int[3][3];
      }
   
   	/**
   	 * Returns the player in square square (1-9).
   	 *
   	 * @param square - the square with the move to return (int)
   	 * @return move - the player whose move is in the square (int)
   	 */
      public int getMove(int square)
      {
         int x = square / 3;
         int y = 0;
         if (square <= 3)
         {
            x = square - 1;
            y = 0;
         }
         else if (square > 3 && square <= 6)
         {
            x =  square - 4;
            y = 1;
         }
         else if (square > 6)
         {
            x = square - 7;
            y = 2;
         }
         return board[y][x];
      }
   
   	/**
   	 * Creates a move in the board where player owns square square (1-9).
   	 *
   	 * @param player - the player whose turn it is currently (int)
   	 * @param square - the square with the move to return (int)
   	 * @return true - the player move is in the square (boolean)
   	 * @return false - the player's move is invalid (boolean)
   	 */
      public boolean makeMove(int player, int square)
      {
         int x = square / 3;
         int y = 0;
         if (square <= 3)
         {
            x = square - 1;
            y = 0;
         }
         else if (square > 3 && square <= 6)
         {
            x =  square - 4;
            y = 1;
         }
         else if (square > 6)
         {
            x = square - 7;
            y = 2;
         }
         if (board[y][x] == 0)
         {
            board[y][x] = player;
            numberOfMovesPlayed++;
            lastMove = square;
            return true;
         }
         return false;
      }
      
   	/**
   	 * Returns the last move made's square (1-9).
   	 *
   	 * @return lastMove - the square with the last move (int)
   	 */
      public int getLastMove()
      {
         return lastMove;
      }
   	
   	/**
   	 * Returns a string representation of the board.
   	 *
   	 * @return output - the String representation of the board (String)
   	 */
		 
///********************
		//I need this
		//used for computer moves
		public boolean makeAltMove(int square)
      {
			int player = 1; //1 represents computer; always computer moves
         int x = square / 3;
         int y = 0;
         if (square <= 3)
         {
            x = square - 1;
            y = 0;
         }
         else if (square > 3 && square <= 6)
         {
            x =  square - 4;
            y = 1;
         }
         else if (square > 6)
         {
            x = square - 7;
            y = 2;
         }
         if (board[y][x] == 0)
         {
            board[y][x] = player;
            numberOfMovesPlayed++;
            lastMove = square;
            return true;
         }
			else //if you can't land your dot/mark there
			{//put it somewhere else
			boolean check = false;
			for (int i = 1; i < 10; i++)
				{
				check = makeMove(player, i);
				if (check)
					{
					i = 10;
					}
				}
			}
         return false;
		}
		      

      public String toString()
      {
         String output = "";
         output += (Arrays.toString(board[0])) + "\n";
         output += (Arrays.toString(board[1])) + "\n";
         output += (Arrays.toString(board[2])) + "\n";
         
         return output;
      }
      
   	/**
   	 * Prints the board to System.out and adds a new line character at the end.
   	 */
      public void printBoard()
      {
         System.out.println(toString());
      }

      //returns 1 if X wins, 2 if O wins, and 0 if there is no win
      public int findWin()
      {
    	  //8 possible ways to win: three across, three up and down, two diagonals
  		
    	  //across 
    	  // 1 2 3
    	  // 4 5 6
    	  // 7 8 9
  		
    	  if (getMove(1) == getMove(2) && getMove(2)==getMove(3) && getMove(3)!=0 )
    		  return getMove(1);
    	  if (getMove(4) == getMove(5) && getMove(5)==getMove(6) && getMove(6)!=0 )
    		  return getMove(4);
    	  if (getMove(7) == getMove(8) && getMove(8)==getMove(9) && getMove(9)!=0 )
    		  return getMove(7);
  		
  		// up and down
    	  if (getMove(1) == getMove(4) && getMove(4)==getMove(7) && getMove(7)!=0 )
    		  return getMove(1);
    	  if (getMove(2) == getMove(5) && getMove(5)==getMove(8) && getMove(8)!=0 )
    		  return getMove(4);
    	  if (getMove(3) == getMove(6) && getMove(6)==getMove(9) && getMove(9)!=0 )
    		  return getMove(7);
  		
  		//diagonals
  		
  		if (getMove(1) == getMove(5) && getMove(5)==getMove(9) && getMove(5) != 0)
  			return getMove(5);
  		
  		if (getMove(3) == getMove(5) && getMove(5)==getMove(7) && getMove(5) != 0)
  			return getMove(5);
  		
  		
  		return 0;
      }
   }