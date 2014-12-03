/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw1.cpp
*compiled with jGRASP for initial development.
* (Unable to test in Linux at the moment).
*/

/*
*Homework 001: How much poison?
*Calculates the maximum amount of soda
* a human can consume before dying,
* based on the amount of artificial
* sweetener present in a soda [relative
* to the amount of artifical sweetener
* consumed by test subjects beforehand].
*/

#include <iostream>
using namespace std;


//main method; no other custom methods required
int main()
{
	// one-tenth of 1% of soda is artifical sweetener
	// represented as .001, per instructions
	const float SWEETENER_RATE_PSODA = 0.001;
	
	//variables to store user-entered information
	float userGoalWeight, tsMouseWeight, tsMouseDiedAfter;
	
	//what we calculate for the user
	float userDrinkNoMoreThan;
	
	//ask the fine end user for the goal weight. GOAL. Not current.
	cout << "Hello, user.\n"
			<< "For the greatest accuracy and health benefits,\n"
			<< " Please enter the target weight of the dieter: ";
	cin >> userGoalWeight;
	
	cout << " You entered " << userGoalWeight << " as your *target*.\n"
			<< " If this is incorrect, please restart the program.\n";
			
	//ask the fine end user for the weight of the test subject (mouse).
	cout << "\n" << "For the next step, user," << "\n"
			<< " please enter the weight of the mouse or other subject" << "\n"
			<< " used in laboratory testing: ";
	cin >> tsMouseWeight;
	
	cout << " You entered " << tsMouseWeight << ".\n"
			<< " If this is incorrect, please restart the program.\n";		
	
	//ask the fine end user for how much sweetener would kill a test subject (mouse)
	cout << "\n" << "For the last step, user," << "\n"
			<< " please enter the amount of sweetener that" << "\n"
			<< " killed the test subject during testing: ";
	cin >> tsMouseDiedAfter;
	
	cout << " You entered " << tsMouseDiedAfter << ".\n"
			<< " If this is incorrect, please restart the program.\n";
			
	//this segment takes the user info and calculates the max number of sodas
	//if calculation fails, this section of code is likely the problem
	
	//ideally, we take a proportion
	//	>> amt killed mouse:weight of mouse = amt kill human:weight goal human
	//	and solve for the unknown
	
	//note that amt kill human = # sodas * rate of consumption
	// where our unknown is how many sodas can be consumed
	// now turn this all into code
	
	userDrinkNoMoreThan = ( tsMouseDiedAfter / tsMouseWeight )*( userGoalWeight / SWEETENER_RATE_PSODA );
	
	
	//return the information on how many units of soda to be consumed
	cout << "\n" << "For your health, drink no more than *"
			<< userDrinkNoMoreThan << "* units of diet soda." << "\n";
	cout << " Should you drink more than *" << userDrinkNoMoreThan << "* units," << "\n"
			<< " seek the aid of a doctor immediately!";
	
	
	return 0;
}