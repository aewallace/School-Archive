#ifndef TOOL_H
#define TOOL_H

#include <iostream>
#include <map>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <cstring>
#include "commandline.h"
#include "configuration.h"
#include "reportT.h"


#ifndef ENUM_TYPES
#define ENUM_TYPES
enum OPER_TYPE_t {null_opr, help, run_t, set, print, save, exit_t};
enum FLAG_t {null_flag, report, count_t, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {p0 = 0, p1 = 1, null_arg, filename, value};
#endif

using namespace std;

class tool{
public:
	tool();
	~tool();
	void invalid_input();
	void show_help();
	bool run(commandline& cmdln, reportT& reporter, configuration& config);
private:
};


#endif