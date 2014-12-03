#include "heap.h"

/* removemax()*/

int main()
{
	ELEM *q = (ELEM *)malloc(sizeof(ELEM));
	
	heap *h = new heap(q, SIZE, 0);

	h->enqueue(2, 10);
	h->enqueue(1, 14);
	h->enqueue(3, 8);
	h->enqueue(0, 16);



	cout<<h->removemax().Object_ID<<endl; // return the object with current max priority which is 0
	cout<<h->removemax().Object_ID<<endl; // return the object with current max priority which is 1
	cout<<h->removemax().Object_ID<<endl; // return the object with current max priority which is 2
	cout<<h->removemax().Object_ID<<endl; // return the object with current max priority which is 3
	cout<<h->removemax().Object_ID<<endl; // the heap is empty, return -1


	free(q);
	q = NULL;
}
