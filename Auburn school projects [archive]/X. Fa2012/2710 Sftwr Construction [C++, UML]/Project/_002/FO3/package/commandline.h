#ifndef COMMANDLINE_H
#define COMMANDLINE_H

#include <iostream>
#include <map>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <cstring>

using namespace std;

#ifndef ENUM_TYPES
#define ENUM_TYPES
enum OPER_TYPE_t {null_opr, help, run_t, set, print, save, exit_t};
enum FLAG_t {null_flag, report, count_t, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {p0 = 0, p1 = 1, null_arg, filename, value};
#endif

class commandline{
public:
	commandline();
	~commandline();
	void parse_input_cmd();
	void map_type(string type_in);
	void map_flag(string flag_in);
	void map_arg_three(string arg_in);
	void welcome_message();
	const OPER_TYPE_t get_curr_opr();
	const FLAG_t get_curr_flag();
	const ARG3_PURPOSE_t get_curr_arg3_purpose();
	const string get_arg3_string();
	std::string filename_worker;

private:
	OPER_TYPE_t current_opr;
	FLAG_t current_flag;
	ARG3_PURPOSE_t argument3_purpose;
	std::string current_arg3;
};


#endif