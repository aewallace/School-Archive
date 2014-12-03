/*
 *Abstract data type "Queue"
 *
 *Uses dynamic arrays. Allows for multiple data types in the queue, 
 * to be defined at variable declaration.
 *
 *HW07, Question 02
 *
*Author: Albert Wallace (aew0024)
*Version: M10.D30.Y2012.T14.27
*
*Compiled under OS X using JGrasp.
*Main method located at end of .cpp file.
*/

#include <iostream>
using namespace std;

template <class T>
class Queue {

   private:
      T *queueArray;
      bool *hasContents;
      int next_index;
      int front;
      int size_index;
      int contains;
   public:
      Queue();
      Queue(int VariableSize);
      ~Queue();
      int enqueue(T typeToEnqueue);
      T dequeue();
      bool empty(); 
      
}; //end class declaration


template<class T>
Queue<T>::Queue()
   {
	int defined_size = 100;
   queueArray = new T[defined_size];
   hasContents = new bool[defined_size];
   next_index  = 0;
   front = 0;
   size_index = defined_size - 1;
   contains = 0;
   for (int i = 0; i < defined_size; i++)
      {
      hasContents[i] = false;
      }
   }
/*int resize(int newSize)
   {
   int *oldarray;
   oldarray = &queueArray;
   int *newArray;
   newArray = new int[newSize];
   for (int i = 0; i < sizeIndex+1; i++)
      {
      if (next_index+i <= size_index)
         {
         newArray[i] = oldArray(next_index+i)
         }
      else if (next_index+i > size_index)
         {
         newArray[i] = //unfinished
         }
      }
   queueArray = &newArray;
   delete [] oldarray;
   size_index = newSize - 1;
   return size_index;
   }
*/
template<class T>
Queue<T>::Queue(int VariableSize)
   {
   queueArray = new T [VariableSize];
   hasContents = new bool[VariableSize];
   next_index  = 0;
   front = 0;
   size_index = VariableSize - 1;
   contains = 0;
   for (int i = 0; i < VariableSize; i++)
      {
      hasContents[i] = false;
      }
   }
template<class T>
Queue<T>::~Queue()
   {
   delete [] queueArray;
   }//
   
template<class T>	
int Queue<T>::enqueue(T numberToEnqueue)
   {
	//if the amount contained equals the size (size index + 1)...
   if (contains == size_index + 1)
      {
      cout << "\nArray is full. Please dequeue a value and try again.\n";
      return 0;
      }
   else if (next_index < size_index)
      {
		cout << next_index << "_";
      queueArray[next_index]  = numberToEnqueue;
      hasContents[next_index] =  true;
		cout << queueArray[next_index] << "\n";
		next_index++;
		contains++;
      }
   else if (next_index == size_index)
      {
		
      if (hasContents[next_index])
         {
         cout << "\nArray error. Value being overwritten. Please check code.\n";
         }
		cout << next_index << "_";
		cout << queueArray[next_index] << "\n";
      queueArray[next_index]  = numberToEnqueue;
      hasContents[next_index] =  true;
		next_index = 0; //reset next_index of array to the front slot
		contains++;
      }
   return contains;
   }

template<class T>
T Queue<T>:: dequeue()
   {
   //always dequeue the next_index  value
   T tempInt;
   cout << "\nFront: " << front << "\n";
   if (empty())
      {
      return -1;
      }
   else
      {
		//if it contains fewer elements than the declared size (size index + 1)
      if (front < size_index)
         {
			cout << queueArray[front] << "\n";
         tempInt = queueArray[front];
         hasContents[front] = false;
			
         front++; //point to the next element as the front
         }
      else //if (front == size_index - 1)
         {
			cout << queueArray[front] << "\n";
         tempInt = queueArray[front];
			
         hasContents[front] = false;
         front = 0;
         }
      }
   contains--;
   return tempInt;
   }

template<class T>	
bool Queue<T>::empty()
   {
   //if queue is empty, return true
   //else, return false
   if (contains == 0)
      {
      cout << "\nQueue empty.\n";
      return true;
      }
   else
      {
      return false;
      }
   }
	
	
//*******************
int main()
{
   Queue<int> newQueue;
   newQueue.empty();
   cout << "Add '1'\n";
   newQueue.enqueue(1);
   newQueue.empty();
  // cout << "Remove '1'\n";
   //cout << "number: " << newQueue.dequeue() << "\n";
   newQueue.empty();
   cout << "Add '2' and '5', then fills the queue (attempting to fill beyond capacity).\n";
   newQueue.enqueue(2);
   newQueue.enqueue(5);
   newQueue.empty();
   for (int i = 0; i < 103; i++)
      {
      newQueue.enqueue(i);
      }
   for (int i = 0; i < 102; i++)
      {
      cout << "number:" << newQueue.dequeue() << "\n";
      }
   newQueue.empty();
   return 0;
}
//*******************
