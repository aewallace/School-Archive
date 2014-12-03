#include <iostream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include "heap.h"
#define MAX_LINE 255
#define SMALL 20
#define PROMPT "Priority Queue>"

//#define _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES 1

using namespace std;

struct cmd { /* struct for commands */
   string name;    /* name of command */
   string help;    /* descriptive help string */
};

class console{
private:
	heap *Heap;
	//std::array<cmd,6> command_list;
	int commandlist_size;
	cmd command_list [6];

public:

	console(heap *h);
	~console();


	int cmd_enqueue(char *param);
	int cmd_dequeue(char *param);
	int cmd_change_weight(char *param);

	int cmd_show(char *param);
	int cmd_help(char *param);
	int cmd_quit(char *param);
	char *cmd_read_line(char *buffer,int size);
	int cmd_parse_line(char *buffer);
	int run();
	

};

/* table of commands 
cmd command_list[]={ 
	{"enqueue","Enqueue an element with object_ID and priority, e.g. enqueue 1 12"},
	{"dequeue","Dequeue the element with highest priority, e.g. dequeue"},
	{"change weight","Change the weight of existing element in the heap with Object_ID and new priority, e.g. change weight 1 12"},
	{"show","Prints out the heap in the format of an array"},
	{"help","Prints out available commands"},
	{"quit","Exit program"}
};

*/



console::console(heap *h)
{
	this->Heap = h;
	commandlist_size = 6;

	this->command_list[0].name = "enqueue";
	this->command_list[0].help = "Enqueue an element with object_ID and priority, e.g. enqueue 1 12";

	this->command_list[1].name = "dequeue";
	this->command_list[1].help = "Dequeue the element with highest priority, e.g. dequeue";

	this->command_list[2].name = "changeweight";
	this->command_list[2].help = "Change the weight of existing element in the heap with Object_ID and new priority, e.g. change weight 1 12";

	this->command_list[3].name = "show";
	this->command_list[3].help ="Prints out the heap in the format of an array";

	this->command_list[4].name = "help";
	this->command_list[4].help = "Prints out available commands";

	this->command_list[5].name = "quit";
	this->command_list[5].help = "Exit program";

}


console::~console()
{
	this->Heap = NULL;
}



/*Enqueue an element */
int console::cmd_enqueue(char *param)
{
	//printf("enqueue!\n");

	while(*param!='\0'&&*param!=' ')
	{
		param++;		
	}
	if(*param=='\0')
	{
		fprintf(stderr,"Error: Lack of parameters. e.g. enqueue 1 12\n");
		return(1);
	}
	++param;
	char first[20]="";
	char *p = first;
	
	while(*param!='\0'&&*param!=' ')
	{
		*p = *param;
		p++;
		param++;		
	}
	if(*param=='\0')
	{
		fprintf(stderr,"Error: Lack of parameters. e.g. enqueue 1 12\n");
		return(1);
	}
	*p = '\0';
	//printf("first	%d	%lu\n", atoi(first), strlen(first));
	++param;
	char second[20]="";
	char *q = second;
	while(*param!='\0')
	{
		*q = *param;
		q++;
		param++;		
	}
	*q = '\0';
	//printf("second	%d	%lu	\n", atoi(second), strlen(second));
	if(atoi(first)<0 || atoi(second)<0)
	{
		fprintf(stderr,"Error: both of object_ID and priority should be larger than 0\n");
		return(1);
	}
	Heap->enqueue(atoi(first), atoi(second));

	return(1);
}

/*Dequeue the element with highest priority*/
int console::cmd_dequeue(char *param)
{
	//printf("dequeue!\n");
	int ID = Heap->dequeue();
	if(ID!=-1)
		cout << "Removed Object ID : "<<ID<<endl;
	return(1);
}

