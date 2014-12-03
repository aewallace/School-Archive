/*
 * This program demonstrates how to implement "Press any key to continue..."
 *
 * 2012 Xiao Qin <xqin@auburn.edu>
 *
 * Samuel Ginn College of Engineering
 * Auburn University, AL 36849-5347 
 * http://www.eng.auburn.edu/~xqin/
 *
 */
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <ctype.h>
#include <iostream>
using namespace std;

int mygetch ( void ) 
{
  int ch;
  struct termios oldt, newt;
  
  tcgetattr ( STDIN_FILENO, &oldt );
  newt = oldt;
  newt.c_lflag &= ~( ICANON | ECHO );
  tcsetattr ( STDIN_FILENO, TCSANOW, &newt );
  ch = getchar();
  tcsetattr ( STDIN_FILENO, TCSANOW, &oldt );
  
  return ch;
} 

int main()
{
  
  int ch;
    
  cout << "Type your password:";
  cin >> ch;

  ch = mygetch();
  cout << "Press any key to continue...";
  ch = mygetch();
 
  //printf ("\nYou entered >%s<", pword);
  cout << endl << "You pressed: " << ch << endl;
  
  return 0;
}