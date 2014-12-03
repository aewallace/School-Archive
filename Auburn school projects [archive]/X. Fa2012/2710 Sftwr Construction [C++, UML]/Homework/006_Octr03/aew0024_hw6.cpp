/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw6.cpp
*written with Vi in Linux & jGRASP in Mac OS X 10.6.
*compiled using default tools on both platforms
*/

/*****************************
 *Homework 006: Doctor, Doctor!!
 ****************************/

//****************************************************
// Enable this line to function in debug mode
//	Disable line to enable production version of software
#define UNIT_TESTING
//***************************************************


#include <iostream>
#include <string>
#include <sstream>
#include <assert.h>
using namespace std;

//global settings and functions ********************
int GLOBAL_MAX_PATIENT_CAPACITY = 100;


//Doctor class, meant to simplify creation of multiple "doctor" objects *******
class Doctor {
	public:
		Doctor(); //default constructor
		Doctor(short patientArrayCapacity);
		Doctor(string doctorName);
		Doctor(string doctorName, short patientArrayCapacity);
		int displayDoctorPatientInfo();
		void resetPatientValues();
		int setInputValues();
		int addPatients();
		~Doctor(); //destructor
		const string getDoctor();
		const short getMaxPatientCapacity();
		const short getCurrentPatientCount();
		bool resizeArray(short size, bool copyContents);
	private:
		string name;
		short numPatientsSupported;
		short actualClienteleSize;
		string*  patientList;
		string* dupPatientListHelper;
		bool resizeArray(short size);
		string* operator =(string* input);
		bool duplicationClearOnExit;
	};
	

//begin main methods*********************************
#ifdef UNIT_TESTING //build and run the debug version
int main(){
	cout << "UNIT TESTING. \n";
	cout << "\n\nUnit tests 1.1 - 1.3: constructor use/object editing tests.\n";

	Doctor newDoctor;
	assert (GLOBAL_MAX_PATIENT_CAPACITY == newDoctor.getMaxPatientCapacity());
	cout << "Unit test 1.1 passed. Object created successfully.\n";
	
	string tempname = "[name not set]";
	assert(0 == tempname.compare(newDoctor.getDoctor()));
	cout << "Unit test 1.2 passed. Doctor name successfully set to generic placeholder.\n";

	short newCapacity = GLOBAL_MAX_PATIENT_CAPACITY + 15;
	newDoctor.resizeArray(newCapacity, true);
	assert(newCapacity == newDoctor.getMaxPatientCapacity());
	cout << "Unit test 1.3 passed. Patient array size successfully changed.\n";
	
	cout << "\n";
	
	cout << "Unit tests 2.1 - 2.2: reset values and print empty class tests.\n";
	newDoctor.resetPatientValues();
	assert(newDoctor.getMaxPatientCapacity() == 0);
	assert(newDoctor.getCurrentPatientCount() == 0);
	cout << "Unit test 2.1 passed. Values reset.\n"; 
	
	assert(0 == newDoctor.displayDoctorPatientInfo());
	cout << "Unit test 2.2 passed. Expected 0 patient names to be displayed.\n";
	

	cout << "\n";
	
	cout << "Unit tests 3.1 to 3.3: when prompted, enter the doctor's name, then add at least one patient.\n";
	cout << "(Note: space will be allocated for at least 100 patients, but only one patient is necessary.)\n";
	Doctor newDoctorB;
   newDoctorB.setInputValues();
	assert (0 < newDoctorB.getCurrentPatientCount());
	cout << "setInputValues() test passed. Now testing functionality of addPatients().\n";
	cout << "Now please add at least one more user.\n";
        newDoctorB.addPatients();
	assert (1 < newDoctorB.getCurrentPatientCount());
	cout << "addPatients() test successfully passed.\n";
	cout << "Unit tests 3.1 to 3.3 passed.\n";
	
	cout << "\n";
	cout << "End of testing."; 
	
	return 0;
	}
#else //build and run the production version
int main(){
	string exitMessage = "*** Goodbye! ***";
	string welcomeMessage = "***Welcome to Albert Wallace's \"Doctor, Doctor!\" program***\n";
	cout << welcomeMessage;
	Doctor newDoctor;
	newDoctor.setInputValues();
	newDoctor.addPatients();
	
	newDoctor.displayDoctorPatientInfo();
	cout << exitMessage;
	return 0;
	}
#endif
//end of main methods ********************



//accessor functions
const string Doctor::getDoctor()
	{
	return name;
	}
const short Doctor::getMaxPatientCapacity()
	{
	return numPatientsSupported;
	}
const short Doctor::getCurrentPatientCount()
	{
	return actualClienteleSize;
	}

