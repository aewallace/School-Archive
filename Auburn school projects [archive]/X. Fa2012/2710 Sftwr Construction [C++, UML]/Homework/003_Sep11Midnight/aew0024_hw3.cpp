/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw3.cpp
*compiled with jGRASP under Mac OS X 10.6 for initial development.
* (Still unable to test in Linux at the moment).
*/

/*
*Homework 003: Best Player!
*/

#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <assert.h>
#include <ctime>
using namespace std;

bool at_least_two_alive(bool A_alive, bool B_alive, bool C_alive);
/* Input: A_alive indicates whether Aaron is alive */
/*	B_alive indicates whether Bob is alive */
/*	C_alive indicates whether Charlie is alive */
/* Return: true if at least two are alive */
/*	otherwise return false */ 
void Aaron_shoots1(bool& B_alive, bool& C_alive);
/* Strategy 1: Use call by reference 
* Input: B_alive indicates whether Bob alive or dead 
*	C_alive indicates whether Charlie is alive or dead 
* Return: Change B_alive into true if Bob is killed. 
*	Change C_alive into true if Charlie is killed.
*/ 
void Bob_shoots(bool& A_alive, bool& C_alive);
/* Call by reference 
* Input: A_alive indicates if Aaron is alive or dead 
*	C_alive indicates whether Charlie is alive or dead 
* Return: Change A_alive into true if Aaron is killed. 
*	Change C_alive into true if Charlie is killed.
*/ 
void Charlie_shoots(bool& A_alive, bool& B_alive);
/* Call by reference 
* Input: A_alive indicates if Aaron is alive or dead 
*	B_alive indicates whether Bob is alive or dead 
* Return: Change A_alive into true if Aaron is killed. 
*	Change B_alive into true if Bob is killed.
*/
void Aaron_shoots2(bool& B_alive, bool& C_alive);
/* Strategy 2: Use call by reference 
* Input: B_alive indicates whether Bob alive or dead 
*	C_alive indicates whether Charlie is alive or dead 
* Return: Change B_alive into true if Bob is killed. 
*	Change C_alive into true if Charlie is killed.
*/

//the following provide tests for their respective methods
void test_at_least_two_alive(void);
void test_Aaron_shoots1(void);
void test_Bob_shoots(void);
void test_Charlie_shoots(void);
void test_Aaron_shoots2(void);
void keyToContinue(void);

/*the following provide tests for Aaron's two strategies
*each method returns Aaron's wins, letting a parent function determine which is better
*/
int strategy_one_analysis(int totalNumberOfRuns);
int strategy_two_analysis(int totalNumberOfRuns);

//main function
int main()
{
	int const totalNumberOfRuns = 10000;
	int Aaron_strategy_one_wins = -15; //used to contain the number of wins Aaron gets under Strt. 1
	int Aaron_strategy_two_wins = -45; //used to contain the number of wins Aaron gets under Strt. 2
	srand(time(0)); //initialize the random number generator once
	cout << "****Welcome to Albert Wallace's Duel Simulator\n****";
	
	/*this section begins to run the tests, with pauses between each test.
	*all test functions produce their own output until keyToContinue is called
	*/
	test_at_least_two_alive();
	keyToContinue();
	
	test_Aaron_shoots1();
	keyToContinue();
	
	test_Bob_shoots();
	keyToContinue();
	
	test_Charlie_shoots();
	keyToContinue();
	
	test_Aaron_shoots2();
	
	
	cout << "\n\r";
	cout << "Ready to test Strategy One (run " << totalNumberOfRuns << " times):\n";
	keyToContinue();
	Aaron_strategy_one_wins = strategy_one_analysis(totalNumberOfRuns);
	
	
	cout << "\n\r";
	cout << "Ready to test Strategy Two (run " << totalNumberOfRuns << " times):\n";
	keyToContinue();
	Aaron_strategy_two_wins = strategy_two_analysis(totalNumberOfRuns);
	
	cout << "\n";
	
	//the following provide analysis for Aaron's two strategies
	if (Aaron_strategy_one_wins < Aaron_strategy_two_wins) //the only one that should happen!
		{
		cout << "Strategy 2 is better than strategy 1.\n";
		}
	else if (Aaron_strategy_one_wins == Aaron_strategy_two_wins) //should not happen, if rarely
		{
		cout << "Strategy 2 and strategy one performed equally well this time.\n";
		}
	else //should not happen, if rarely
		{
		cout << "Strategy 1 is better than strategy two this time.\n";
		}
		
		
return 0;
}//end main function



