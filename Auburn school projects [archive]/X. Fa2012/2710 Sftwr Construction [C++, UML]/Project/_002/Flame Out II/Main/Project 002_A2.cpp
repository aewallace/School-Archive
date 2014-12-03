
#include <iostream>
#include <map>
using namespace std;


enum wind_directions_t {NO_WIND, NORTH_WIND, SOUTH_WIND, EAST_WIND, WEST_WIND};
enum OP_TYPE_t {help, run, set, print, save);

int main()
{
	cout << "Hello World!";
	
	map<std::string,wind_directions_t> m;
	m["NO_WIND"] = NO_WIND;
	m["NORTH_WIND"] = NORTH_WIND; //repeat the process for the other wind directions


	std::string wind_dir;
	cin >> wind_dir;
	wind_directions_t wind_dir_e = m[wind_dir];
	
	//mapping OP_TYPE_t
	map<std::string, OP_TYPE_t> map_operation_type;
	map_operation_type["help"] = help;
	map_operation_type["run"] = run;
	map_operation_type["set"] = set;
	map_operation_type["print"] = print;
	map_operation_type["save"] = save;
}