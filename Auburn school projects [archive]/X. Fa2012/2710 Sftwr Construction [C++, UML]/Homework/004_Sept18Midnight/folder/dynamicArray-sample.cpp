/* 
 * Xiao Qin: Homework 6
 * (1) How to design a Doctor class
 * (2) Unit testing.
 * (3) Pointers 
 * (4) Dynamic Array (dynamic vs. static array)
 * (5) Resize a dynamic array
 * (6) Overload assignment operator
 * (7) Overload operators as friend functions (not member functions)
 *  Put the assignment operator inside Doctor class definition. 
 *  It must be a member because operator= is special (one parameter). 
 * (8) Can one constructor of a class call another constructor of 
 *     the same class to initialize the this object?
 *     Answer: No! But you can let two constroctors share a private function
 */ 
//#define UNIT_TESTING_CONSTRUCTORS
//#define UNIT_TESTING_ADD_EMPTY_PATIENT
//#define UNIT_TESTING_RESIZE
//#define UNIT_TESTING_ASSIGNMENT_OPERATOR
#define PRODUCT

#include <iostream>
#include <string>
#include <assert.h>
using namespace std;

typedef unsigned short ushort_t;
typedef string* stringPtr_t;

bool get_number (ushort_t& number);

class Doctor {
private:
  string doctorName;
  stringPtr_t patientArray;
  ushort_t patientArraySize;
  ushort_t numOfPatient;
public:
  Doctor(); //Default doctorName="need a name"  patientArraySize = 100
  Doctor(ushort_t patientArrayCapacity); //specify patientArraySize
  Doctor(string docName); //Default patientArraySize = 100
  Doctor(string docName, ushort_t patientArrayCapacity); //specify patientArraySize

  //Add a patient. Please check that patientArray is not Full.
  //Return: true - successfully add a patient
  //        false - this is a failure
  bool addPatient(string patientName);

  void displayPatientArray();

  //If the Array size is small, we need to resize the array
  void resizePatientArray(ushort_t newArraySize); 

  string getDoctorName() const {return doctorName;}
  ushort_t getNumOfPatient() const {return numOfPatient;}
  ushort_t getArraySize() const {return patientArraySize;}

  void setDoctorName(string docName) {doctorName.assign(docName);};

  //Just delete patient infomation without removing memory resources 
  void emptyPatientArray() {numOfPatient = 0;} 

  Doctor& operator =(const Doctor& docSource);
  //friend does not work here.
  //friend Doctor& operator =(Doctor& docSource);
  ~Doctor() {delete [] patientArray;}  
};

int main()
{
#ifdef UNIT_TESTING_CONSTRUCTORS
  //Test Constructors
  Doctor testDoc1;
  testDoc1.displayPatientArray();

  Doctor testDoc2(2);
  testDoc2.displayPatientArray();

  //Implement more test cases below:

#endif

#ifdef UNIT_TESTING_ADD_EMPTY_PATIENT
  //Test addPatient()
  cout << "Test addPatient() \n";
  Doctor testDoc5(2);
  assert(testDoc5.addPatient("Bob Smith")==true);
  assert(testDoc5.addPatient("Ali Smith")==true);
  testDoc5.displayPatientArray();

  //Below please implement a test case where the dynamic array is full:
  

#endif

#ifdef UNIT_TESTING_RESIZE
  //Implement test cases for resizePatientArray() below:
  

#endif


#ifdef UNIT_TESTING_ASSIGNMENT_OPERATOR
  //Implement test cases for the overloaded assignment operator below:


#endif

//Implement a product version
#ifdef PRODUCT	
  


#endif

}

Doctor::Doctor() : doctorName("need a name."), patientArraySize(100), numOfPatient(0) {
  //Create a dynamic array for patients below:
  
}

Doctor::Doctor(ushort_t patientArrayCapacity) : doctorName("need a name."), patientArraySize(patientArrayCapacity), numOfPatient(0) {
  //Create a dynamic array for patients below:
}


//Implement the third constructor below:
Doctor::Doctor(string docName) : 
  

//Implement the fourth constructor below:
Doctor::Doctor(string docName, ushort_t patientArrayCapacity) : 


//Implement addPatient() below:

//Implement displayPatientArray() below:

//Implement resizePatientArray below:
//If newArraySize is smaller than the original size
//then the size will be reduced to newArraySize; the rest patients 
//will be dropped. 
void Doctor::resizePatientArray(ushort_t newArraySize) { 
  

}

// Overload the assignment operator below:
// friend function does not work here.
// Doctor& operator =(Doctor& docSource);
Doctor& Doctor::operator =(const Doctor& docSource) {

}

bool get_number (ushort_t& number)
{
  char ch;
  while ( !( cin >> number ) ) { //checks to see if the value in the cin
		//stream is the correct type, if not it returns false,
			//true otwise.
    if ( cin.eof() )	//Will this line be normally executed?
      return false;
    else {

	  cin.clear(); //This corrects the stream.
	  cin.ignore(1000, '\n'); //Ignore 1000 characters or when '\n' is found
      
	  cout<<"Invalid input, please try again: "; //You may update this line for your own programs

    }
  }

  return true;
}