int strategy_one_analysis(int totalNumberOfRuns) //returns number of Aaron wins, for Strategy 1
	{
	bool Aaron_alive = true, Bob_alive = true, Charlie_alive = true; //declaration
	int total_Aaron_wins = 0, total_Bob_wins = 0, total_Charlie_wins = 0; //to calculate win percentage/ratio
	
	for (int i = 0; i < totalNumberOfRuns; i++)
		{
		Aaron_alive = true, Bob_alive = true, Charlie_alive = true; //re-set for each of the runs
		do //run this until there is one man standing
			//each man's function should ignore the call if the others are dead already
			{
			if (Aaron_alive)
				{
				Aaron_shoots1(Bob_alive, Charlie_alive);
				}
			if (Bob_alive)
				{
				Bob_shoots(Aaron_alive, Charlie_alive);
				}
			if (Charlie_alive)
				{
				Charlie_shoots(Aaron_alive, Bob_alive);
				}
			}
		while (at_least_two_alive(Aaron_alive, Bob_alive, Charlie_alive));
		if (Aaron_alive)
			total_Aaron_wins++;
		else if (Bob_alive)
			total_Bob_wins++;
		else if (Charlie_alive)
			total_Charlie_wins++;
		else //there should be no case where everyone is dead, but...
			cout << "Everyone somehow died. Fix me!\n";
			
		//no more is done before running another simulation
		}
	//if the simulation is done with n iterations/runs,
	//calculate hits and display stats
	
	int run_check = total_Aaron_wins + total_Bob_wins + total_Charlie_wins;
	float Aaron_percent, Bob_percent, Charlie_percent;
	if (run_check < totalNumberOfRuns)
		{
		cout << "The total wins did not match with the expected number of runs. Please check code.\n";
		cout << "!!!Error Section: Strategy 1 Win Count [E501]\n";
		return 0;
		}
	else
		{
		Aaron_percent = (float) total_Aaron_wins * 100 / (float) totalNumberOfRuns;
		Bob_percent = (float) total_Bob_wins * 100 / (float) totalNumberOfRuns;
		Charlie_percent = (float) total_Charlie_wins * 100 / (float) totalNumberOfRuns;
		
		cout << "Aaron won " << total_Aaron_wins << "/" << totalNumberOfRuns << " duels or " << Aaron_percent << "%.\n";
		cout << "Bob won " << total_Bob_wins << "/" << totalNumberOfRuns << " duels or " << Bob_percent << "%.\n";
		cout << "Charlie won " << total_Charlie_wins << "/" << totalNumberOfRuns << " duels or " << Charlie_percent << "%.\n";
		}
	return total_Aaron_wins;
	}

