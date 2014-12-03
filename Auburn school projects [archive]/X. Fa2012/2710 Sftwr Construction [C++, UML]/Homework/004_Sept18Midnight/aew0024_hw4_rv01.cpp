/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw4.cpp
*compiled with jGRASP under Mac OS X 10.6 for initial development.
* (Still unable to test in Linux at the moment).
*/

/*
*Homework 004: Two Files In, One File Out!
*/

#include <fstream>
#include <iostream>
#include <cstdlib>  //for exit()
#include <assert.h>
#include <cstring>
using namespace std;

const int MAX_SIZE = 100;// max array size for testing

int readFile(string filename, int fileArray[]);
string getFileName();
int sort(int inputArray1[], int inputArray1_size, int inputArray2[], int inputArray2_size, int outputArray[]);
void writefile(int outputArray[], int outputArray_size);
void toDisk(string fileName, int outputArray[], int outputArray_size);
void runTests(void);
bool arrayDisplay(int input_array[], int array_size);

/* 
 * Two test drivers for sort().
 * test1_sort(): A list of assertions are used.
 * test2_sort(): A for loop is used.
 */
void test1_sort();
void test2_sort();

int main()
	{
	const int inputFileDesiredSize = 100, outputFileDesiredSize = 200;
	int inputArrayOne[inputFileDesiredSize];
	int inputArrayTwo[inputFileDesiredSize];
	int outputFile[outputFileDesiredSize];
	int fileOneTrueSize = 0, fileTwoTrueSize = 0, outputTrueSize = 0;
	string welcome_string = "*** Welcome to Albert Wallace's sorting program! ***";
	
	string fileNameOne, fileNameTwo, fileNameOut;
	
	//run the unit test cases
	runTests();
	
	//run the actual sorting process
	cout << welcome_string << "\n";
	cout << "Please enter the first input file's name: ";
	fileNameOne = getFileName();
	//read the file and store the file count based on input file name
	fileOneTrueSize = readFile(fileNameOne, inputArrayOne);
	
	cout << "The list of " << fileOneTrueSize << " numbers in file "
		<< fileNameOne << " is:\n";
	arrayDisplay(inputArrayOne, fileOneTrueSize);
	
	cout << "Please enter the second input file's name: ";
	fileNameTwo = getFileName();
	//read the file and store the file count based on input file name
	fileTwoTrueSize = readFile(fileNameTwo, inputArrayTwo);
	
	cout << endl;
	cout << "The list of " << fileTwoTrueSize << " numbers in file "
		<< fileNameTwo << " is:\n";
	arrayDisplay(inputArrayTwo, fileTwoTrueSize);
	
	outputTrueSize = sort(inputArrayOne, fileOneTrueSize, inputArrayTwo, fileTwoTrueSize, outputFile);
	
	cout << endl;
	writefile(outputFile, outputTrueSize);
	
	return 0;
	}
	
string getFileName()
	{
	string filename;
	cin >> filename;
	return filename;
	}
	
//runs all unit test cases
void runTests(void)
	{
	test1_sort();
   test2_sort();
	}

//returns file size, since array is static size and may be over sized
//file is opened, written to memory, and closed from here	
int readFile(string filename, int fileArray[])
	{
	ifstream inStream;
   int data;
	
	cout << "Opening file " << filename << "..." << endl;
	
	inStream.open((char*)filename.c_str());
	
	if (inStream.fail())
		{
		cout << "Input file opening failed." << endl;
		exit(1);
   	}
		
	int iteration = 0;
	inStream >> data;
	fileArray[iteration] = data; 
	iteration++;
	
   while (!inStream.eof()) {
   	inStream >> data;
		fileArray[iteration] = data;
		iteration++;
   	}
   inStream.close( );
	return iteration;
	}
	
//displays contents of given array input_array, given size array_size
//the array must have a size; else, this function won't run
bool arrayDisplay(int input_array[], int array_size)
	{
	if (array_size < 1)
		{
		return false;
		}
	for (int i = 0; i < array_size; i++)
		{
		cout << input_array[i] << "\n";
		}
	return true;
	}
	
//returns the output file size, since its array may take up more space than true contents
//files 1 and 2 are read and sorted, with proper sort stored in the output array
//input array sizes are to ensure proper iteration
int sort(int inputArray1[], int inputArray1_size, int inputArray2[], int inputArray2_size, int outputArray[])
	{
	int arrayOne_itr = 0, arrayTwo_itr = 0, outArray_itr = 0;
	
	while (arrayOne_itr < inputArray1_size && arrayTwo_itr < inputArray2_size)
		{
		if (inputArray1[arrayOne_itr] < inputArray2[arrayTwo_itr])
			{
			outputArray[outArray_itr] = inputArray1[arrayOne_itr];
			outArray_itr++;
			arrayOne_itr++;
			}
		else if (inputArray1[arrayOne_itr] > inputArray2[arrayTwo_itr])
			{
			outputArray[outArray_itr] = inputArray2[arrayTwo_itr];
			outArray_itr++;
			arrayTwo_itr++;
			}
		else //if (inputArray1[arrayOne_itr] == inputArray2[arrayTwo_itr])
			{
			outputArray[outArray_itr] = inputArray1[arrayOne_itr];
			outArray_itr++;
			arrayOne_itr++;
			outputArray[outArray_itr] = inputArray2[arrayTwo_itr];
			outArray_itr++;
			arrayTwo_itr++;
			}
		}
	while (arrayOne_itr < inputArray1_size)
		{
		outputArray[outArray_itr] = inputArray1[arrayOne_itr];
		arrayOne_itr++;
		outArray_itr++;
		}
	while (arrayTwo_itr < inputArray2_size)
		{
		outputArray[outArray_itr] = inputArray2[arrayTwo_itr];
		outArray_itr++;
		arrayTwo_itr++;
		}
	return outArray_itr;
	}

