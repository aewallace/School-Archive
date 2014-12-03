#include <iostream>
#include <map>
using namespace std;

enum OP_TYPE_t {null, help, run, set, print, save, exit);
enum FLAG_t {null, report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {0 = 0, 1 = 1, null, filename, value};

class commandline{
public:
	commandline();
	~commandline();
	void input_full_cmd();
	void map_type(string type_in);
	void map_flag(string flag_in);
	void map_arg_three(string arg_in);
	void welcome_message();
	void invalid_input();
	void show_help();

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
}

commandline::~commandline()
{
}

void commandline::parse_input_oper(){
	std::string input_command_to_parse;
	cout << "::";
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

void commandline::invalid_input()
{
	cout << "Invalid command. Type \'help\' to get list of acceptable commands.\n";
}

void commandline::show_help()
{
	cout << "run - run the monitoring tool. \n"
		<< "set interval [value] Ð set sampling period to [value]\n"
		<< "set count [value] Ð set the number of records to [value]\n" 
		<<	"set report [name] Ð set report file name to [name]\n"
		<< "set blk_read [0|1] Ð set print_blk_read to 0 or 1\n"
		<< "set blk_read/s [0|1] Ð set print_blk_read/s to 0 or 1\n" 
		<< "set kb_read/s [0|1] Ð set print_kb_read to 0 or 1\n"
		<<	"set blk_write [0|1] Ð set print_blk_write to 0 or 1\n"
		<<	"set blk_write/s [0|1] Ð set print_blk_write/s to 0 or 1\n" 
		<<	"set kb_write [0|1] Ð set print_kb_write to 0 or 1\n"
		<<	"print conf Ð display all the parameters\n"
		<<	"print report Ð open and display the report file\n"
		<<	"save Ð the configuration file audisktool.conf is updated\n"
		<<	"exit Ð exit the tool.\n";
}
	