//visual accessor function; displays all data for a given Doctor object
int Doctor::displayDoctorPatientInfo(){

	cout << "***Doctor & Patient Data Output***\n";
	
	int lines_of_patients_output = 0;
	cout << "Name of doctor: " << name << ".\n";
	cout << "Number of patients: " << actualClienteleSize << ".\n";
	cout << "List of patients: \n";
	for (int i = 0; i < actualClienteleSize; i++){
		cout << patientList[i] << "\n";
		lines_of_patients_output++;
		}
	return lines_of_patients_output;
	}

//resets the PATIENT values, while maintaining the name of the doctor
//resets patient count and max patient storage value
//warning: class will be unusable unless constructor is called
//to preserve doctor's name, call this function, temporarily store name in alt variable, then call constructor
void Doctor::resetPatientValues(){
	numPatientsSupported = 0;
	actualClienteleSize = 0;
	patientList = new string[numPatientsSupported];
	}

//destructor for class "Doctor"
//warning: patient data will be removed from memory, use carefully!
Doctor::~Doctor(){
	//releases all memory used
	delete [] patientList;
	if (duplicationClearOnExit)
		{
		cout << "\nclearing last bits of memory...";
		delete [] dupPatientListHelper;
		}
	}
	
//overload of the equals ("=") operator
//allows duplication of dynamic string arrays
string* Doctor::operator =(string* input){
	duplicationClearOnExit = true;
	dupPatientListHelper = new string[numPatientsSupported];
	for (int i = 0; i < numPatientsSupported; i++){
		dupPatientListHelper[i] = input[i];
		}
	return dupPatientListHelper;
	}
	
//gets doctor and patient data
//warning: will overwrite all current values. to add patients later, use addPatients method
int Doctor::setInputValues(){
	short lines_read_in = 0;
	string tempName;
	cout << "Please input the name of the doctor: ";
	getline(cin, tempName);
	cout << "\n";

	short tempNumPatients = 0;
	cout << "Please input the maximum number of patients a doctor may have:\n";
	cout << "(Each doctor can support at least " << GLOBAL_MAX_PATIENT_CAPACITY << " patients; please choose accordingly.\n";
	cin >> tempNumPatients;
	cin.ignore(1000, '\n');
	resizeArray(tempNumPatients);
	cout << "\n";
		
	name = tempName;
	
	bool endEntry = 0;
	
	for (short i = 0; i < getMaxPatientCapacity(); i++){
		cout << "Please enter name of patient number " << i << ": ";
		getline(cin, patientList[i]);
		cout << "\n";
		lines_read_in++;
		actualClienteleSize++;
		if ( i%5 == 0)
			{
			cout << "Would you like to add more patients? (You can add more later)\n";
			cout << "Enter 1 to stop adding patients, or enter 0 to add more patients: ";
			cin >> endEntry;
			cin.ignore(1000, '\n');
			if (endEntry)
				{
				i = numPatientsSupported;
				}
			cout << "\n";
			}
		}
	cout << "Thank you. Data successfully read in.\n";
	return lines_read_in;
	}

//allows additional patient information to be stored, assuming the array of patients isn't full
//if array is full, a non-destructive resize is called
int Doctor::addPatients(){
	int newAdditions = 0;
	string mystr;
	short targetSize;
	if (actualClienteleSize >=  numPatientsSupported)
		{
		cout << "You must non-destrictively resize the number of supported patients for this doctor.\n";
		cout << "What is the maximum number of patients to be supported under this doctor?\n";
		cout << "(Note: each doctor can support at least " << GLOBAL_MAX_PATIENT_CAPACITY << " patients.)\n";
		getline(cin,mystr);
		stringstream(mystr) >> targetSize;
		if(!resizeArray(targetSize, true)) //if no resizing occurs...
			{
			return 0; //...return that no elements were added
			}
		}
	bool continueAdd = true;
	int i = actualClienteleSize;
	
	cout << "Would you like to add another patient? \n";
	cout << "(enter 0 for no, or enter any other value to add more patients): ";
	getline (cin,mystr);
	stringstream(mystr) >> continueAdd;
	cout << "\n";
	
	while (continueAdd)
		{
		cout << "You have space to add " << numPatientsSupported - actualClienteleSize << " more patient(s).\n";
		if (numPatientsSupported <= actualClienteleSize){
			continueAdd = false;
			}
		else	{
			cout << "Would you like to add another patient? (0 for no, any other value for yes) ";
			getline (cin,mystr);
			stringstream(mystr) >> continueAdd;
			cout << "\n";
			if (!continueAdd)
				{
				//do nothing
				}
			else {
				cout << "Please add a patient name: ";
				getline(cin, patientList[i]);
				cout << "\n";
				newAdditions++;
				actualClienteleSize++;
				i++;
				}
			}
			
		
		}
	return newAdditions;
	}

