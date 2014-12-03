/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw5.cpp
*compiled with jGRASP under Mac OS X 10.6.
*/

/*****************************
 *Homework 005: Trivia Time!
 ****************************/

//****************************************************
// Enable this line to function in debug mode
//	Disable line to enable production version of software
#define UNIT_TESTING
//***************************************************


#include <iostream>
#include <string>
#include <sstream>
#include <assert.h>
using namespace std;

// Maximum number of trivia allowed in trivia array
const int NUM_TRIVIA = 45;

// Structure for each bit of trivia. Contains the question, answer, and award
struct trivia {
  string question;
  string answer;
  int award;
};

//	hard-coded function to initialize the array of trivia questions
int initTriviaArray(trivia triviaArray[], int& currentSize);

//	displays trivia questions on the screen in a defined format
int printTrivia (const trivia triviaAry[], int size, int trivia_index);

// interactive version of printTrivia, allowing player to input guessed answer
int interactivePrintTrivia(const trivia triviaArray[], const int currentSize, const int trivia_index, int& currentPoints);

// adds new trivia to the temporary array; returns the number of items added
int addNewTrivia (trivia triviaArray[], int& currentSize);

#ifdef UNIT_TESTING
//	test runs hard-coded function to initialize the array of trivia questions
void test_initTriviaArray(trivia triviaArray[], int& currentSize);

//	test displays trivia questions on the screen in a defined format
void test_printTrivia (const trivia triviaAry[], int size);

// test interactive version of printTrivia, allowing player to input guessed answer
void test_interactivePrintTrivia(const trivia triviaArray[], const int currentSize, int& currentPoints);


// test adds new trivia to the temporary trivia array;
void test_addNewTrivia (trivia triviaArray[], int& currentSize);
#endif


/*********
 *
 * Main function: one debugging version, one production version
 *
 *********/

#ifdef UNIT_TESTING //if running the debug version
int main()
{
  string debugMessage = "*** This is a Debugging Version of aew0024's Code \"Trivia Time!\" *** \n";
  string exitMessage = "*** End of the Debugging Version *** \n";
  trivia triviaArray[NUM_TRIVIA];
  int currentPoints = 0;
  int currentSize = 0;
  	
	cout << debugMessage;
 	test_initTriviaArray(triviaArray, currentSize);
	test_interactivePrintTrivia(triviaArray, currentSize, currentPoints);
	test_addNewTrivia (triviaArray, currentSize);
	test_printTrivia (triviaArray, currentSize);
	cout << exitMessage;
  
  return 0;
}
#else //if running the production version
int main ()
{
  trivia triviaArray[NUM_TRIVIA];
  int currentPoints = 0;
  int currentSize = 0;
  string welcomeMessage = "*** Welcome to Albert Wallace's trivia quiz game ***";
  string exitMessage = " *** Thank you for playing the trivia quiz game. Goodbye! ***";
  
 	 
  
	initTriviaArray(triviaArray, currentSize);
	
	cout << welcomeMessage;
	cout << "\n";
	

	addNewTrivia (triviaArray, currentSize);
		
	
	for (int trivia_index = 0; trivia_index < currentSize; trivia_index++)
		{	
		interactivePrintTrivia(triviaArray, currentSize, trivia_index, currentPoints);
		cout << "\n";
		}
	cout << "In this game, you earned " << currentPoints << " points total.\n";
	if (currentPoints > 0)
		{
		cout << "Congratulations!\n";
		}
	cout << exitMessage;
  return 0;
}
#endif

