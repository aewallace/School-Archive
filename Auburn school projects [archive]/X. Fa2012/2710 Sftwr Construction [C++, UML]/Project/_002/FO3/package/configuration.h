#ifndef CONFIGURATION_H
#define CONFIGURATION_H

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

//is NOT designed to read from file

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



#endif