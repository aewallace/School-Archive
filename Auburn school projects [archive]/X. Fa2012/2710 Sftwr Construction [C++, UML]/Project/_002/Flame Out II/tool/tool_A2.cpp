#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

enum OP_TYPE_t {null, help, run, set, print, save, exit);
enum FLAG_t {null, report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {0 = 0, 1 = 1, null, filename, value};

class tool{
public:
	tool();
	~tool();
	void invalid_input();
	void show_help();
	bool run();
private:
};

tool::tool()
{
}

tool::~tool()
{
}

bool tool::run(commandline& cmdln, report& reporter, configuration& config)
{
	if(cmdln.get_curr_opr() == null)
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
		case null:
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
	else if(cmdln.get_curr_opr() == exit) //finished
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
		<<	"exit Ð exit the tool.\n";
}