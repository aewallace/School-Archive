#include <string>
using namespace std;

class configuration{
public:
		configuration();
		~configuration();
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
}

int get_interval()
{
	return interval_value;
}

int get_count()
{
	return count_value;
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
	}
	
bool configuration::set_blk_read_s(bool new_val)
{
	blk_read_s = new_val;
	}
bool configuration::set_kb_read(bool new_val)
{
	kb_read = new_val;
	}
bool configuration::set_blk_write(bool new_val)
{
	blk_write = new_val;
	}
bool configuration::set_blk_write_s(bool new_val)
{
	blk_write_s = new_val;
	}
bool configuration::set_kb_write(bool new_val)
{
	kb_write = new_val;
	}
bool configuration::set_interval(int new_val);
{
	interval_value = new_val;
	}
bool configuration::set_count(int new_val)
{
	count_value = new_val;
	}
/*bool configuration::set_report(string name)
{
	report_name = name;
	}*/
	
void configuration::print_config()
{
		cout << "Interval between successive samples (interval_value): " << interval_value;
		cout << "Number of samples to gather (count_value): " << count_value; 
		cout << "File name for report (report_name): " << report_name;
		cout << "\nPrint blk_read: " << blk_read;
		cout << "\nPrint blk_read/s: " << blk_read_s; 
		cout << "\nPrint kb_read: " << kb_read;
		cout << "\nPrint blk_write: " << blk_write;
		cout << "\nPrint blk_write/s: " << blk_write_s;
		cout << "\nPrint kb_write: " << kb_write << "\n";
		}