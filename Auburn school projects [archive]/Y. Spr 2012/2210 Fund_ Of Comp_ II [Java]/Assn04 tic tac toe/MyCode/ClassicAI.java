   import java.util.Random;
   import java.util.ArrayList;

/**
*AI for the game's moves
*
*@author: Christina Grajales & Albert Wallace
*@ver: a001.000.20120426.0558P
*/

//this will not be pretty	
public class ClassicAI{

	int X = 1, O = 0;
	
	//handles making an unintelligent first move
	  public ClassicBoard firstMove()
      {
         ClassicBoard b = new ClassicBoard();
         int randomNum = r.nextInt(4);
         int topLeft = 0;
         b.makeMove(1, topLeft);
         return b;
      }
}