// Allows the user to add new trivia.
// Should the currentSize be the maximum addressable size of the array,
// returns zero to indicate zero elements added. Else, returns one
// to indicate one new element added.
int addNewTrivia(trivia triviaArray[], int& currentSize)
	{
	int itemsAdded = 0;
	string addAnotherA = "yes";
 	string addAnotherB = "YES";
 	string addAnotherC = "Yes";
 	string input;
 	int yes = 0, no = 5000;
 	int continueOn = yes;
	
	if (currentSize >= NUM_TRIVIA)
				{
				return itemsAdded; //fail to add items
				}
	else
		{			
			while (continueOn == yes)
			{
			   cout << "Enter a question: ";
		 	   getline (cin,triviaArray[currentSize].question);
		 	   cout << "Enter the answer for this question: ";
		 	   getline (cin,triviaArray[currentSize].answer);
		 	   cout << "Enter award points for this question: ";
			// problem of mixing getline with cin.
			//    cin >> triviaArray[currentSize].award;
			// Solution 1: see the following two lines
			//    getline (cin,mystr);
			//    stringstream(mystr) >> triviaArray[currentSize].award;
			// Solution 2: see the following two lines
		 	   cin >> triviaArray[currentSize].award;
		 	   cin.ignore(1000, '\n');
				
				itemsAdded++;
				currentSize++;
		 		
		
			cout << "\nWould you like to add another trivia question? (Yes/No) ";
			getline(cin, input);
				if (input.compare(addAnotherA) == yes)
					continueOn = yes;
				else if	(input.compare(addAnotherB) == yes)
					continueOn = yes;
				else if (input.compare(addAnotherC) == yes)
					continueOn = yes;
				else
					continueOn = no;
			}//end while
		} //end else
			 
	return itemsAdded; 
	}//end addNewTrivia

int printTrivia (const trivia triviaAry[], int size, int trivia_index)
{
  if (size > NUM_TRIVIA || trivia_index >= size) 
      return 1; //fail

  cout << "Trivia " << trivia_index << "\n";
  cout << "Question: " << triviaAry[trivia_index].question << "\n";
  cout << "Answer: " << triviaAry[trivia_index].answer << "\n";
  cout << "Award: " << triviaAry[trivia_index].award << "\n";
  return 0; //success
}

/*
 * Asks the player a question, accepts input for the player's answer,
 * and checks if the player got the correct answer (awarding them if they did).
 * If their answer was incorrect, displays the correct answer.
 * returns 1 if there is a problem calling due to size mismatch
 * returns 0 if all is well
 */
int interactivePrintTrivia(const trivia triviaArray[], const int currentSize, const int trivia_index, int& currentPoints)
	{
	int additionalPoints = 0;
	if (currentSize > NUM_TRIVIA || trivia_index >= currentSize)
		{ 
      return 1; //fail
		}
		
	int ANSWER_MAX_INPUT_LENGTH = 100;	
	string inputAnswer; 
	
  	cout << "Question: " << triviaArray[trivia_index].question << "\n";
	cout << "Answer: ";
	getline(cin,inputAnswer);
	cout << "\n";
	int STRINGS_ARE_EQUAL = 0;
	if ((triviaArray[trivia_index].answer.compare(inputAnswer)) == STRINGS_ARE_EQUAL)
		{
		additionalPoints = triviaArray[trivia_index].award;
		cout << "Your answer is correct. You receive " << additionalPoints << " points.\n";
		}
	else
		{
		cout << "Your answer is wrong. The correct answer is: " << triviaArray[trivia_index].answer << "\n";
		additionalPoints = 0;
		}
	
	currentPoints = currentPoints + additionalPoints;
  	cout << "Your total points: " << currentPoints << "\n";
  	return 0; //success
	}//end interActivePrintTrivia

// initializes the trivia array with three basic questions
// returns the number of elements created (should return three)
// Increments the currentSize variable automatically so the program knows the actual size.
int initTriviaArray(trivia triviaArray[], int& currentSize)
	{
	int itemsAdded = 0;
	
	triviaArray[0].question = "How long was the shortest war on record? (Hint: how many minutes)";
	triviaArray[0].answer = "38";
	triviaArray[0].award = 100;
	currentSize++;
	itemsAdded++;
	triviaArray[1].question = "What was Bank of America's original name? (Hint: Bank of Italy or Bank of Germany)?";
	triviaArray[1].answer = "Bank of Italy";
	triviaArray[1].award = 50;
	currentSize++;
	itemsAdded++;
	triviaArray[2].question = "What is the best-selling video game of all time? (Hint: Call of Duty or Wii Sports)?";
	triviaArray[2].answer = "Wii Sports";
	triviaArray[2].award = 20;
	currentSize++;
	itemsAdded++;
	
	return itemsAdded;
	}

