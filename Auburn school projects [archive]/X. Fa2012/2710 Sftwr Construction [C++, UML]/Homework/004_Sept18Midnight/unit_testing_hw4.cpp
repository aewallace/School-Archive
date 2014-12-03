// Xiao Qin (xzq0001)
// xzq0001_hw4.cpp
// Example compiling code: g++ unit_testing_hw4.cpp -o unit_testing_hw4
//                     or: make unit_testing_hw4 
// test1_sort(): the first test driver for the sort() function. A list of assertions are used.
// test2_sort(): the second test driver for the sort() function. A for loop is used.

#include <iostream>
#include <fstream>
#include <cstring>
#include <assert.h>
using namespace std;


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

/* 
 * Implementation of sort().
 */
int sort(int inputArray1[], int inputArray1_size, int inputArray2[],
     int inputArray2_size, int outputArray[])
{
     //...
}