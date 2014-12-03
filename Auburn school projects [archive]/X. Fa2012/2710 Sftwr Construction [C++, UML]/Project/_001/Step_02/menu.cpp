/*
 * This program shows how to design and implement a menu class for projects
 * conducted in comp2710. This program also demonstrates how to test the menu class.
 *
 * 2012 Xiao Qin <xqin@auburn.edu>
 *
 * Samuel Ginn College of Engineering
 * Auburn University, AL 36849-5347 
 * http://www.eng.auburn.edu/~xqin/
 *
 */
#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <assert.h>
#include <time.h> 

//#define TESTING

using namespace std;

class Menu
{
public:
    void displayOptions( );
    void addAnOption(string newMessage);
    bool selectOption(int& option); //must be updated to handle errors.
private:
    vector<string> optionMessage;
};


int main( )
{
    Menu startMenu;
    Menu mainMenu;
    int startOption;
    int mainOption;

#ifndef TESTING
   
    //Add your product version here. 

#else
	//Add your testing version here. 
    startMenu.addAnOption("1) Strat a New Game of Dunstan and Dragons!");
    startMenu.addAnOption("2) View top 10 High Scores");
    startMenu.addAnOption("3) Quit");
    startMenu.displayOptions();
    startMenu.selectOption(selectedOption);    
    cout << "selected option is" << selectedOption << endl;    
    
    mainMenu.addAnOption("1) Move");
    mainMenu.addAnOption("2) Read technical papers");
    mainMenu.addAnOption("3) Search for losse change");
    mainMenu.addAnOption("4) View character");
    mainMenu.addAnOption("5) Quit the Game");
    mainMenu.displayOptions();
    mainMenu.displayOptions();
    startMenu.selectOption(selectedOption);    
    cout << "selected option is" << selectedOption << endl;    
   
    
    //********* More testing code can be added here **************a
    return 0;
#endif
}

void Menu::displayOptions( ) {
    int i;
    
    for (i = 0; i < optionMessage.size(); i++) 
        cout << optionMessage[i] << endl;
    cout << "Please choose an action:";
}

void Menu::addAnOption(string newMessage) {
    optionMessage.push_back(newMessage);
}

bool Menu::selectOption(int& option ) {
    char ch;

//    cin >> option;

    while ( !( cin >> option ) ) {
        if ( cin.eof() )
            return false;
        else {
            cin.clear();

            //check the user input 
            cout << "Invalid input, please try again (Integer Only!): ";
            while (cin.get(ch) && ch != '\n' );
        }
     } 

  return true;
}