#ifdef UNIT_TESTING
//	test runs hard-coded function to initialize the array of trivia questions
void test_initTriviaArray(trivia triviaArray[], int& currentSize)
	{
	cout << "Unit Test Case 0.1: Initialize the array of trivia items. (fn: \"initTriviaArray\".)\n";
	int IF_RUN_PROPERLY = 3;
	assert(IF_RUN_PROPERLY == initTriviaArray(triviaArray, currentSize));
	cout << "Case 0.1 (initialization) passed.\n";
	}

//	test displays trivia questions on the screen in a defined format
void test_printTrivia (const trivia triviaAry[], int size)
	{
	int IF_RUN_PROPERLY = 0;
	cout << "Unit Test Case 5.1: Print out all of the trivia currently in the array.\n";
	for (int trivia_index = 0; trivia_index < size; trivia_index++)
		{
		assert (IF_RUN_PROPERLY == printTrivia(triviaAry, size, trivia_index));
		}
	cout << "Case 5.1 Passed.\n";
	cout << "Unit Test Case 5.2: Attempt to print from out-of-bounds location in array.\n";
	int trivia_index_OS = size + 5;
	int FAIL = 1;
	assert (FAIL == printTrivia(triviaAry, size, trivia_index_OS));
	cout << "Case 5.2 Passed.\n";
	}

// test interactive version of printTrivia, allowing player to input guessed answer
void test_interactivePrintTrivia(const trivia triviaArray[], const int currentSize, int& currentPoints)
	{
	int RUNS_PROPERLY = 0;
	cout << "Unit Test Case 1.1: Ask the question of the first trivia in the array. The tester enters a correct answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 0, currentPoints));
	cout << "Case 1.1 Passed\n";
	cout << "Unit Test Case 1.2: Ask the question of the first trivia in the array. The tester enters an incorrect answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 0, currentPoints));
	cout << "Case 1.2 Passed\n";
	cout << "Unit Test Case 2.1: Ask the question of the last trivia in the array. The tester enters a correct answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 2, currentPoints));
	cout << "Case 2.1 Passed\n";
	cout << "Unit Test Case 2.2: Ask the question of the last trivia in the array. The tester enters an incorrect answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 2, currentPoints));
	cout << "Case 2.2 Passed\n";
	cout << "Unit Test Case 3.1: Ask the question of the middle trivia in the array. The tester enters a correct answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 1, currentPoints));
	cout << "Case 3.1 Passed\n";
	cout << "Unit Test Case 3.2: Ask the question of the middle trivia in the array. The tester enters an incorrect answer.\n";
	assert (RUNS_PROPERLY == interactivePrintTrivia(triviaArray, currentSize, 1, currentPoints));
	cout << "Case 3.2 Passed\n";
	}

// test adds new trivia to the temporary trivia array;
void test_addNewTrivia (trivia triviaArray[], int& currentSize)
	{
	cout << "Unit Test Case 4.1: Tests the ability to add new trivia questions. (fn: \"addNewTrivia\")\n";
		int RUNS_PROPERLY = 1;
		assert (RUNS_PROPERLY == addNewTrivia (triviaArray, currentSize));
		cout << "Test Case 4.1 passed.\n";
	cout << "Unit Test Case 4.2: Tests protection from adding question outside of bounds of array. (fn: \"addNewTrivia\".)\n";
		int FAILS = 0;
		int overSized = NUM_TRIVIA + 1;
		assert (FAILS == addNewTrivia(triviaArray, overSized));
		cout << "Test Case 4.2 passed.\n";
	}
#endif

// :)