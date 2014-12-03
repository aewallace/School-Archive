#include "commandline.h"

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
	getline(cin, input_command_to_parse);

	std::string is01 = "";
	std::string is02 = "";
	std::string is03 = "";

	int space_last_found_at = -1;

	space_last_found_at = input_command_to_parse.find(" ");
	is01 = input_command_to_parse.substr(0, space_last_found_at);
	#ifdef DEBUG
	cout << "is01: " << is01;
	#endif
	
	input_command_to_parse = input_command_to_parse.substr(space_last_found_at + 1);
	#ifdef DEBUG
	cout << space_last_found_at << "\n::";
	cout << input_command_to_parse;
	#endif
	
	space_last_found_at = input_command_to_parse.find(" ");
	if (input_command_to_parse.size() > 0)
	{
		is02 = input_command_to_parse.substr(0, space_last_found_at);
		#ifdef DEBUG
		cout << "\nis02: " << is02;
		#endif
	}
	input_command_to_parse = input_command_to_parse.substr(space_last_found_at + 1);
	#ifdef DEBUG
	cout << "\nslfa " << space_last_found_at << "::";
	cout << "\nictp " << input_command_to_parse << "::";
	#endif
	
	space_last_found_at = input_command_to_parse.find(" ");

	if (input_command_to_parse.size() > 0)
	{
		is03 = input_command_to_parse.substr(0, space_last_found_at);
		#ifdef DEBUG
		cout << "\nis03: " << is03;
		#endif
	}
	
	map_type(is01);
	map_flag(is02);
	map_arg_three(is03);
}

void commandline::map_type(string type_in){
//(1) mapping OPER_TYPE_t
	map<std::string, OPER_TYPE_t> map_operation_type;
	map_operation_type["null"] = null_opr;
	map_operation_type["help"] = help;
	map_operation_type["run"] = run_t;
	map_operation_type["set"] = set;
	map_operation_type["print"] = print;
	map_operation_type["save"] = save;
	map_operation_type["exit"] = exit_t;
	
	current_opr = map_operation_type[type_in];
	#ifdef DEBUG
	cout << "\nmapping type: " << type_in << "...respective value changed to: " << current_opr << "\n";
	#endif
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
	map_flag["count"] = count_t;
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
	
	else if (string::npos != arg_in.find(".")) //if the period is actually found at any position...
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
	string verNum = "1D0F.30Nov2012.23:06";

	cout << "auDiskTool, version " << verNum << ".";
	cout << "\n";
	cout << "DEMO VERSION; Not all functions implemented as required.\n"
	cout << "Type \'help\' to find out about commands, or enter alternative command now.\n";
}

const OPER_TYPE_t commandline::get_curr_opr()
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

