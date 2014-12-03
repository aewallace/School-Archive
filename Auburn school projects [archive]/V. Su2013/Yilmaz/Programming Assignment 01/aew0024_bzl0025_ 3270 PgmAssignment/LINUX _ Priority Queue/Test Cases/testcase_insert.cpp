#include "heap.h"

/* insert()*/

int main()
{
	ELEM *q = (ELEM *)malloc(sizeof(ELEM));

	heap *h = new heap(q, SIZE, 0);

	Object temp, temp1, temp2;
	temp.Object_ID = 0;
	temp.priority = 1;
	temp.index = -1;
	h->insert(temp);
	h->display();
/*
	Display as below:

	Object ID	priority
	0		1
*/


	temp1.Object_ID = 1;
	temp1.priority = 2;
	temp1.index = -1;
	h->insert(temp1);
	h->display();
/*
	Display as below:

	Object ID	priority
	1		2
	0		1
*/


	temp2.Object_ID = 2;
	temp2.priority = 10;
	temp2.index = -1;
	h->insert(temp2);
	h->display();
/*
	Display as below:

	Object ID	priority
	2		10
	0		1
	1		2
*/


	free(q);
	q = NULL;
}
