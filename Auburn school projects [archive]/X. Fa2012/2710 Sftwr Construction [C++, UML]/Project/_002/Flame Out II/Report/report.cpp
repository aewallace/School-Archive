#include <iostream>
#include <fstream>
#include <string>
using namespace std;


//only deals with the primary disk drive in the system, as reported by diskstat

class report{
public:
	report();
	~report();
	bool print_report();
	bool grab_report();
	bool build_report();
	bool read_file();
private:
	reportlet* samples;
	bool blk_read;
	bool blk_read_s; 
	bool kb_read;
	bool blk_write;
	bool blk_write_s;
	bool kb_write;
	string output;
	string raw_input;
	long sec_red_temp;
	long sec_writ_temp;

};

//stores one diskstat sample
struct reportlet{

	long sectors_read;
	long sectors_written;
	long kb_read;
	long kb_written;
	long kb_read_s;
	long kb_written_s;
	//fields 1 (reads, where 1 read = 1 sector), 5 (writes, where 1 write = 1 sector), 
	// and calculate from that based on deltas in time (for /s)
	// or(and) 1 sector or block being 1 KB
};

report::report()
{
	raw_input = "";
	output = "";
}

report::report(int sample_count)
{
	samples = new reportlet[sample_count];
	raw_input = "";
	output = "";
}

report::~report()
{
}

bool report::print_report(string filename)
{
	std::string rSTRING;
	ifstream infile;
	infile.open (filename.c_str());
        while(!infile.eof) // To get you all the lines.
        {
	        getline(infile,rSTRING); // Saves the line in STRING.
	        cout<<rSTRING; // Prints our STRING.
        }
	infile.close();
}

bool report::grab_report()
{
	read_file();
	
	int location = raw_input.find("sda ");
	raw_input = raw_input.substring(location);
	
	location = raw_input.find(" ");
	string temp_string = raw_input.substring(0, location);
	char * tempPA_CS;
	tempPA_CS = new char [temp_string.size() + 1];
	strcpy(tempPA_CS, temp_string.c_str());
	
	sec_red_temp = atol(tempPA_CS);
	
	//at this point, our first major value has been copied
	//now to continue to seek the file...
	//get to the second value
	location = raw_input.find(" ");
	raw_input = raw_input.substring(location);
	//get to the third value
	location = raw_input.find(" ");
	raw_input = raw_input.substring(location);
	//get to the fourth value
	location = raw_input.find(" ");
	raw_input = raw_input.substring(location);
	//get to the fifth value
	location = raw_input.find(" ");
	raw_input = raw_input.substring(location);
	//single out the fifth value & convert
	location = raw_input.find(" ");
	raw_input = raw_input.substring(0, location);
	delete [] tempPA_CS;
	tempPA_CS = new char [raw_input.size() + 1];
	strcpy(tempPA_CS, raw_input.c_str());
	//write second value;
	sec_writ_temp = atol(tempPA_CS);
	
}

bool report::build_report(configuration config)
{
	config.pass_params(blk_read, blk_read_s, kb_read, blk_write, blk_write_s, kb_write);
	output = "";
	
	for(int i = 0; i < config.get_count(); i++)
	{
		if (i % 10 == 0)
			{
			if(blk_read)
				output += " blocks read" << "::";
			if(blk_read_s)
				output += " blocks read/s" << "::";
			if(kb_read)
				output += " KB read" << "::";
			if(blk_write)
				output += " blocks written" << "::";
			if(blk_write_s)
				output += " blocks written/s" << "::";
			if(kb_write)
				output += " kb_write" << "\n";
			}
		
		grab_report();
		
		if(blk_read)
			output += " " << samples[i].sectors_read << "::";
		if(blk_read_s)
			output += " " << samples[i].sectors_read_s << "::";
		if(kb_read)
			output += " " << samples[i].kb_read << "::";
		if(blk_write)
			output += " " << samples[i].sectors_written << "::";
		if(blk_write_s)
			output += " " << samples[i].sectors_written_s << "::";
		if(kb_write)
			output += " " << samples[i].kb_written << "\n";
	}
	
	

}

/*
 Code ripped from the internet, modified to fit
 */
bool report::read_file()
{
	ifstream infile;
	string diskstats = "/proc/diskstats";
	infile.open (diskstats.c_str());
        while(!infile.eof) // To get you all the lines.
        {
	        getline(infile,raw_input); // Saves the line in STRING.
	        //cout<<STRING; // Prints our STRING.
        }
	infile.close();
}


//this also stolen from the internet
bool report::write_file(string filename)
{
	ofstream myfile (filename.c_str());
  if (myfile.is_open())
  {
    myfile << output;
    myfile.close();
  }
  else cout << "Unable to open file";
  return 0;
}