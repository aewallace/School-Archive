#include "configuration.h"

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
	cout << "\nNote: configuration never read to/saved from file. Functions not implemented.\n";
}

int configuration::get_interval()
{
	return interval_value;
}

int configuration::get_count()
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
	return blk_read;
	}
	
bool configuration::set_blk_read_s(bool new_val)
{
	blk_read_s = new_val;
	return blk_read_s;
	}
bool configuration::set_kb_read(bool new_val)
{
	kb_read = new_val;
	return kb_read;
	}
bool configuration::set_blk_write(bool new_val)
{
	blk_write = new_val;
	return blk_write;
	}
bool configuration::set_blk_write_s(bool new_val)
{
	blk_write_s = new_val;
	return blk_write_s;
	}
bool configuration::set_kb_write(bool new_val)
{
	kb_write = new_val;
	return kb_write;
	}
bool configuration::set_interval(int new_val)
{
	interval_value = new_val;
	return interval_value;
	}
bool configuration::set_count(int new_val)
{
	count_value = new_val;
	return count_value;
	}
/*bool configuration::set_report(string name)
{
	report_name = name;
	return true;
	}*/
	
void configuration::print_config()
{
		cout << "\n\nConfiguration: ";
		cout << "\nInterval between successive samples (interval_value): " << interval_value;
		cout << "\nNumber of samples to gather (count_value): " << count_value; 
		//cout << "File name for report (report_name): " << report_name;
		cout << "\nPrint blk_read: " << blk_read;
		cout << "\nPrint blk_read/s: " << blk_read_s; 
		cout << "\nPrint kb_read: " << kb_read;
		cout << "\nPrint blk_write: " << blk_write;
		cout << "\nPrint blk_write/s: " << blk_write_s;
		cout << "\nPrint kb_write: " << kb_write << "\n\n";
		}
		
		
