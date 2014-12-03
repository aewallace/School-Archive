   import java.util.Random;
   import java.util.ArrayList;

/**
 * Chooses quantum moves for the computer when there is not an entanglment cycle.
 *
 * @author Christina Grajales
 * @version 4-26-12
 */
   public class AI
   {
      static int gameDepth = 1;
   
      int alpha = 0;
      BinaryTreeNode<ClassicBoard> neededBoard;
      BinaryTreeNode<ClassicBoard> gameTree = new BinaryTreeNode<ClassicBoard>(new ClassicBoard());
      BinaryTreeNode<ClassicBoard> alias = gameTree;
      ArrayList<Integer> moveArray = new<Integer>ArrayList();
      Random r = new Random();
   
      /**
   	 * Constructs an AI by initializing the boxes that can be moved in (ArrayList).
   	 */
      public AI()
      {
         for(int i = 1; i < 10; i++)
         {
            moveArray.add(i);
         }
         moveArray.add(r.nextInt(8) + 1);
         moveArray.add(r.nextInt(8) + 1);
         moveArray.add(5);
         moveArray.add(1);
         moveArray.add(3);
         moveArray.add(5);
         moveArray.add(7);
         moveArray.add(9);
      }
   	
   	/**
   	 * Chooses the first move for X (center and a random corner).
   	 *
   	 * @return b - a new board with the quantum move made
   	 */
      public Board firstMove()
      {
         Board b = new Board();
         int randomNum = r.nextInt(3);
         int num = 0;
         switch(randomNum)
         {
            case 0:
               num = 1;
               break;
            case 1:
               num = 3;
               break;
            case 2:
               num = 7;
               break;
            case 3:
               num = 9;
               break;
            default:
               num = 1;
         }
         b.quantumMove("x",1,5,num);
         return b;
      }
   	
   	/**
   	 * Chooses a new board based off of random numbers and probablity heuristics.
   	 *
   	 * @param originalBoard - the board with all of the current game moves (Board)
   	 */
      public Board chooseRandomBoard(Board originalBoard)
      {
         int num1 = r.nextInt(moveArray.size()) - 1;
         int num2 = r.nextInt(moveArray.size()) - 1;
         while (!originalBoard.quantumMove("x",gameDepth,moveArray.get(num1),moveArray.get(num2)))
         {
            num1 = r.nextInt(moveArray.size()) - 1;
            num2 = r.nextInt(moveArray.size()) - 1;
         }
         moveArray.add(moveArray.get(num1));
         moveArray.add(moveArray.get(num2));
      	
         return originalBoard;
      }
   
   	/**
   	 * Constructs a game tree for the Board given.
   	 *
   	 * @param originalBoard - the board with all of the current game moves (Board)
   	 */
      public void constructGameTree(Board originalBoard)
      {
      	//test
         Board temp = originalBoard;
         for(int i = 0; i < 3; i++)
         {
            alias = gameTree;
            int points = 0;
            for(int j = 0; j < 3; j++)
            {
               int square = 1;
               if (i <= 0)
                  square = (j + 1);
               else if (i == 1)
                  square = (j + 4);
               else if (i >= 2)
                  square = (j + 7);
               
               ClassicBoard b = new ClassicBoard();
               for(int k = 0; k < temp.accessBox(square).size(); k++)
               {
                  points = 0;
                  int player = temp.accessBox(square).get(k)[0];
                  b.makeMove(player, square);
                  if (square == 1 || square == 3 || square == 7 || square == 9)
                  {
                     if (player == 0)
                        points += -2;
                     else
                        points += 2;
                  }
                  else if (square == 2 || square == 4 || square == 6 || square == 8)
                  {
                     if (player == 0)
                        points += -1;
                     else
                        points += 1;
                  }
                  else
                  {
                     if (player == 0)
                        points += -3;
                     else
                        points += 3;
                  }
                  alias.right = new BinaryTreeNode<ClassicBoard>(b);
                  alias = alias.right;
                  alias.setValue(points);
               }
               alias.left = new BinaryTreeNode<ClassicBoard>(b);
               alias = alias.left;
               alias.setValue(points);
            }
         }
         alias = gameTree;
      }
   	
   	/**
   	 * Chooses an optimal board from the game tree.
   	 *
   	 * @param originalBoard - the board with all of the current game moves (Board)
   	 * @return board - a new board with the quantum move made
   	 */
      public Board chooseBoard(Board originalBoard)
      {
         int searchTerm = minimax(gameTree.left, gameDepth);
         BinaryTreeNode<ClassicBoard> moveA = gameTree.left.search(searchTerm);
         int square1 = moveA.getElement().getLastMove();
         searchTerm = minimax(gameTree.right, gameDepth);
         BinaryTreeNode<ClassicBoard> moveB = gameTree.right.search(searchTerm);
         int square2 = moveB.getElement().getLastMove();
      	
         originalBoard.quantumMove("x", gameDepth-1, square1, square2);
      	
         gameDepth = gameDepth + 2;
      }
   
   	/**
   	 * Minimax algorithm.
   	 *
   	 * @param n - the gameTree for the current board (BinaryTreeNode)
   	 * @param depth - the depth of the leaves in the gameTree (int)
   	 * @return alpha - the integer representation of the optimal board (int)
   	 */
      public int minimax(BinaryTreeNode n, int depth) //depth is number of moves + 1 (root is empty)
      {
         if (n.noChild() || depth <= 0)
         {
            return n.getValue();
         }
         alpha = -100;
         while (!n.noChild())
         {
            if (n.getLeft() != null)
               alpha = max(alpha, -minimax(n.getLeft(), depth - 1));
            if (n.getRight() != null)
               alpha = max(alpha, -minimax(n.getRight(), depth - 1));
         }
         neededBoard = n.search(alpha);
         return alpha;
      }
   
   	/**
   	 * Chooses the maximum value of the two integer parameters.
   	 *
   	 * @param alpha - the integer representation of the estimated optimal board (int)
   	 * @param compVar2 - the integer to compare alpha with (int)
   	 * @return num - the larger integer (int)
   	 */
      public int max(int alpha, int compVar2)
      {
         return alpha > compVar2 ? alpha : compVar2;
      }
   }