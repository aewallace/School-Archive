#include "reportT.h"

/******************************************************************/
reportT::reportT()
{
	raw_input = "";
	output = "";
}

reportT::reportT(int sample_count)
{
	samples = new reportlet[sample_count];
	raw_input = "";
	output = "";
}

reportT::~reportT()
{
}

bool reportT::print_report(string filename)
{
	std::string rSTRING;
	ifstream infile;
	infile.open (filename.c_str());
        while(!infile.eof()) // To get you all the lines.
        {
	        getline(infile,rSTRING); // Saves the line in STRING.
	        cout<<rSTRING; // Prints our STRING.
        }
	infile.close();
	return true;
}

bool reportT::grab_report()
{
	read_file();
	
	if (raw_input.length() > 1)
		{
		return false;
		}
	
	int location = raw_input.find("sda ");
	raw_input = raw_input.substr(location);
	
	location = raw_input.find(" ");
	string temp_string = raw_input.substr(0, location);
	char * tempPA_CS;
	tempPA_CS = new char [temp_string.size() + 1];
	strcpy(tempPA_CS, temp_string.c_str());
	
	sec_red_temp = atol(tempPA_CS);
	
	//at this point, our first major value has been copied
	//now to continue to seek the file...
	//get to the second value
	location = raw_input.find(" ");
	raw_input = raw_input.substr(location);
	//get to the third value
	location = raw_input.find(" ");
	raw_input = raw_input.substr(location);
	//get to the fourth value
	location = raw_input.find(" ");
	raw_input = raw_input.substr(location);
	//get to the fifth value
	location = raw_input.find(" ");
	raw_input = raw_input.substr(location);
	//single out the fifth value & convert
	location = raw_input.find(" ");
	raw_input = raw_input.substr(0, location);
	delete [] tempPA_CS;
	tempPA_CS = new char [raw_input.size() + 1];
	strcpy(tempPA_CS, raw_input.c_str());
	//write second value;
	sec_writ_temp = atol(tempPA_CS);
	
	return true;
}

bool reportT::build_report(configuration config)
{
	config.pass_params(blk_read, blk_read_s, kb_read, blk_write, blk_write_s, kb_write);
	output = "";
	
	for(int i = 0; i < config.get_count(); i++)
	{
		if (i % 10 == 0)
			{
			if(blk_read)
				output += " blocks read ::";
			if(blk_read_s)
				output += " blocks read/s ::";
			if(kb_read)
				output += " KB read ::";
			if(blk_write)
				output += " blocks written ::";
			if(blk_write_s)
				output += " blocks written/s ::";
			if(kb_write)
				output += " kb_write \n";
			}
		
		grab_report();
		
		if(blk_read){
			output += " ";
			output += longtostr(samples[i].sectors_read);
			output += "::";}
		if(blk_read_s){
			output += " ";
			output += longtostr(samples[i].sectors_read_s);
			output += "::";}
		if(kb_read){
			output += " ";
			output += longtostr(samples[i].kb_read);
			output += "::";}
		if(blk_write){
			output += " ";
			output += longtostr(samples[i].sectors_written);
			output += "::";}
		if(blk_write_s){
			output += " ";
			output += longtostr(samples[i].sectors_written_s);
			output += "::";}
		if(kb_write){
			output += " ";
			output += longtostr(samples[i].kb_written);
			output += "::";}
	}
	
	return true;

}

/*
 Code ripped from the internet, modified to fit
 */
bool reportT::read_file()
{
	ifstream infile;
	bool sda_not_found = true;
	infile.open ("/proc/diskstats");
        while(sda_not_found && !infile.eof()) // To get you all the lines.
        {
	        getline(infile,raw_input); // Saves the line in STRING.
	        //cout<<STRING; // Prints our STRING.
			  if (string::npos != raw_input.find("sda "))
			  	{
				sda_not_found = false;
				}
        }
	infile.close();
	
	if (sda_not_found)
		{
		raw_input = "";
		}
	
	#ifdef DEBUG
	cout << raw_input;
	#endif
	
	return true;
}


//this also stolen from the internet
bool reportT::write_file(string filename)
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




//also via the internet
string longtostr(long number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}