int strategy_two_analysis(int totalNumberOfRuns) //again, return the number of Aaron wins, this time for S2
	{
	bool Aaron_alive = true, Bob_alive = true, Charlie_alive = true; //declaration
	int total_Aaron_wins = 0, total_Bob_wins = 0, total_Charlie_wins = 0; //to calculate win percentage/ratio
	
	for (int i = 0; i < totalNumberOfRuns; i++)
		{
		Aaron_alive = true, Bob_alive = true, Charlie_alive = true; //re-set for each of the runs
		do //run this until there is one man standing
			//each man's function should ignore the call if the others are dead already
			{
			if (Aaron_alive)
				{
				Aaron_shoots2(Bob_alive, Charlie_alive); //this line is the ONLY change from strategy_one_analysis
				}
			if (Bob_alive)
				{
				Bob_shoots(Aaron_alive, Charlie_alive);
				}
			if (Charlie_alive)
				{
				Charlie_shoots(Aaron_alive, Bob_alive);
				}
			}
		while (at_least_two_alive(Aaron_alive, Bob_alive, Charlie_alive));
		if (Aaron_alive)
			total_Aaron_wins++;
		else if (Bob_alive)
			total_Bob_wins++;
		else if (Charlie_alive)
			total_Charlie_wins++;
		else //there should be no case where everyone is dead, but...
			cout << "Everyone somehow died. Fix me! [R4H1]\n";
			
		//no more is done before running another simulation
		}
	//if the simulation is done with n iterations/runs,
	//calculate hits and display stats
	
	int run_check = total_Aaron_wins + total_Bob_wins + total_Charlie_wins;
	float Aaron_percent, Bob_percent, Charlie_percent;
	if (run_check < totalNumberOfRuns)
		{
		cout << "The total wins did not match with the expected number of runs. Please check code.\n";
		cout << "!!!Error Section: Strategy 2 Win Count [GF02]\n";
		return -1;
		}
	else
		{
		Aaron_percent = (float) total_Aaron_wins * 100 / (float) totalNumberOfRuns;
		Bob_percent = (float) total_Bob_wins * 100 / (float) totalNumberOfRuns;
		Charlie_percent = (float) total_Charlie_wins * 100 / (float) totalNumberOfRuns;
		
		cout << "Aaron won " << total_Aaron_wins << "/" << totalNumberOfRuns << " duels or " << Aaron_percent << "%.\n";
		cout << "Bob won " << total_Bob_wins << "/" << totalNumberOfRuns << " duels or " << Bob_percent << "%.\n";
		cout << "Charlie won " << total_Charlie_wins << "/" << totalNumberOfRuns <<" duels or " << Charlie_percent << "%.\n";
		}
	return total_Aaron_wins;
	}
/*
*checks to see if at least two players are alive
*
*parameters are the status of each of the three players
*returns true if at least two are alive, false if one or zero are alive
*/
bool at_least_two_alive(bool A_alive, bool B_alive, bool C_alive){ 
	if (A_alive && B_alive)
		return true;
	else if (B_alive && C_alive)
		return true;
	else if (A_alive && C_alive)
		return true;
	else
		return false;
	}

//provides the function that controls Aaron's first strategy
void Aaron_shoots1(bool& B_alive, bool& C_alive){
	int shoot_target_result;
	shoot_target_result = rand()%100;
	int const aaron_hit_chance = 33; //Aaron has 1/3 chance to hit, or 33%
	bool hitSuccess = false;
	if (shoot_target_result < aaron_hit_chance) //if it falls inside the hit chance, successful hit
		{
		hitSuccess = true;
		}
	
	if (C_alive)
		{
		C_alive = hitSuccess;
		}
	else if (B_alive)
		{
		B_alive = hitSuccess;
		}
	else
		{
		//do nothing
		}
	}

//provides the function that controls Bob's shooting strategy
void Bob_shoots(bool& A_alive, bool& C_alive){
	int shoot_target_result;
	shoot_target_result = rand()%100;
	int const Bob_hit_chance = 50; //Bob has a 1/2 chance to hit, or 50%
	bool hitSuccess = false;
	if (shoot_target_result <= Bob_hit_chance) //if it falls inside the hit chance, successful hit
		{
		hitSuccess = true;
		}
	
	if (C_alive)
		{
		C_alive = hitSuccess;
		}
	else if (A_alive)
		{
		A_alive = hitSuccess;
		}
	else
		{
		//do nothing
		}
	}

//provides the function that controls Charlie's shooting strategy
void Charlie_shoots(bool& A_alive, bool& B_alive){
	/*
	*no code needed for probabilities; Charlie is always accurate
	*/
	if (B_alive)
		{
		B_alive = false; //always gets shot
		}
	else if (A_alive)
		{
		A_alive = false; //always gets shot
		}
	else
		{
		//do nothing
		}
	}

//provides the function that controls Aaron's second shooting strategy
void Aaron_shoots2(bool& B_alive, bool& C_alive){
	int shoot_target_result;
	shoot_target_result = rand()%100;
	int const aaron_hit_chance = 33; //again, Aaron has a 33% chance of hitting
	bool hitSuccess = false;
	if (shoot_target_result < aaron_hit_chance) //if it falls inside the hit chance, successful hit
		{
		hitSuccess = true;
		}

	if (C_alive && B_alive)
		{
		//do nothing; intentional miss
		}
	else if (C_alive)
		{
		C_alive = hitSuccess;
		}
	else if (B_alive)
		{
		B_alive = hitSuccess;
		}
	else
		{
		//do nothing
		}
	}

