#include "heap.h"

/* isLeaf(), leftChild(), rightChild(), parent()*/

int main()
{
	ELEM *q = (ELEM *)malloc(sizeof(ELEM));
	
	heap *h = new heap(q, SIZE, 0);

	h->enqueue(0, 16);
	h->enqueue(1, 14);
	h->enqueue(2, 10);
	h->enqueue(3, 8);
	h->enqueue(4, 7);
	h->enqueue(5, 9);
	h->enqueue(6, 3);
	h->enqueue(7, 2);
	h->enqueue(8, 4);
	h->enqueue(9, 1);
	
	// isLeaf()
	cout << "isLeaf()" <<endl;
	cout<<h->isLeaf(5)<<endl; // return true, which is 1 in integer type
	cout<<h->isLeaf(9)<<endl; // return true, which is 1 in integer type
	cout<<h->isLeaf(4)<<endl; // return false, which is 0 in integer type
	cout<<h->isLeaf(0)<<endl; // return false, which is 0 in integer type

	//leftChild()
	cout << "leftChild()" <<endl;
	cout<<h->leftChild(0)<<endl; // return 1
	cout<<h->leftChild(1)<<endl; // return 3
	cout<<h->leftChild(4)<<endl; // return 9
	cout<<h->leftChild(5)<<endl; // return -1	

	//rightChild()
	cout << "rightChild()" <<endl;
	cout<<h->rightChild(0)<<endl; // return 2
	cout<<h->rightChild(1)<<endl; // return 4
	cout<<h->rightChild(2)<<endl; // return 6
	cout<<h->rightChild(5)<<endl; // return -1	

	//parent()
	cout << "parent()" <<endl;
	cout<<h->parent(0)<<endl; // return -1
	cout<<h->parent(1)<<endl; // return 0
	cout<<h->parent(4)<<endl; // return 1
	cout<<h->parent(9)<<endl; // return 4			




	free(q);
	q = NULL;
}
