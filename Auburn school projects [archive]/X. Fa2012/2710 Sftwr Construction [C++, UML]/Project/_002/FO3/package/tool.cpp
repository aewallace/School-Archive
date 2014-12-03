#include "tool.h"

tool::tool()
{
}

tool::~tool()
{
}

bool tool::run(commandline& cmdln, reportT& reporter, configuration& config)
{
	if(cmdln.get_curr_opr() == null_opr)
	{
		invalid_input();
	}
	else if(cmdln.get_curr_opr() == help)
	{
		show_help();
	}
	else if(cmdln.get_curr_opr() == run_t)
	{
		reporter.build_report(config);
		reporter.write_file(cmdln.filename_worker);
		reporter.print_report(cmdln.filename_worker);
		cout << "\n";
	}
	else if(cmdln.get_curr_opr() == set) //finished
	{
		switch (cmdln.get_curr_flag()){
		case null_flag:
			invalid_input();
			break;
		case report:
			cmdln.filename_worker = cmdln.get_arg3_string();
			break;
		case count_t:
			config.set_count(atoi(cmdln.get_arg3_string().c_str()));
			break;
		case interval:
			config.set_interval(atoi(cmdln.get_arg3_string().c_str()));
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
			config.set_kb_read(cmdln.get_curr_arg3_purpose());
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
			reporter.print_report(cmdln.filename_worker);
			}
		else
			{
			cout << "No flag specified. Please retry command.\n";
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
		<<	"exit Ð exit the tool.\n";
}

