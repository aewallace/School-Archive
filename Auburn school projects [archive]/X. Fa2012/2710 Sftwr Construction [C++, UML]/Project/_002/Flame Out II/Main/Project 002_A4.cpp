
#include <iostream>
#include <map>
#include <fstream>
#include <string>
using namespace std;

enum OP_TYPE_t {null_opr, help, run, set, print, save, exit_t};
enum FLAG_t {null_flag, report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {p0 = 0, p1 = 1, null_arg, filename, value};

class commandline{
public:
	commandline();
	~commandline();
	void parse_input_cmd();
	void map_type(string type_in);
	void map_flag(string flag_in);
	void map_arg_three(string arg_in);
	void welcome_message();
	const OP_TYPE_t get_curr_opr();
	const FLAG_t get_curr_flag();
	const ARG3_PURPOSE_t get_curr_arg3_purpose();
	const string get_arg3_string();
	std::string filename_worker;

private:
	OP_TYPE_t current_opr;
	FLAG_t current_flag;
	ARG3_PURPOSE_t argument3_purpose;
	std::string current_arg3;
};


class tool{
public:
	tool();
	~tool();
	void invalid_input();
	void show_help();
	bool run(commandline& cmdln, report& reporter, configuration& config);
private:
};

class configuration{
public:
		configuration();
		~configuration();
		bool init();
		bool set_blk_read(bool new_val);
		bool set_blk_read_s(bool new_val); 
		bool set_kb_read(bool new_val);
		bool set_blk_write(bool new_val);
		bool set_blk_write_s(bool new_val);
		bool set_kb_write(bool new_val);
		bool set_interval(int new_val);
		bool set_count(int new_val);
		/*bool set_report(string name);*/
		bool pass_params(bool& bRead, bool& bReadS, bool& kbRead, bool& bWrite, bool& bWriteS, bool& kbWrite); 
		void print_config();
		int get_interval();
		int get_count();
private:
	 	int interval_value;
		int count_value; 
		/*string report_name;*/
		//since bool true == int 1, a simple flick to false requires only changing to zero
		//can be directly manipulated by input from "set [flag]" command
		//all values can be 0/false (DO_NOT_WRITE) or 1/true (WRITE)
		bool blk_read;
		bool blk_read_s; 
		bool kb_read;
		bool blk_write;
		bool blk_write_s;
		bool kb_write;


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

class reportT{
public:
	reportT();
	~reportT();
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


//enum OP_TYPE_t {help, run, set, print, save, exit_t);
//enum FLAG_t {report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};

int main()
{
	commandline cmdln;
	tool tool_body;
	reportT reporter;
	configuration config;
	
	
	config.init();
	cmdln.welcome_message();
	
	
	cmdln.parse_input_cmd();
	bool reallyRun = tool_body.run(cmdln, reporter, config);
	
	while (reallyRun == true)
	{
		cmdln.parse_input_cmd();
		reallyRun = tool_body.run(cmdln, reporter, config);
	}
	
}

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
        while(!infile.eof) // To get you all the lines.
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
bool reportT::read_file()
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


configuration::configuration()
{
	interval_value = 10;
	count_value = 10;
	/*report_name = "report.adt";*/
	//by super-default, set all values to true/1
	blk_read = true;
	blk_read_s = true;
	kb_read = true;
	blk_write = true;
	blk_write_s = true;
	kb_write = true;
	}
	
configuration::~configuration()
{
}

int get_interval()
{
	return interval_value;
}

int get_count()
{
	return count_value;
}

bool configuration::init()
{
	/*read in the configuration*/
	return true;
}

bool configuration::pass_params(bool& bRead, bool& bReadS, bool& kbRead, bool& bWrite, bool& bWriteS, bool& kbWrite)
{
	bRead = blk_read; 
	bReadS = blk_read_s;
	kbRead = kb_read;
	bWrite = blk_write;
	bWriteS = blk_write_s;
	kbWrite = kb_write;
	
	return true;
}


bool configuration::set_blk_read(bool new_val)
{
	blk_read = new_val;
	}
	
bool configuration::set_blk_read_s(bool new_val)
{
	blk_read_s = new_val;
	}
bool configuration::set_kb_read(bool new_val)
{
	kb_read = new_val;
	}
bool configuration::set_blk_write(bool new_val)
{
	blk_write = new_val;
	}
bool configuration::set_blk_write_s(bool new_val)
{
	blk_write_s = new_val;
	}
bool configuration::set_kb_write(bool new_val)
{
	kb_write = new_val;
	}
bool configuration::set_interval(int new_val);
{
	interval_value = new_val;
	}
bool configuration::set_count(int new_val)
{
	count_value = new_val;
	}
/*bool configuration::set_report(string name)
{
	report_name = name;
	}*/
	
void configuration::print_config()
{
		cout << "Interval between successive samples (interval_value): " << interval_value;
		cout << "Number of samples to gather (count_value): " << count_value; 
		cout << "File name for report (report_name): " << report_name;
		cout << "\nPrint blk_read: " << blk_read;
		cout << "\nPrint blk_read/s: " << blk_read_s; 
		cout << "\nPrint kb_read: " << kb_read;
		cout << "\nPrint blk_write: " << blk_write;
		cout << "\nPrint blk_write/s: " << blk_write_s;
		cout << "\nPrint kb_write: " << kb_write;
		}
		
		
tool::tool()
{
}

tool::~tool()
{
}

bool tool::run(commandline& cmdln, report& reporter, configuration& config)
{
	if(cmdln.get_curr_opr() == null_opr)
	{
		invalid_input();
	}
	else if(cmdln.get_curr_opr() == help)
	{
		show_help();
	}
	else if(cmdln.get_curr_opr() == run)
	{
		reporter.build_report(config);
		reporter.write_file(cmdln.get_filename());
		reporter.print_report(cmdln.get_filename());
		cout << "\n";
	}
	else if(cmdln.get_curr_opr() == set) //finished
	{
		switch (cmdln.get_curr_flag()){
		case null_flag:
			invalid_input();
			break;
		case report:
			config.set_report_name(cmdln.get_arg3_string);
			break;
		case count:
			config.set_count_value(atoi(cmdln.get_arg3_string().c_str()));
			break;
		case interval:
			config.set_interval:value(atoi(cmdln.get_arg3_string().c_str()));
			break;
		case blk_read:
			config.set_blk_read(cmdln.get_curr_arg3_purpose());
			break;
		case blk_read_s:
			config.set_blk_read_s(cmdln.get_curr_arg3_purpose());
			break;
		case blk_write:
			config.set_blk_write(cmdln.get_curr_arg3_purpose());
			break;
		case blk_write_s:
			config.set_blk_write_s(cmdln.get_curr_arg3_purpose());
			break;
		case kb_read:
			config.set_kb_read_s(cmdln.get_curr_arg3_purpose());
			break;
		case kb_write:
			config.set_kb_write(cmdln.get_curr_arg3_purpose());
			break;
		}
	}
	else if(cmdln.get_curr_opr() == print)//finished
	{
		if(cmdln.get_curr_flag() == conf)
			{
			config.print_config();
			}
		else if(cmdln.get_curr_flag() == report)
			{
			reporter.print_report(cmdln.get_filename());
			}
	}
	else if(cmdln.get_curr_opr() == save)
	{
	}
	else if(cmdln.get_curr_opr() == exit_t) //finished
	{
		return false;
	}
	else
	{
		return false;
	}
	return true;
}
void tool::invalid_input()
{
	cout << "Invalid command. Type \'help\' to get list of acceptable commands.\n";
}

void tool::show_help()
{
	cout << "run - run the monitoring tool. \n"
		<< "set interval [value] Ð set sampling period to [value]\n"
		<< "set count [value] Ð set the number of records to [value]\n" 
		<<	"set report [name] Ð set report file name to [name]\n"
		<< "set blk_read [0|1] Ð set print_blk_read to 0 or 1\n"
		<< "set blk_read/s [0|1] Ð set print_blk_read/s to 0 or 1\n" 
		<< "set kb_read [0|1] Ð set print_kb_read to 0 or 1\n"
		<<	"set blk_write [0|1] Ð set print_blk_write to 0 or 1\n"
		<<	"set blk_write/s [0|1] Ð set print_blk_write/s to 0 or 1\n" 
		<<	"set kb_write [0|1] Ð set print_kb_write to 0 or 1\n"
		<<	"print conf Ð display all the parameters\n"
		<<	"print report Ð open and display the report file\n"
		<<	"save Ð the configuration file audisktool.conf is updated\n"
		<<	"exit_t Ð exit_t the tool.\n";
}


commandline::commandline()
{
	current_opr = null_opr;
	current_flag = null_flag;
	argument3_purpose = null_arg;
	current_arg3 = "";
	filename_worker = "report.adt";
}

commandline::~commandline()
{
}

void commandline::parse_input_cmd(){
	std::string input_command_to_parse;
	cout << "::";
	cin >> input_command_to_parse;

	std::string is01 = "";
	std::string is02 = "";
	std::string is03 = "";

	int space_found_at = -1;

	space_last_found_at = input_command_to_parse.find(" ");
	is01 = input_command_to_parse.substring(0, space_last_found_at);

	int space_found_at_next = input_command_to_parse.find(" ", space_last_found_at);
	if (space_found_at_next > space_last_found_at)
	{
		is02 = input_command_to_parse.substring(space_last_found_at, space_found_at_next);

		is03 = input_command_to_parse.substring(space_found_at_next);
	}
	
	map_type(is01);
	map_flag(is02);
	map_arg_3(is03);
}

void commandline::map_type(string type_in){
//(1) mapping OPER_TYPE_t
	map<std::string, OPER_TYPE_t> map_operation_type;
	map_operation_type["null"] = null_opr;
	map_operation_type["help"] = help;
	map_operation_type["run"] = run;
	map_operation_type["set"] = set;
	map_operation_type["print"] = print;
	map_operation_type["save"] = save;
	map_operation_type["exit_t"] = exit_t;
	
	current_opr
	
	/*
	//using map of OPER_TYPE_t
	std::string operation_string_input;
	cin >> operation_string_input;
	OPER_TYPE_t operation_type_input = map_operation_type[operation_string_input];
	*/

}

void commandline::map_flag(string flag_in){

	//(2) mapping FLAG_t
	map<std::string, FLAG_t> map_flag;
	map_flag["null"] = null_flag;
	map_flag["report"] = report;
	map_flag["count"] = count;
	map_flag["interval"] = interval;
	map_flag["conf"] = conf;
	map_flag["blk_read"] = blk_read;
	map_flag["blk_read/s"] = blk_read_s;
	map_flag["blk_write"] = blk_write;
	map_flag["blk_write/s"] = blk_write_s;
	map_flag["kb_read"] = kb_read;
	map_flag["kb_write"] = kb_write;
	map_flag[""] = null_flag;
	
	if (map_flag.end() != map_flag.find(flag_in))
		{
		current_flag = map_flag[flag_in];
		}
	else
		{
		current_flag = null_flag;
		}
	
	/*
	//using map of FLAG_t
	std::string flag_in;
	cin >> flag_in;
	FLAG_t flag_input = map_flag[flag_in];
	*/
}

void commandline::map_arg_three(string arg_in){

	
	
	//(3) mapping ARG3_PURPOSE_t
	map<std::string, ARG3_PURPOSE_t> map_arg3_purpose;
	map_arg3_purpose["null"] = null_arg;
	map_arg3_purpose["0"] = p0;
	map_arg3_purpose["1"] = p1;
	map_arg3_purpose[""] = null_arg;
	
	/*
	//using map of ARG3_PURPOSE_t
	std::string arg3_string_in;
	cin >> arg3_string_in;
	ARG3_PURPOSE_t arg3_purpose = map_arg3_purpose[arg3_string_in];
	*/
	if (map_arg3_purpose.end() != map_arg3_purpose.find(arg_in))
		{
		//assume it is a predefined value, like a 0 or 1...or it's empty
		argument3_purpose = map_arg3_purpose[arg_in];
		current_arg3 = arg_in;
		}
	
	else if (arg_in.contains("."))
		{
		//assume a file name
		argument3_purpose = filename;
		current_arg3 = arg_in;
		filename_worker = arg_in;
		}
	else
		{
		//assume a value of some sort [ignoring 0 and 1], not a file name
		argument3_purpose = value;
		current_arg3 = arg_in;
		}
}

void commandline::welcome_message()
{
	cout << "auDiskTool, version " << verNum << ". Type \'help\' to find out about commands, or enter alternative command now.\n";
}

const OP_TYPE_t commandline::get_curr_opr()
{
	return current_opr;
}

const FLAG_t commandline::get_curr_flag()
{
	return current_flag;
}

const ARG3_PURPOSE_t commandline::get_curr_arg3_purpose()
{
	return argument3_purpose;
}

const string commandline::get_arg3_string()
{
	return current_arg3;
}