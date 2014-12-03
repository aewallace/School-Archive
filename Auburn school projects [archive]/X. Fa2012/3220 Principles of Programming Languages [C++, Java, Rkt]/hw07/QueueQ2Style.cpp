/*
 *Abstract data type "Queue"
 *
 *Uses dynamic arrays.
 */

#include <iostream>
using namespace std;

template <class T>
class Queue {

   private:
      <T> *queueArray;
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
      int dequeue();
      bool empty(); 
      
}; //end class declaration


template<class T>
Queue::Queue()
   {
   queueArray = new T[100];
   hasContents = new bool[100];
   next_index  = 0;
   front = 0;
   size_index = 99;
   contains = 0;
   for (int i = 0; i < 100; i++)
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
template<typename TYPE>
Queue<T>::Queue(int VariableSize)
   {
   queueArray = new type[VariableSize];
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
template<typename TYPE>
Queue::~Queue()
   {
   delete [] queueArray;
   }//
   
template<typename TYPE>	
int Queue::enqueue(int numberToEnqueue)
   {
   if (contains == size_index+1)
      {
      cout << "\nArray is full. Please dequeue a value and try again.\n";
      return -1;
      }
   else if (contains < size_index+1 && next_index  < size_index)
      {
      
      queueArray[next_index]  = numberToEnqueue;
      hasContents[next_index] =  true;
		cout << queueArray[next_index] << "\n";
		next_index++;
      }
   else if (contains < size_index+1 && next_index  == size_index)
      {
        if (hasContents[next_index])
         {
         cout << "\nArray error. Value being overwritten. Please check code.\n";
         }
		cout << queueArray[next_index] << "\n";
      queueArray[next_index]  = numberToEnqueue;
      hasContents[next_index] =  true;
		next_index = 0; //reset to next_index of array

      }
   contains++;
   return contains;
   }

template<typename TYPE>
int Queue::dequeue()
   {
   //always dequeue the next_index  value
   int tempInt;
   
   if (empty())
      {
      return -1;
      }
   else
      {
      if (contains < size_index+1 && front < size_index)
         {
         tempInt = queueArray[front];
         hasContents[front] = false;
			cout << queueArray[front] << "\n";
         front++; //point to the next element as the front
         }
      else if (contains < size_index+1 && front == size_index)
         {
         tempInt = queueArray[front];
			cout << queueArray[front] << "\n";
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
   cout << "Remove '1'\n";
   cout << "number: " << newQueue.dequeue() << "\n";
   newQueue.empty();
   cout << "Add '2' and '5'\n";
   newQueue.enqueue(2);
   newQueue.enqueue(5);
   newQueue.empty();
   for (int i = 0; i < 102; i++)
      {
      newQueue.enqueue(i);
      }
   for (int i = 0; i < 100; i++)
      {
      cout << "number:" << newQueue.dequeue() << "\n";
      }
   newQueue.empty();
   return 0;
}
//*******************
