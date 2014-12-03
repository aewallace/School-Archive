#include "heap.h"

/* heapsize()*/

int main()
{
	ELEM *q = (ELEM *)malloc(sizeof(ELEM));

	heap *h = new heap(q, SIZE, 0);

	cout<<h->heapsize()<<endl;//return 0

	h->enqueue(0, 1);
	cout<<h->heapsize()<<endl;//return 1

	h->enqueue(1, 1);
	cout<<h->heapsize()<<endl;//return 2

	h->enqueue(2, 2);
	cout<<h->heapsize()<<endl;//return 3

	h->enqueue(3, 3);
	cout<<h->heapsize()<<endl;//return 4

	h->enqueue(4, 3);
	cout<<h->heapsize()<<endl;//return 5
	
	h->dequeue();
	cout<<h->heapsize()<<endl;//return 4

	free(q);
	q = NULL;
}
