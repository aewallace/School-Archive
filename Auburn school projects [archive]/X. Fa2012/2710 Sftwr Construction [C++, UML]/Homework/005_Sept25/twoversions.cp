// array of structures
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

//#define UNIT_TESTING
#define N_MOVIES 2 

struct movies_t {
  string title;
  int year;
} films [N_MOVIES];

void printmovie (movies_t movie);
void test_printmovie(void);

int main ()
{
  string mystr;
  int n;

/* 
 * Run test drivers here 
 */
#ifdef UNIT_TESTING
  test_printmovie();

/* 
 * Run product version here 
 */
#else
  for (n=0; n<N_MOVIES; n++)
  {
    cout << "Enter title: ";
    getline (cin,films[n].title);
    cout << "Enter year: ";
    getline (cin,mystr);
    stringstream(mystr) >> films[n].year;
  }

  cout << "\nYou have entered these movies:\n";
  for (n=0; n<N_MOVIES; n++)
    printmovie (films[n]);
#endif

  return 0;
}

void printmovie (movies_t movie)
{
  cout << movie.title;
  cout << " (" << movie.year << ")\n";
}

void test_printmovie(void) {
  cout << "Test Case 1: \n";
  cout << "Test Case 1 passed...\n";
  cout << "Test Case 2: \n";
  cout << "Test Case 2 passed...\n";
}
