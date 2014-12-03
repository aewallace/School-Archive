#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;
//this is the clock replacement policy


int main(int argc, char * argv[])/*num_frames num_pages input.dat output.opt*/
{
	//just make note of whether or not there are empty slots
	bool empty_frame_exists = false;
	//count the number of slots empty
	int num_empty_frames = 0;
	//the total number of memory frames available
	int total_frames_to_make_available = 0;
	int total_frames_to_count = 0;

	/*must indicate the random number that was being stored at the time of a page fault,
	  and also keep track of the total number of page faults*/
	int total_faults = 0;
	//int curr_RN = -1; //declared and used later
	

	/*so as we record the numbers from input.dat (or any other file),
	  we must check to see if a number has been written already (speed doesn't matter)
	  and if it has, (1) do not re-write; (2) make note of which RN (maybe in an array or a string)
	  and (3) make sure you increase the count of total faults by one.
	  everything may be written out at the end.*/
	/*as such, we need an array to represent all the possible frames (of variable size)
	  an array to hold all the numbers that caused the fault/weren't found in the list (of the same variable size)
	  and a counter (which we have) for the total number of faults.*/
	int * virtual_frames;
	int * virtual_frames_used_recently;
	int pages_used = 0;
	int * faults_due_to_these;

	if ( argc != 5 ) // argc should be 5 for correct execution
    		{// We print argv[0] assuming it is the program name
   		cout<<"usage: "<< argv[0] <<" <num_frames> <num_pages> <input file name> <output file name>\n";
		}
	else if ((8 * atoi(argv[1]/*.c_str()*/)) > (atoi(argv[2]/*.c_str()*/)) )
		{
		cout << "Page range is not at least 8x number of frames\n";
		}
	
 	else
	{
	virtual_frames = new int[atoi(argv[1]/*.c_str()*/)];
	virtual_frames_used_recently = new int[atoi(argv[1]/*.c_str()*/)];
	int pointer_points_at = -1;
	bool actually_perform = false;
    	
	for (int i = 0; i < 2; i++)
	{	
		string line;
		if(!actually_perform)
		{
			// We assume argv[3] is a filename to open
    			ifstream the_file ( argv[3] );
   	 		// Always check to see if file opening succeeded
    			if ( !the_file.is_open() )
     	  			cout<<"Could not open file; maybe invalid file name. Please try again.\n";
    			else // if (the_file.is_open())
  			{
				//set up the page fault'd array
    				while ( the_file.good() )
    				{
      					getline (the_file,line);
					total_frames_to_count++;
    				}
    				the_file.close();
				faults_due_to_these = new int[total_frames_to_count];
				actually_perform = true;
  			}
			
  		}
		else //if(actually_perform)
		{
			// We assume argv[3] is a filename to open
    			ifstream the_file ( argv[3] );
   	 		// Always check to see if file opening succeeded
    			if ( !the_file.is_open() )
     	  			cout<<"Could not open file; maybe invalid file name. Please try again.\n";
    			else // if (the_file.is_open())
  			{
				line = "";
				int last_page_hit_index = -1;
				int curr_RN = -1;
    				for (int j = 0; j < total_frames_to_count || the_file.good(); j++)
    				{
      					getline (the_file,line);
					int curr_RN = atoi(line.c_str());
					bool does_exist = false;
					for (int k = 0; k < pages_used && does_exist == false; k++)
						{
						if (curr_RN == virtual_frames[k])
							{
							does_exist = true;
							last_page_hit_index = k;
							}
						}
					if (does_exist)
					{
						//actually no fault; mark it as used recently and move on
						virtual_frames_used_recently[last_page_hit_index]++;
					}
					else //(if current number does not exist)
					{
						//write to fault'd list
						faults_due_to_these[total_faults] = curr_RN;
						//increase count of faults
						total_faults++;
						//store in a decent spot, moving ahead from current index of last stored
						//how do circular queue?
						int cycle = 0;
						int temp_itr = pointer_points_at;
						while (cycle < 1)
							{
							if (virtual_frames_used_recently[temp_itr] == 0)
							{
							virtual_frames[temp_itr] = curr_RN;
							virtual_frames_used_recently[temp_itr]++;
							pointer_points_at = temp_itr;
							}
							if (virtual_frames_used_recently[temp_itr] != 0)
							{
							virtual_frames_used_recently[temp_itr] = 0;
							}
							if (temp_itr == pages_used)
								temp_itr = 0;
							if (temp_itr == pointer_points_at)
								cycle++;
							}
					
					}
    				}
    				the_file.close();
  			}
  		}
	}
	
	//now, write the contents out....
	
	ofstream myfile;
  myfile.open (argv[4]);
  for (int q = 0; q < total_faults; q++)
	{
	myfile << faults_due_to_these[q];
	myfile << "\n";
	}
	myfile << "Total page faults: ";
	myfile << total_faults;
	myfile << "\n";
  myfile.close();
	}

	
	

    return 0;
}