//allows resizing of the current array with destructive tendencies
//directly manipulates the array instantiated within the class
//allows resize to minimum size of GLOBAL_MAX_PARENT_CAPACITY
bool Doctor::resizeArray(short targetSize)
	{
	short size = targetSize;
	if (size < GLOBAL_MAX_PATIENT_CAPACITY)
		{
		cout << "Attempted resize below defined minimum of " << GLOBAL_MAX_PATIENT_CAPACITY << " units.\n";
		cout << "Target array size automatically set to " << GLOBAL_MAX_PATIENT_CAPACITY << " units of patient storage.\n";
		size = GLOBAL_MAX_PATIENT_CAPACITY;
		}
	patientList = new string[size];
	numPatientsSupported = size;
	actualClienteleSize = 0;
	return true;
	}
	
//allows resizing of the current array with support for copying (safer)
//directly manipulates the array instantiated within the class
//size must be greater than or equal to GLOBAL_MAX_PATIENT_CAPACITY
//size must also be greater than the number of elements to be copied
bool Doctor::resizeArray(short targetSize, bool copyContents)
	{
	duplicationClearOnExit = true;
	short size = targetSize;
	if (size <= actualClienteleSize)
		{
		cout << "Attempted resize below current patient capacity.\n";
		cout << "Array left intact.\n";
		return false;
		}
	if (size < GLOBAL_MAX_PATIENT_CAPACITY)
		{
		cout << "Attempted resize below defined minimum of " << GLOBAL_MAX_PATIENT_CAPACITY << " units.\n";
		cout << "Target array size automatically set to " << GLOBAL_MAX_PATIENT_CAPACITY << " units of patient storage.\n";
		size = GLOBAL_MAX_PATIENT_CAPACITY;
		}
	dupPatientListHelper = new string[numPatientsSupported];
	for (int i = 0; i < numPatientsSupported; i++){
		dupPatientListHelper[i] = patientList[i];
		}
	patientList = new string[size];
	for (int i = 0; i < numPatientsSupported; i++){
		patientList[i] = dupPatientListHelper[i];
		}
	numPatientsSupported = size;
	return true;
	}

//default constructor
//sets a doctor name placeholder, and sets a maximum array size of GLOBAL_MAX_PATIENT_CAPACITY
Doctor::Doctor(){
	name = "[name not set]";
	duplicationClearOnExit = false;
   numPatientsSupported = GLOBAL_MAX_PATIENT_CAPACITY;
	actualClienteleSize = 0;
   patientList = new string[GLOBAL_MAX_PATIENT_CAPACITY];
	for (int i = 0; i < GLOBAL_MAX_PATIENT_CAPACITY; i++)
		{
		patientList[i] = ""; //initialize patient array to blanks
		}
	}

//most basic constructor.
//allows for a custom maximum array size, but sets a generic doctor name placeholder
Doctor::Doctor(short patientArrayCapacity){
	name = "[name not set]";
   numPatientsSupported = patientArrayCapacity;
	duplicationClearOnExit = false;
	actualClienteleSize = 0;
   patientList = new string[numPatientsSupported];
	for (int i = 0; i < patientArrayCapacity; i++)
		{
		patientList[i] = ""; //initialize patient array to blanks
		}
	}

//second most basic constructor.
//allows for a custom doctor name upon instantiation (including blank name),
//but defaults to a maximum array size of GLOBAL_MAX_PATIENT_CAPACITY
Doctor::Doctor(string doctorName){
	name = doctorName;
	duplicationClearOnExit = false;
	numPatientsSupported = GLOBAL_MAX_PATIENT_CAPACITY;
	actualClienteleSize = 0;
	patientList = new string[GLOBAL_MAX_PATIENT_CAPACITY];
	for (int i = 0; i < GLOBAL_MAX_PATIENT_CAPACITY; i++){
		patientList[i] = ""; //initialize all values to blanks
		}
	}

//most feature rich constructor
//allows name of doctor and size of array to be set when object is created
Doctor::Doctor(string doctorName, short patientArrayCapacity){
	name = doctorName;
	duplicationClearOnExit = false;
	numPatientsSupported = patientArrayCapacity;
	actualClienteleSize = 0;
	patientList = new string[patientArrayCapacity];
	for (int i = 0; i < patientArrayCapacity; i++){
		patientList[i] = ""; //initialize all values to blanks
		}
	}

// :]
