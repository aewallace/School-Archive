
#include <iostream>
#include <map>
using namespace std;


enum wind_directions_t {NO_WIND, NORTH_WIND, SOUTH_WIND, EAST_WIND, WEST_WIND};
enum OP_TYPE_t {help, run, set, print, save, exit);
enum FLAG_t {report, count, interval, conf, blk_read, blk_read_s, blk_write, blk_write_s, kb_read, kb_write};

int main()
{
	cout << "Hello World!";
	
	map<std::string,wind_directions_t> m;
	m["NO_WIND"] = NO_WIND;
	m["NORTH_WIND"] = NORTH_WIND; //repeat the process for the other wind directions


	std::string wind_dir;
	cin >> wind_dir;
	wind_directions_t wind_dir_e = m[wind_dir];
	
	//(1) mapping OPER_TYPE_t
	map<std::string, OPER_TYPE_t> map_operation_type;
	map_operation_type["help"] = help;
	map_operation_type["run"] = run;
	map_operation_type["set"] = set;
	map_operation_type["print"] = print;
	map_operation_type["save"] = save;
	map_operation_type["exit"] = exit;
	
	//using map of OPER_TYPE_t
	std::string operation_string_input;
	cin >> operation_string_input;
	OPER_TYPE_t operation_type_input = map_operation_type[operation_string_input];
	
	//(2) mapping FLAG_t
	map<std::string, FLAG_t> map_flag;
	map_flag["report"] = report;
	map_flag["count"] = count;
	map_flag["interval"] = interval;
	map_flag["config"] = conf;
	map_flag["blk read"] = blk_read;
	map_flag["blk read/s"] = blk_read_s;
	map_flag["blk write"] = blk_write;
	map_flag["blk write/s"] = blk_write_s;
	map_flag["kb read"] = kb_read;
	map_flag["kb write"] = kb_write;

	
	
}