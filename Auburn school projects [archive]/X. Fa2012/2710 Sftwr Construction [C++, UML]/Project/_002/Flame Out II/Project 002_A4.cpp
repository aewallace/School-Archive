
#include <iostream>
#include <map>
using namespace std;


enum wind_directions_t {NO_WIND, NORTH_WIND, SOUTH_WIND, EAST_WIND, WEST_WIND};

int main()
{
	cout << "Hello World!";
	
	map<std::string,wind_directions_t> m;
	m["NO_WIND"] = NO_WIND;
	m["NORTH_WIND"] = NORTH_WIND; //repeat the process for the other wind directions


	std::string wind_dir;
	cin >> wind_dir;
	wind_directions_t wind_dir_e = m[wind_dir];
	
	
	
	
}