/*
*The following is a selection of possible test cases to avoid most issues.
*/
void test_at_least_two_alive(void) { 
	cout << "Unit Testing 1: Function - at_least_two_alive()\n";
	cout << "\tCase 1: Aaron alive, Bob alive, Charlie alive\n"; 
	assert(true	==	at_least_two_alive(true, true, true));	
	cout << "\tCase passed	...\n";
	cout << "\tCase 2: Aaron dead, Bob	alive, Charlie	alive\n";
	assert(true	==	at_least_two_alive(false, true, true)); 
	cout << "\tCase passed	...\n";
	cout << "\tCase 3: Aaron alive, Bob dead, Charlie	alive\n"; 
	assert(true	==	at_least_two_alive(true, false, true)); 
	cout	<<	"\tCase	passed ...\n";
	cout << "\tCase 4: Aaron alive, Bob alive, Charlie dead\n";
	assert(true == at_least_two_alive(true, true, false));
	cout << "\tCase passed ...\n";
	cout << "\tCase 5: Aaron dead, Bob dead, Charlie alive\n";
	assert(false == at_least_two_alive(false, false, true));
	cout << "\tCase passed ...\n";
	cout << "\tCase 6: Aaron dead, Bob alive, Charlie dead\n";
	assert(false == at_least_two_alive(false, true, false));
	cout << "\tCase passed ...\n";
	cout << "\tCase 7: Aaron alive, Bob dead, Charlie dead\n";
	assert(false == at_least_two_alive(true, false, false));
	cout << "\tCase passed ...\n";
	cout << "\tCase 8: Aaron dead, Bob dead, Charlie dead\n";
	assert(false == at_least_two_alive(false, false, false));
	cout << "\tCase passed ...\n";
	}

void test_Aaron_shoots1(void){
	bool B_alive = true, C_alive = true;
	cout << "Unit Testing 2: Function Aaron_shoots1(Bob_alive, Charlie_alive)\n";
	cout << "\tCase 1: Bob alive, Charlie alive\n";
	cout << "\tAaron is shooting at Charlie\n";
	cout << "\t";
	Aaron_shoots1(B_alive, C_alive);
	if (C_alive)
		{
		cout << "Aaron misses.";
		}
	else
		{
		cout << "Charlie is dead.";
		}
	cout << "\n";
	cout << "\tCase 2: Bob dead, Charlie alive\n";
	cout << "\tAaron is shooting at Charlie\n";
	cout << "\t";
	B_alive = false;
	C_alive = true;
	Aaron_shoots1(B_alive, C_alive);
	if (C_alive)
		{
		cout << "Aaron misses.";
		}
	else
		{
		cout << "Charlie is dead.";
		}
	cout << "\n";
	cout << "\tCase 3: Bob alive, Charlie dead\n";
	cout << "\tAaron is shooting at Bob\n";
	cout << "\t";
	B_alive = true;
	C_alive = false;
	Aaron_shoots1(B_alive, C_alive);
	if (B_alive)
		{
		cout << "Aaron misses.";
		}
	else
		{
		cout << "Bob is dead.";
		}
	cout << "\n";
	}

