#ifndef REPORTT_H
#define REPORTT_H

#include <iostream>
#include <map>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <cstring>

#include "commandline.h"
#include "configuration.h"

using namespace std;

#ifndef ENUM_TYPES
#define ENUM_TYPES
enum OPER_TYPE_t {null_opr, help, run_t, set, print, save, exit_t};
enum FLAG_t {null_flag, report, count_t, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};
enum ARG3_PURPOSE_t {p0 = 0, p1 = 1, null_arg, filename, value};
#endif

string longtostr(long number);

//stores one diskstat sample
struct reportlet{

	long sectors_read;
	long sectors_written;
	long kb_read;
	long kb_written;
	long sectors_read_s;
	long sectors_written_s;
	//fields 1 (reads, where 1 read = 1 sector), 5 (writes, where 1 write = 1 sector), 
	// and calculate from that based on deltas in time (for /s)
	// or(and) 1 sector or block being 1 KB
};

class reportT{
public:
	reportT();
	reportT(int sample_count);
	~reportT();
	bool print_report(string filename);
	bool grab_report();
	bool build_report(configuration config);
	bool read_file();
	bool write_file(string filename);
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


#endif