#include "console.h"
using namespace std;

int main()
{	
	heap *h = new heap(q, SIZE, 0);
	h->buildheap();
	console *con = new console(h);
	
	con->run();
}
