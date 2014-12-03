/*
*This class handles the collapses for entanglements.
*
*@author Albert Wallace
*@version b004.010.2012.04.26.16.56.f
*(branch.miniRevision.year.month.day.hour.minute.BOOLEANusable)
*/

import java.util.ArrayList;


public class procUnder
{
 int X = 1, O = 0;
 int type = 0, move = 1, location = 2;
 ArrayList<String> doNotUse = new ArrayList<String>();
//this code will decide moves and collapses
//there is no intelligence; it just works (on some level)
//it probably will lose, but....


//When working with QBox's moves/return types:
// int[0] = type. If return 0, O. If return 1, X.
// int[1] = move. If return 1, 1. (X1), if return 2, 2. (O2, etc.)
// int[2] = corresponding location for that move. 1 through 9 = location of the box.

/*
*This method is the initial step in collapsing things across the board.
*It assumes that you pass in the board, and an INTEGER ARRAY
* of locations/addresses of the squares to be collapsed.
*There is currently no way to dictate which move you want to pass in first.
* (The computer always decides).
*
*@param brdIn the board we need to collapse
*@param squares the numbers of the squares that must be edited/collapsed
*/
public Board initCollapse(Board brdIn, int[] squares)
	{
	System.out.println("\n\rInit collapse. Preparing storage facilities...\n\r");
	doNotUse.add("");
	//new plan: take the board, get the boxes, process the boxes in a new method,
	//make a new board, return the new board (or replace the affected boxes
	//by doing a switch (if value is Box1, replace box1, etc, etc)
	ArrayList<QBox> boxes = new ArrayList<QBox>();
	
	System.out.println("\n\rCollapsing, phase 1...\n\r");
	
	for (int i = 0; i < squares.length; i++)
		{
		activityIndicator(i);
		boxes.add(brdIn.accessBox(squares[i]));
		}
	//took the board, got the boxes
	
	System.out.println("\n\rCollapsing, phase 2...please wait.\n\r");
	
	//now to process the boxes in a new method
	boxes = collapseByParts(boxes);
	//processed the boxes
	
	System.out.println("\n\rCollapsing, phase 3...please wait.\n\r");
	//now to use the modified boxes as replacements in the board
	for (int j = 0; j < boxes.size(); j++) //j used to remember position in cycle
													//j also used as a pointer to actual square being stored
													//i.e. squares[0] may be Box2, squares[1] is Box5, etc.
		{
		activityIndicator(j);
		//we're going to hope the boxes are in proper order
		//there is no querying each box for its location
		//so just stick things back where the initial address is. allegedly.
		//the int array "squares" provides this information.
		//this assumes we can just replace a box
		//I may need to ask for method to replace said box
		int position = squares[j];//position in the board to place the box

		//new board = old board spliced with one box from "boxes" at a time, at given position;
		brdIn = replaceBoxHelper(position, brdIn, boxes.get(j));
		}
	System.out.println("\n\rFinal phase of collapse.\n\r");
	//now that we've replaced the boxes, can we return the board?
	//No; must clear doNotUse, to prepare for next time around.
	doNotUse.clear();
	//NOW can we return the board?
	//We can!
	//returning board brdIn, since it seems no new board was made for modifications
	return brdIn;
	}


/*
*Method to collapse a series of squares/boxes. 
*Accepts afflicted boxes culled--from the board--to collapse
*then returns to initCollapse so initCollapse can re-form a board.
*REQUIRES initCollapse to modify the board!
*
*@param boxes the boxes to be affected by the collapse, as an ArrayList
*(being able to push/pop would be nice, but it works just as well as an ArrayList)
*/
public ArrayList collapseByParts(ArrayList<QBox> boxes)
	{
	if (boxes.size() == 1) //recursive, if only one box left
		{
		ArrayList<int[]> movesInBox = boxes.get(0).getValues();
		//we now have the arraylist of values that represent the moves, movesInBox
		//so we need to search for an X in that collection of moves.
		//if an X is found, use it
		//since it's an arraylist of int arrays, we need to search all the intIn[type]
		//or intIn[0] values for 1, as 1 represents X.
		//a loop may do well to help here
		System.out.println("\n\rChecking initial box & cascading from there.");
		for (int zt = 0; zt < movesInBox.size(); zt++)
			{
			activityIndicator(zt);
			int[] inputter = movesInBox.get(zt);
			if (inputter[type] == X)
				{
				//if we get an X, set the value as an X
				boxes.get(0).setValue(X);
				//then be sure to write the used value to doNotUse
				//the stored move value requires conversion to add to doNotUse
				doNotUse.add(moveConverter(movesInBox.get(zt)));
				//do not touch the basic values
				//then exit the cycle
				zt = movesInBox.size() + 1;
				}
			else{ //assumes there was no X if it reached this point
					if (zt == movesInBox.size() - 1)
						{
						boxes.get(0).setValue(O);
						doNotUse.add(moveConverter(movesInBox.get(zt)));
						}
				}
			}
		
		return boxes;
		} //end one box left; begin rest of recursion decision
	else // if (boxes.length > 1)
		{
		ArrayList<QBox> boxesLess1 = new ArrayList<QBox>();
		boxesLess1 = boxes; //copy the boxes to drop the first one
		QBox boxN0 = boxes.get(0); //copy the first one to collapse
		boxesLess1.remove(0); //remove the first box
		boxes = collapseByParts(boxesLess1); //recursively repeat the processing for all other boxes
		//process the single box based on the new first box
		boxN0 = chooseAnXorO(boxN0);
		//add boxN0 back to the beginning of boxes (which had been boxesLess1 till now)
		boxes.add(boxN0);
		return boxes; //returns the new set of boxes for further processing
		}	
	}//end collapseParts method
	
