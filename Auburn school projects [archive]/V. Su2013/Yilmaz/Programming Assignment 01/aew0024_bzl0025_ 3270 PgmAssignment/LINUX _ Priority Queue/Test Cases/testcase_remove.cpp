#include "heap.h"

/* remove()*/

int main()
{
	ELEM *q = (ELEM *)malloc(sizeof(ELEM));
	Object a, b, c, d, e, a1, b1, c1, d1, e1;
	a.Object_ID = 0;
	a.priority = 4;
	a.index = 0;
	b.Object_ID = 1;
	b.priority = 1;
	b.index = 1;
	c.Object_ID = 2;
	c.priority = 3;
	c.index = 2;
	d.Object_ID = 3;
	d.priority = 2;
	d.index = 3;
	e.Object_ID = 4;
	e.priority = 16;
	e.index = 4;

	a1.Object_ID = 5;
	a1.priority = 9;
	a1.index = 5;
	b1.Object_ID = 6;
	b1.priority = 10;
	b1.index = 6;
	c1.Object_ID = 7;
	c1.priority = 14;
	c1.index = 7;
	d1.Object_ID = 8;
	d1.priority = 8;
	d1.index = 8;
	e1.Object_ID = 9;
	e1.priority = 7;
	e1.index = 9;
		
	q->heapArray[0] = a;
	q->heapArray[1] = b;
	q->heapArray[2] = c;
	q->heapArray[3] = d;
	q->heapArray[4] = e;
	q->heapArray[5] = a1;
	q->heapArray[6] = b1;
	q->heapArray[7] = c1;
	q->heapArray[8] = d1;
	q->heapArray[9] = e1;



	heap *h = new heap(q, SIZE, 10);
	h->buildheap();
	h->display();
/*
	Display as below:

	Object ID	priority
	4		16
	7		14
	6		10
	8		8
	9		7
	5		9
	2		3
	3		2
	0		4
	1		1
*/

	h->remove(5); // 5 is the logical index in the heap, instead of physical position
	h->display();
/*
	Display as below:

	Object ID	priority
	4		16
	7		14
	6		10
	8		8
	9		7
	1		1
	2		3
	3		2
	0		4
*/	

	free(q);
	q = NULL;
}
