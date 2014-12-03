/*
	object ID should be larger than 0, an interger
	object_ID is the position in the array, starting fro 0, instead of 1
*/
#include <iostream>
#include <array>
#include "stdio.h"
#include "stdbool.h"


#define SIZE 5
using namespace std;


/*
	object is the basic element for storing basic information, Object_ID, priority, index are all zero-based
	index stands for the logical location for the Object in the heap, while the Object_ID indicates the physical location in the ELEM array

*/
typedef struct{
	int Object_ID; // physical
	int priority;
	int index; // logical 
}Object;

/*ELEM is an array, storing each object physically*/
typedef struct{
	array<Object, SIZE> heapArray;
}ELEM;

class heap{
private:
	ELEM *Heap;
	int size;
	int n;
	void siftdown(int position);
	
public:

	heap(ELEM *ele, int size, int n);
	~heap();
	int heapsize() const;
	bool isLeaf(int Object_ID) const;
	int leftChild(int Object_ID) const;
	int rightChild(int Object_ID) const;	
	int parent(int Object_ID) const;
	
	Object getObject(int index) const;/*get Object by index*/
	Object getObjectByID(int ID) const;/*get Object by Object_ID*/
	int getIndex(int Object_ID) const;/*get index by Object_ID*/
	int getID(int index) const;/*get Object_ID by index*/

	void insert(const Object obj);
	Object remove(int position);
	Object removemax();

	void heap_increase_key(int position, int priority);

	void buildheap();
	void display();/*display heap in the order of the logic*/
	void displayALL();/*display all element in the array physically*/
/**/
	/*enqueue an element*/
	void enqueue(int Object_ID, int priority);
	/*dequeue an element*/
	int dequeue();
	/*change the weight of an existing object*/
	void changeWeight(int Object_ID, int new_priority);

};

/*constructor*/
heap::heap(ELEM *ele, int size, int n)
{
	/*Initiate all the object in the ELEM, change the value of index to -1, which represents this current object is not existhing in the heap*/
	int i = 0;
	for(i=1;i<size;i++)
	{
		if(ele->heapArray[i].Object_ID == 0)
			ele->heapArray[i].index = -1;
	}

	this->Heap = ele;
	this->size = size;
	this->n = n;
}

heap::~heap()
{
	this->Heap = NULL;
	this->size = 0;
	this->n = 0;
}

int heap::getIndex(int Object_ID) const
{
	return this->Heap->heapArray[Object_ID].index;
}
int heap::getID(int index1) const
{
	int i = 0;
	for(;i< this->size;i++)
	{
		if(this->Heap->heapArray[i].index == index1)
			break;
	}	
	return this->Heap->heapArray[i].Object_ID;
}


Object heap::getObject(int index) const
{
	return this->Heap->heapArray[this->getID(index)];
}

Object heap::getObjectByID(int ID) const
{
	return this->Heap->heapArray[ID];
}

/*return heap size*/
int heap::heapsize() const
{
	return this->n;
}
/*judge whether input object is a leaf or not*/
bool heap::isLeaf(int Object_ID) const
{
	if((this->getIndex(Object_ID)+1) > (this->n)/2)
		return true;
	else
		return false;
}
/*return logical index of left child of input object*/
int heap::leftChild(int Object_ID) const
{
	if(2*this->getIndex(Object_ID)+1 < this->n)
		return 2*this->getIndex(Object_ID)+1;
	else	
		return -1;
}

/*return logical index of right child of input object*/
int heap::rightChild(int Object_ID) const
{
	if(2*this->getIndex(Object_ID)+2 < this->n)
		return 2*this->getIndex(Object_ID)+2;
	else	
		return -1;
}
/*return logical index of parent of input object*/
int heap::parent(int Object_ID) const
{
	if((this->getIndex(Object_ID)+1)/2 > 0)
		return (this->getIndex(Object_ID)+1)/2 - 1;
	else
		return 0;
}