	public QBox chooseAnXorO(QBox setup) //use to read what not to use and select an X or O
			//I'm going to need a way to store what not to use--EDIT: Stored in doNotUse
		{
		//check dontUse variables, then choose haphazardly based on that
		ArrayList potValues = setup.getValues(); //get the potential values that must be collapsed
		for (int i = 0; i < potValues.size(); i++)
			{
			activityIndicator(i);
			
						/*if the value is invalid for setting....*/
			if (doNotUse.contains(moveConverter(potValues.get(i))))
				{
				//do nothing but ignore that value and iterate
				}
			else //if the value being queried isn't invalid
				{
				//aka, if the value we just selected is a good value
				//put the value down; there is nothing else to do
				int[] gVal = potValues.get(i);
				setup.setValue(gVal[type]);
				i = potValues.size(); //so that we exit the loop fairly quickly.
				doNotUse.add(moveConverter(gVal));
				}
			}		
		return setup;
		}//end chooseAnXorO method
		
/*
*Method to convert from inner-program address & type representation
* to human-readable type information (enables searching by contents).
*
*@param herInfo [see below].
* int[0] = type. If return 0, O. If return 1, X.
* int[1] = move. If return 1, 1. (X1), if return 2, 2. (O2, etc.)
* int[2] = corresponding location for that move. 1 through 9 = location of the box.
*@return returns a string X1, O2, etc.
*/
public String moveConverter(int[] hInfo)
	{
	
	String toReturn = "";
	if (hInfo[type] == X)
		{
		toReturn += "X";
		}
	if (hInfo[type] == O)
		{
		toReturn += "O";
		}
	toReturn += "" + hInfo[move];
	return toReturn;
	}//end conversion of box info
		
/*
*Method to help replace boxes in the board, using ints 1-9 as the box to replace.
*1-3 is the top row, 7-9 are the bottom.
*REPLACES ONE BOX WITH EACH CALL.
*Uses a switch to directly replace the box, then return immediately.
*
*@param boxRef the box number 1-9 to be addressed
*@param board the board to be modified
*@param boxRep the box used to modify the board
*@return returns the board with the box requested replaced
*/
public Board replaceBoxHelper(int boxRef, Board boardIn, Box boxRep)
	{
	/*
		To access boxes, refer to these addresses:
		(replace "board" with the name of the board)
		board[1][1] = 1
		board[1][2] = 2
		board[1][3] = 3
		board[2][1] = 4
		board[2][2] = 5
		board[2][3] = 6
		board[3][1] = 7
		board[3][2] = 8
		board[3][3] = 9
		*/
	switch (boxRef) {
		case 1: board.setBox(1,1,boxRep);
		return board;
		case 2: board.setBox(1,2,boxRep);
		return board;
		case 3: board.setBox(1,3,boxRep);
		return board;
		case 4: board.setBox(2,1,boxRep);
		return board;
		case 5: board.setBox(2,2,boxRep);
		return board;
		case 6: board.setBox(2,3,boxRep);
		return board;
		case 7: board.setBox(3,1,boxRep);
		return board;
		case 8: board.setBox(3,2,boxRep);
		return board;
		case 9: board.setBox(3,3,boxRep);
		return board;
		default: System.out.println("\n\rErr: method replaceBoxHelper failed; returning unmod'd board");
		return board;
		}//end switch
	return board;
	}//end replaceBoxHelper method
	
public void activityIndicator(int cycleInput)
	{
	int decision = cycleInput % 4;
	char output;
	switch (decision){
		case 0: output = '.';
			break;
		case 1: output = ',';
			break;
		case 2: output = ';';
			break;
		case 3: output = ':';
			break;
		default: output = '+';
			break;
		}
	System.out.print(decision);
	}

}
	/*
	Inject into "Board" class, to get access to the board.
	Unfinished.
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

//end procUnder class

/******************************
*Scratch board/old comments
******************************
******************************/
//hard-code the row, column, and diag inas using the p3inna class
//there will be 2 diag + 3 column + 3 row


//pseudocode for figure out 3row, 3column, 3diagonal, 2row, 2column, 2diag
	//if row, must be square 1+2+3; 4+5+6; 7+8+9
	//if column, must be squares 1+4+7; 2+5+8; 3+6+9
	//if diagonal, must be squares 1+5+9 or 3+5+7
	
//given the locations, if X & O, choose the first X. All the time, every time.
//if the game has been set up properly, this will solve all our problems.
//If there are a bunch of Os, just choose the first O.

//we can then store the locations as we go along for the final dumps
//it might be wise to check for what's actually in each box.
	
	//for two in a row, column, or diagonal, can use same checks, since this covers
	//all scenarios

//pseudocode for receive boxes to collapse
	//assuming we receive instructions for boxes to collapse
	
	//check forthe pattern, and possible paths. There will be two possible paths.
	//if either of them makes a selection of X that satisfies 3inna, choose that way
	//this requires checking squares not in the collapse, too
	//so, basically we can hard code the 3inna check to check all boxes every time
	//maybe 3inna can store potential 3inna values as time goes on


//things I need to know:
//--for collapse, am I just getting the board at call time? 
//     Am I getting affected boxes with index numbers?

//I will get board with pointers to affected location.

//--is there a way for me to store the board in my own methods without it being difficult?
//--is there a way for me to store information as it occurs?

//   will I just have to wait for a refreshed board after every move?
//   will I be able to get each move (such as box and contents) to store myself?
//   I want to do this to cut down on my collapse thinking; if none of them match, move on.
//   (It would be active processing as opposed to post-processing).



