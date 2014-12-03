   import java.util.Scanner;

/**
 * This class is a client for our Tic-Tac-Toe game.
 *
 * @author Christina Grajales
 * @version 4-26-2012
 */
   public class TTTClient
   {
      public static void main(String[] args)
      {
         Scanner scan = new Scanner(System.in);
         ClassicBoard b = new ClassicBoard();
         ClassicAI ai = new ClassicAI();
         int numberOfMoves = 1;
			//*****
			int humansLastMove = -1;
      
         System.out.println("The Computer is 1, you are 2, and 0 is an empty spot.");
         System.out.println("The Computer's Turn.");
         b = ai.firstMove();
         b.printBoard();
         numberOfMoves++;
      	
         while(b.findWin() <= 0 && numberOfMoves < 10)
         {
            if (numberOfMoves % 2 == 0)
            {
               System.out.println("Your turn now. Please enter an integer from 1 to 9.");
               int in1 = scan.nextInt();
               while(!b.makeMove(2,in1))
               {
                  System.out.println("You entered an invalid move. Please enter a new one.");
                  in1 = scan.nextInt();
               }
					humansLastMove = in1;
               b.printBoard();
               numberOfMoves++;
            }
            else
            {
               System.out.println("The Computer's Turn.");
					//I need this line to be added!!!
					//-Albert*********************
               b = ai.makeComputerMove(b, numberOfMoves, humansLastMove); 
					//****************************
               b.printBoard();
               numberOfMoves++;
            }
         }
         if (b.findWin() == 1)
      	{
         	System.out.println("The Winner is X (The Computer)");
      	}
      	else if (b.findWin() == 2)
      	{
      		System.out.println("The Winner is O (YOU)!!!");
      	}
      	else
      	{
      		System.out.println("There was no winner :(");
      	}
      }
   }