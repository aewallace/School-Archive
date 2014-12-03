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
bool arrayDisplay(int input_array[], int array_size);
void keyToContinue(void);

/*
 * Calling this function runs all implemented tests.
 */
void runTests(void);
/* 
 * Test driver for sort().
 * test2_sort(): A for loop is used.
 */
void test2_sort(void);
/*
 * Test driver for arrayDisplay()
 */
void test_arrayDisplay(void);
/* 
 * Tests the getFileName method
 */
void test_getFileName(void);

//represents other test functions that could not be successfully implemented
void testOtherFunctions(void);


/*****************************
 * Main function begins here.
 *****************************
 */
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
	
/*******************************
 * Helper functions begin here.
 *******************************
 */


//runs all unit test cases
void runTests(void)
	{
	test_getFileName();
	keyToContinue();
   test2_sort();
	keyToContinue();
	test_arrayDisplay();
	keyToContinue();
	testOtherFunctions();
	keyToContinue();
	}
	
//used only to retrieve the file name from user keyboard input
//returns the filename as a string	
string getFileName()
	{
	std::cin.clear();
	string filename;
	cin >> filename;
	std::cin.clear();
	return filename;
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
		cout << "Please check your file name and try again." << endl;
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
	
//initialized the file writing process
//works in tandem with toDisk() to accomplish this task
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



void test2_sort(void)
{
	cout << "Unit Test Case 2: Function Name - sort()\n";
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
   
   cout << "Merging inputArray1:\n";
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

   cout << "...with inputArray2:\n";
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

void test_arrayDisplay()
	{
	cout << "Unit test Case 3: Function name - arrayDisplay().\n";
	int inputArray1_size = 6;
	int inputArray1[inputArray1_size];
	inputArray1[0] = 4;
   inputArray1[1] = 13;
   inputArray1[2] = 14;
   inputArray1[3] = 17;
   inputArray1[4] = 23;
   inputArray1[5] = 89;
   
	cout << "\tPart 1:\n";
	cout << "\tIf the input array is said to have a size less than or equal to zero...\n";
	cout << "\tExample: arrayDisplay(inputArray1, -1)\n";
	assert(false == arrayDisplay(inputArray1, -1));
	cout << "\tSuccess; no data was read from the array.\n";
	
	cout << "\tPart 2:\n";
	cout << "\tIf the input array is said to have a size greater than zero...\n";
	cout << "\tExample: arrayDisplay(inputArray1, 6)\n";
	assert(true == arrayDisplay(inputArray1, 6));	
	cout << "\tSuccess; the array could be read and displayed properly.\n";
	cout << "\n";
	cout<< "Unit Test 3 passed.\n";
	}

void test_getFileName()
	{
	cout << "To begin testing, please input non-empty strings as prompted:\n";
	string fileName = "";
	
	string string1 = "\tEnter one word\n";
	string string2 = "\tEnter another word:\n";
	string string3 = "\tEnter any string with no spaces:\n";
	string string4 = "\tEnter any number of characters with no spaces:\n";
	
	cout << string1;
	fileName = getFileName();
	assert (fileName != "");
	
	fileName = "";
	cout << string2;
	fileName = getFileName();
	assert (fileName != "");
	
	fileName = "";
	cout << string3;
	fileName = getFileName();
	assert (fileName != "");
	
	fileName = "";
	cout << string4;
	fileName = getFileName();
	assert (fileName != "");
	
	cout << "Character entry test passed.\n";
	}

void testOtherFunctions(void)
	{
	cout << "***Testing of other functions not implemented due to variable file system structure;\n";
	cout << "***Internal tests for each method will avoid most problems.\n";
	}
	
void keyToContinue(void){ //use this method for Linux
	std::cin.clear();
	cout << "Enter any character to continue...";
	cin.ignore().get(); //Pause Command for Linux Terminal
	cout << "\n\r";
	}


// :)