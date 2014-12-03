#include <iostream>

using namespace std;

bool get_number ( int& number )
{
  char ch;
  while ( !( cin >> number ) ) { //checks to see if the value in the cin
				//stream is the correct type, if not it returns false,
				//true otwise.
    if ( cin.eof() )			//Will this line be normally executed?
      return false;
    else {

	  cin.clear(); //This corrects the stream.
	  cin.ignore(1000, '\n'); //Ignore 1000 characters or when '\n' is found
        //  while (cin.get(ch) && ch != '\n' ); //What does this line do?
      
	  cout<<"Invalid input, please try again: "; //You may update this line for your own programs
      //while (cin.get(ch) && ch != '\n' ); //What does this line do?

    }
  }

  return true;
}

int main()
{
  int number;
  
  //Test get_number()
  while ( get_number ( number ) )
    cout<< number <<endl;
}