void test_Bob_shoots(void) {
	bool A_alive = true, C_alive = true;
	cout << "Unit Testing 3: Function Bob_shoots(Aaron_alive, Charlie_alive)\n";
	cout << "\tCase 1: Aaron alive, Charlie alive\n";
	cout << "\tBob is shooting at Charlie\n";
	cout << "\t";
	Bob_shoots(A_alive, C_alive);
	if (C_alive)
		{
		cout << "Bob misses.";
		}
	else
		{
		cout << "Charlie is dead.";
		}
	cout << "\n";
	cout << "\tCase 2: Aaron dead, Charlie alive\n";
	cout << "\tBob is shooting at Charlie\n";
	cout << "\t";
	A_alive = false;
	C_alive = true;
	Bob_shoots(A_alive, C_alive);
	if (C_alive)
		{
		cout << "Bob misses.";
		}
	else
		{
		cout << "Charlie is dead.";
		}
	cout << "\n";
	cout << "\tCase 3: Aaron alive, Charlie dead\n";
	cout << "\tBob is shooting at Aaron\n";
	cout << "\t";
	A_alive = true;
	C_alive = false;
	Bob_shoots(A_alive, C_alive);
	if (A_alive)
		{
		cout << "Bob misses.";
		}
	else
		{
		cout << "Aaron is dead.";
		}
	cout << "\n";
	}
 
void test_Charlie_shoots(void){
	bool A_alive = true, B_alive = true;
	cout << "Unit Testing 4: Function Charlie_shoots(Aaron_alive, Bob_alive)\n";
	cout << "\tCase 1: Aaron alive, Bob alive\n";
	cout << "\tCharlie is shooting at Bob\n";
	cout << "\t";
	Charlie_shoots(A_alive, B_alive);
	if (B_alive)
		{
		cout << "Black magic! Bob isn't dead!";
		}
	else
		{
		cout << "Bob is dead";
		}
	cout << "\n";
	cout << "\tCase 2: Aaron dead, Bob alive\n";
	cout << "\tCharlie is shooting at Bob\n";
	cout << "\t";
	A_alive = false;
	B_alive = true;
	Charlie_shoots(A_alive, B_alive);
	if (B_alive)
		{
		cout << "Black magic! Bob isn't dead!";
		}
	else
		{
		cout << "Bob is dead";
		}
	cout << "\n";
	cout << "\tCase 3: Aaron alive, Bob dead\n";
	cout << "\tCharlie is shooting at Aaron\n";
	cout << "\t";
	A_alive = true;
	B_alive = false;
	Charlie_shoots(A_alive, B_alive);
	if (A_alive)
		{
		cout << "Black magic! Aaron isn't dead!";
		}
	else
		{
		cout << "Aaron is dead";
		}
	cout << "\n";
	}

void test_Aaron_shoots2(void){
	bool B_alive = true, C_alive = true;
	cout << "Unit Testing 5: Function Aaron_shoots2(Bob_alive, Charlie_alive)\n";
	cout << "\tCase 1: Bob alive, Charlie alive\n";
	cout << "\tAaron intentionally misses his first shot\n";
	Aaron_shoots2(B_alive, C_alive);
	cout << "\t";
	if (C_alive && B_alive)
		{
		cout << "Both Bob and Charlie are alive.";
		}
	else
		{
		cout << "Someone died even though he intentionally missed.\n";
		cout << "\tWe have a game of Clue on our hands! [RR09]";
		}
	cout << "\n";
	cout << "\tCase 2: Bob dead, Charlie alive\n";
	cout << "\tAaron is shooting at Charlie\n";
	B_alive = false;
	C_alive = true;
	Aaron_shoots2(B_alive, C_alive);
	cout << "\t";
	if (C_alive)
		{
		cout << "Aaron misses.";
		}
	else
		{
		cout << "Charlie is dead.";
		}
	cout << "\n";
	cout << "\tCase 3: Bob alive, Charlie dead\n";
	cout << "\tAaron is shooting at Bob\n";
	B_alive = true;
	C_alive = false;
	Aaron_shoots2(B_alive, C_alive);
	cout << "\t";
	if (B_alive)
		{
		cout << "Aaron misses.";
		}
	else
		{
		cout << "Bob is dead.";
		}
	cout << "\n";
	}
	
//The following is just the "press any key to continue" function, in two variants
//Comment out whichever function is not needed for a given platform

/*
void keyToContinue(void){ //use this method for Linux
	cout << "Enter any character to continue...";
	cin.ignore().get(); //Pause Command for Linux Terminal
	cout << "\n\r";
	}
//*/

///*
void keyToContinue(void){ //use this method for OS X
	cout << "Press enter/return to continue...";
	cin.get(); //Pause command in OS X, allows any key to be pressed to continue
	cout << "\n\r";
	}
//*/

// :)