/*Change the weight of existing element in the heap */
int console::cmd_change_weight(char *param)
{
	//printf("change weight!\n");
	
	while(*param!='\0'&&*param!=' ')
	{
		param++;		
	}
	if(*param=='\0')
	{
		fprintf(stderr,"Error: Lack of parameters. e.g. changeweight 1 12\n");
		return(1);
	}

	param++;	
	char first[20]="";
	char *p = first;
	
	while(*param!='\0'&&*param!=' ')
	{
		*p = *param;
		p++;
		param++;		
	}
	if(*param=='\0')
	{
		fprintf(stderr,"Error: Lack of parameters. e.g. changeweight 1 12\n");
		return(1);
	}
	*p = '\0';
	//printf("first	%d	%lu\n", atoi(first), strlen(first));
	++param;
	char second[20]="";
	char *q = second;
	while(*param!='\0')
	{
		*q = *param;
		q++;
		param++;		
	}
	*q = '\0';
	//printf("second	%d	%lu	\n", atoi(second), strlen(second));
	if(atoi(first)<0 || atoi(second)<0)
	{
		fprintf(stderr,"Error: both of object_ID and priority should be larger than 0\n");
		return(1);
	}

	Heap->changeWeight(atoi(first), atoi(second));
	return(1);
}


/*Show the heap in the format of an array*/
int console::cmd_show(char *param)
{
	Heap->display();
	//Heap->displayALL();
	//Heap->displayALL();
	return(1);
}


/*help: show the command list*/
int console::cmd_help(char *param)
{
	int i=0; /* traversal variable for command table */

	for (int i=0; i < commandlist_size; i++) 
	{
		if(i!=2)
			cout<<command_list[i].name <<"			"<<command_list[i].help<<endl;
		else
			cout << command_list[i].name<<"		"<<command_list[i].help<<endl;
	}
	return(1); 
}



/*'quit' - returns 0 and exit */
int console::cmd_quit(char *param) 
{
	return(0);
}

/* read command from user, translate aliases if any, return fgets status */
char *console::cmd_read_line(char *buffer,int size)
{
	char *result;

	printf("%s",PROMPT);
	/* force prompt to print, waits here*/
	fflush(stdout);                      
	if (result=fgets(buffer,size,stdin)) 
	{
		/* delete final CR */
		buffer[strlen(buffer)-1]='\0';
		/* translate aliases */    
		if (!strcmp(buffer,"?"))           
			strcpy(buffer,"help");
		if (!strcmp(buffer,"exit"))
			strcpy(buffer,"quit");
		if (!strcmp(buffer,"q"))
			strcpy(buffer,"quit");
	}
	return (result);
}

/* parse input command line */
int console::cmd_parse_line(char *buffer)
{
	/* default return status */
	int result=1; 
	/* length of parsed command */
	int len; 
	/* traversal variable for command table */
	int i; 
	/* check for shell escape */
	if (*buffer=='!') 
		system((strlen(buffer)>1)?buffer+1:getenv("SHELL"));
	else
	{
		/* walk command table */
	      	for (i=0; i< commandlist_size; i++) 
		{
			//cout<<"	i	" <<i <<"	"<<command_list[i].name<<endl;
			if (strncmp(command_list[i].name.c_str(), buffer, len=command_list[i].name.size())==0)
			{ 	
				/* if command matches... */
				//printf("i	%d\n", i);
				switch(i)
				{
					case 0: result = cmd_enqueue(buffer); break;
					case 1: result = cmd_dequeue(buffer); break;
					case 2: result = cmd_change_weight(buffer); break;
					case 3: result = cmd_show(buffer); break;
					case 4: result = cmd_help(buffer); break;
					case 5: result = cmd_quit(buffer); break;
					default: break;
				}
				break; /* call function and pass remainder of line as parameter */
			}
		}
		/* if no commands were called... */
		if (i == commandlist_size) 
			printf("The command is not available, please try again.\n"); /* tribute to Canadian diction */
	}
	/* return 1 unless exit requested, then return 0 */
	return(result); 
}


int console::run()
{

	char buffer[MAX_LINE+1]="";
	/*read command line and parse it*/
	while (cmd_read_line(buffer,MAX_LINE) && cmd_parse_line(buffer))
        	;


	return 0;
}