/*max-heapify algorithm*/
void heap::siftdown(int position_logic)
{
	Object current = getObject(position_logic);
	Object l, r;
	if(leftChild(this->getID(position_logic))!=-1)
		l = getObject(leftChild(this->getID(position_logic)));
	if(rightChild(this->getID(position_logic))!=-1)
		r = getObject(rightChild(this->getID(position_logic)));	
	int largest = position_logic;

	if(leftChild(this->getID(position_logic))!=-1)
	{
		if(l.priority > current.priority)
			largest = l.index;
		else
			largest = current.index;
	}
	if(rightChild(this->getID(position_logic))!=-1)
	{
		if(r.priority > getObject(largest).priority )
			largest = r.index;
	}

	if(largest != position_logic)
	{	
		int ID1 = getID(position_logic), ID2 =  getID(largest);	
		this->Heap->heapArray[ID2].index = position_logic;
		this->Heap->heapArray[ID1].index = largest;
		siftdown(largest);
	}
}
/*build the heap*/
void heap::buildheap()
{
	if(this->n<=2)
		return;
	int i = 0;
	for(i =  this->n/2-1; i>=0; i--)
	{
		this->siftdown(i);
	}
}
/*remove the object with highest priority*/
Object heap::removemax()
{
	Object temp;
	if(this->n<1)
	{
		cout << "Error: Empty Heap" <<endl;		
		temp.Object_ID = -1;
		return temp;
	}
	temp = getObject(0);
	int ID1 = getID(0), ID2 = getID(this->n-1);
	if(this->n-1 != 0)
	{
		this->Heap->heapArray[ID1].index = -1;
		this->Heap->heapArray[ID2].index = 0;
	}
	else
	{
		this->Heap->heapArray[ID2].index = -1;
	}
	this->n --;
	this->siftdown(0);
	return temp;	
}

Object heap::remove(int position) // position is logical position, which is index
{
	Object temp;
	if(this->n<position+1)
	{
		cout << "Error: Empty Heap" <<endl;		
		temp.Object_ID = -1;
		return temp;
	}
	temp = getObject(position);
	int ID1 = getID(position), ID2 = getID(this->n-1);
	this->Heap->heapArray[ID1].index = -1;
	this->Heap->heapArray[ID2].index = position;
	this->n --;
	this->siftdown(position);
	return temp;
}

/*insert an object to the heap*/
void heap::insert(const Object obj)
{
	this->Heap->heapArray[obj.Object_ID].Object_ID = obj.Object_ID;
	this->n = this->n+1;
	this->Heap->heapArray[obj.Object_ID].index = this->n-1;
	this->Heap->heapArray[obj.Object_ID].priority = -1;
	this->heap_increase_key(this->n-1, obj.priority);
}

void heap::display()
{
	int i = 0;
	cout <<"Object ID	"<<"priority"<<endl;
	for(;i<this->n;i++)
	{
		Object current = getObject(i);
		cout <<current.Object_ID<<"		"<< current.priority<<endl;
	}
}

void heap::displayALL()
{
	int i = 0;
	for(;i<this->size;i++)
	{
		Object current = getObjectByID(i);
		cout << "heap test " << current.Object_ID <<"  "<< current.priority <<"   "<< current.index <<endl;
	}
}
/*modify the priority of an existing object*/
void heap::heap_increase_key(int position, int priority)
{
	/*if equal, nothing should be done*/
	if(getObject(position).priority == priority)
	{
		return;
	}
	/*if new priority is less than previous one, we just make sure the max-heap attribute is maintained below this object*/
	else if(getObject(position).priority > priority)
	{
		this->Heap->heapArray[getID(position)].priority = priority;
		siftdown(position);
	}
	/*if new priority is larger than previous one, we have to maintain the max-heap attribute of all objects above this object*/
	else 
	{
		this->Heap->heapArray[getID(position)].priority = priority;
		while(position>0&& getObject(parent(getID(position))).priority < getObject(position).priority)
		{
			int ID1 = getID(position), ID2 = getID(parent(getID(position))), p = parent(getID(position));
			this->Heap->heapArray[ID1].index = p;
			this->Heap->heapArray[ID2].index = position;
			position = p;
		}
	}	
}


void heap::enqueue(int Object_ID, int priority)
{
	if(Object_ID>this->size-1)
	{
		cout << "Error: Full Heap" <<endl;
		return;
	}
	if(this->Heap->heapArray[Object_ID].index != -1)
	{
		cout << "Error: Object Exists" <<endl;
		return;
	}
	Object temp;
	temp.Object_ID = Object_ID;
	temp.priority = priority;
	temp.index = -1;
	this->insert(temp);
}
int heap::dequeue()
{
	Object temp = removemax();
	if(temp.Object_ID == -1)
	{
		return -1;
	}
	return temp.Object_ID;
}

void heap::changeWeight(int Object_ID, int new_priority)
{
	if(getIndex(Object_ID) == -1)
	{
		cout << "Error: Doesn't exist" <<endl;
		return;
	}
	heap_increase_key(getIndex(Object_ID), new_priority);
}



