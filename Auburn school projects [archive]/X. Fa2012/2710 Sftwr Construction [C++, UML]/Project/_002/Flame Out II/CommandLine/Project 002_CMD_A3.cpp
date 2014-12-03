#include <iostream>
#include <map>
using namespace std;

enum OP_TYPE_t {null_opr, help, run, set, print, save, exit_t};
enum FLAG_t {null_flag, report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {0 = 0, 1 = 1, null_arg, filename, value};

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



commandline::commandline()
{
	current_opr = null;
	current_flag = null;
	argument3_purpose = null;
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
	map_operation_type["null"] = null;
	map_operation_type["help"] = help;
	map_operation_type["run"] = run;
	map_operation_type["set"] = set;
	map_operation_type["print"] = print;
	map_operation_type["save"] = save;
	map_operation_type["exit"] = exit;
	
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
	map_flag["null"] = null;
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
	map_flag[""] = null;
	
	if (map.end() != map_flag.find(flag_in))
		{
		current_flag = map_flag[flag_in];
		}
	else
		{
		current_flag = null;
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
	//map_arg3_purpose["null"] = null;
	//map_arg3_purpose["filename"] = filename;
	//map_arg3_purpose["value"] = value;
	map_arg3_purpose[""] = null;
	
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