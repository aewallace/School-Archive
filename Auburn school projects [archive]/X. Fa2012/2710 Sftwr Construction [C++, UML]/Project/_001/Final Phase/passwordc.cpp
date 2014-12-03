/*
 * This program shows how to hide passwords.
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
  char pword[BUFSIZ];
  int i = 0;
  int id;
 
  cout << "Enter your id:";
  cin >> id;
  mygetch(); //You must have this line. Otherwise the password segment below can NOT work!
 
  cout << "Enter your password:";
  fflush(stdout);
  
  while ((ch = mygetch()) != EOF 
          && ch != '\n' 
          && ch != '\r' 
          && i < sizeof(pword) - 1)
  {
    if (ch == '\b' && i > 0) 
    {
      cout << "\b \b";
      fflush(stdout);
      i--;
      pword[i] = '\0';
    }
    else if (isalnum(ch))
    {
      cout << '*';
      pword[i++] = (char)ch;
    }
  }

  pword[i] = '\0';
  
  cout << endl << "You id entered:" << id;
  cout << endl << "You password entered:" << pword << endl;
  
  
  return 0;
}