void writefile(int outputArray[], int outputArray_size)
	{
	cout << "The sorted list of " << outputArray_size << " numbers is: ";
	int itrn = 0;
	while (itrn < outputArray_size)
		{
		cout << outputArray[itrn];
		cout << " ";
		itrn++;
		}
	cout << "\nEnter the output file name: ";
	string fileName = getFileName();
	
	toDisk(fileName, outputArray, outputArray_size);
	
	cout << "*** Please check the new file - " << fileName << " ***\n";
	cout << "*** Goodbye. ***\n";
	}
	
//writes the file to disk for writeFile function	
void toDisk(string fileName, int outputArray[], int outputArray_size)
	{
	
	ofstream outStream;
	
	outStream.open((char*)fileName.c_str());
	
	if (outStream.fail())
		{
		cout << "Input file opening failed." << endl;
		exit(1);
   	}
		
	for (int i = 0; i < outputArray_size; i++)
		{
		outStream << outputArray[i];
		outStream << '\n';
		}
	
	outStream.flush( );
	
	outStream.close( );
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

   // Array 2
   inputArray2[0] = 3;
   inputArray2[1] = 7;
   inputArray2[2] = 9;
   inputArray2[3] = 14;
   inputArray2[4] = 15;
   inputArray2_size = 5;

   cout << "inputArray2:\n";
   for (int num = 0; num < inputArray2_size; num++)
   {
      cout << inputArray2[num] << endl;
   }
  
   cout << endl;
   

   // sort and print the merged files
   outputArray_size = sort(inputArray1, inputArray1_size, inputArray2,
                           inputArray2_size, outputArray);
   
   //Testing ...
   assert(outputArray[0] == 3);
   assert(outputArray[1] == 4);
   assert(outputArray[2] == 7);
   assert(outputArray[3] == 9);
   assert(outputArray[4] == 13);
   assert(outputArray[5] == 14);
   assert(outputArray[6] == 14);
   assert(outputArray[7] == 15);
   assert(outputArray[8] == 17);
   assert(outputArray[9] == 23);
   assert(outputArray[10] == 89);
   assert(outputArray_size == 11);
   
   cout << "Pass test case 1... \n";
    
   //Case 2:
   //inputArray1: 3 6 10
   //inputArray2: 2
   //outputArray: 2 3 6 10

   //Case 3:
   //inputArray1: 3 6 10
   //inputArray2: 5

   //Case 4:
   //inputArray1: 3 6 10
   //inputArray2: 9

   //Case 5:
   //inputArray1: 3 6 10
   //inputArray2: 15

   //Case 6:
   //inputArray2: 3 6 10
   //inputArray1: 2
   //outputArray: 2 3 6 10

   //Case 7:
   //inputArray2: 3 6 10
   //inputArray1: 5

   //Case 8:
   //inputArray1: 9
   //inputArray2: 3 6 10
   
   //Case 9:
   //inputArray1: 15
   //inputArray2: 3 6 10


}

void test2_sort(void)
{
   // Variable Declarations
   int i;
   int inputArray1_size;
   int inputArray2_size;
   int outputArray_size;
   int inputArray1[MAX_SIZE];
   int inputArray2[MAX_SIZE];
   int outputArray[MAX_SIZE];
   int expectedOutputArray[MAX_SIZE] = {3, 4, 7, 9, 13, 14, 14, 15, 17, 23, 89};
      
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

   // Array 2
   inputArray2[0] = 3;
   inputArray2[1] = 7;
   inputArray2[2] = 9;
   inputArray2[3] = 14;
   inputArray2[4] = 15;
   inputArray2_size = 5;

   cout << "inputArray2:\n";
   for (int num = 0; num < inputArray2_size; num++)
   {
      cout << inputArray2[num] << endl;
   }
  
   cout << endl;
   

   // sort and print the merged files
   outputArray_size = sort(inputArray1, inputArray1_size, inputArray2,
                           inputArray2_size, outputArray);
   
   //Testing ...
   assert(outputArray_size == 11);

   for (i = 0; i < outputArray_size; i++)
	   assert(outputArray[i] == expectedOutputArray[i]);
   
   cout << "Pass test case 1... \n";
    
   //Case 2:
   //inputArray1: 3 6 10
   //inputArray2: 2
   //outputArray: 2 3 6 10

   //Case 3:
   //inputArray1: 3 6 10
   //inputArray2: 5

   //Case 4:
   //inputArray1: 3 6 10
   //inputArray2: 9

   //Case 5:
   //inputArray1: 3 6 10
   //inputArray2: 15

   //Case 6:
   //inputArray2: 3 6 10
   //inputArray1: 2
   //outputArray: 2 3 6 10

   //Case 7:
   //inputArray2: 3 6 10
   //inputArray1: 5

   //Case 8:
   //inputArray1: 9
   //inputArray2: 3 6 10
   
   //Case 9:
   //inputArray1: 15
   //inputArray2: 3 6 10
}

// :)