// Xiao Qin (xzq0001)
// xzq0001_hw4.cpp
// Example compiling code: g++ testing_hw4.cpp -o testing_hw4
// Where should we use assert?
// test1_sort(): the first test driver for the sort() function. A list of assertions are used.

#include <iostream>
#include <fstream>
#include <cstring>
#include <assert.h>
using namespace std;

const int FILE_NAME_LEN = 20;

/* Input: (1) inputArray1[]    - the first array of integers in an ascending order
 *        (2) inputArray1_size - the number of ints in inputArray1
 *        (3) inputArray2[]    - the second array of integers in an ascending order
 *        (4) inputArray2_size - the number of ints in inputArray2
 *        (5) outputArray[]    - the array merging inputArray1 and inputArray2
 * Output: the size of outputArray[]
 */
int sort(int inputArray1[], int inputArray1_size, int inputArray2[],
     int inputArray2_size, int outputArray[]);

/* 
 * Two test drivers for sort().
 * test1_sort(): A list of assertions are used.
 * test2_sort(): A for loop is used.
 */
void test1_sort();
void test2_sort();

const int MAX_SIZE = 100;// max array size

int main()
{
   test1_sort();
   test2_sort();
   return 0;
}

void test1_sort(void)
{
   // Variable Declarations
   
   int inputArray1_size;
   int inputArray2_size;
   int outputArray_size;
   int inputArray1[MAX_SIZE];
   int inputArray2[MAX_SIZE];
   int outputArray[MAX_SIZE];
      
   cout << "Test case 1: \n";
   //Array 1
   inputArray1[0] = 4;
   inputArray1[1] = 13;
   inputArray1[2] = 14;
   inputArray1[3] = 17;
   inputArray1[4] = 23;
   inputArray1[5] = 89;
   inputArray1_size = 6;
   
   cout << "inputArray1:\n";
   for (int num = 0; num < inputArray1_size; num++)
   {
      cout << inputArray1[num] << endl;
   }

}


/* 
 * Implementation of openFileToParse1().
 */
void openFileToParse1(ifstream& reader)
{
	char loc[FILE_NAME_LEN];
    
    cout << "Enter the input file name: ";
    cin >> loc;
    reader.open((char*)loc.c_str());

    assert(reader.fail()==false);
}

/* 
 * Implementation of openFileToParse2().
 */
void openFileToParse2(ifstream& reader)
{
	loc = "";
    
    cout << "Enter the input file name: ";
    cin >> loc;
    reader.open((char*)loc.c_str());
   
    if (!reader.good())
    {
        cout << "Error opening the requested file. Please input a valid, uncorrupted file path." << endl;
        openFileToParse2(reader);
    }
}

/* 
 * Implementation of openFileToParse3().
 * Return 0: success
 *        1: failure
 */
int openFileToParse3(ifstream& reader)
{
	char loc[FILE_NAME_LEN];
    
    cout << "Enter the input file name: ";
    cin >> loc;
    reader.open((char*)loc.c_str());
   
    if (reader.fail())
		return 1;
    else return 0; 
}

void successOpenFile(ifstream& reader)
{
	//call openFileToParse.
	// successOpened = false
	//do-while not successOpened 
	//   if openFileToParse3() == 0
	//		successOpened = true;
	//end do while
}

void testOpenFileToParse3(ifstream& reader)
{
	ifstream test_reader;

	cout << "Case 1: enter a correct file name:\n";
	if (openfileToParse3(test_reader) == 0) 
		cout << "Case 1 passed...\n";

	cout << "Case 2: enter a wrong file name:\n";
	if (openfileToParse3(test_reader) == 1) 
		cout << "Case 2 passed...\n";
}
