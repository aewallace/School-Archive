/*
*Complex Numbers Class & self-implented test
*HW07, Question 03.
*
*Author: Albert Wallace (aew0024)
*Version: M10.D30.Y2012.T14.13
*
*Compiled under OS X using JGrasp.
*Main method located at end of .cpp file.
*/

#include <iostream>
#include <string>
using namespace std;

class cpxNum {
	
	public:
		cpxNum();
		cpxNum(double real_f, double imag_f);
		cpxNum(string wholeNum);
		
		cpxNum operator +(cpxNum num2);
		cpxNum operator -(cpxNum num2);
		cpxNum operator *(cpxNum num2);
		cpxNum operator /(cpxNum num2);
		
		double getRealF();
		double getImagF();
		cpxNum getThisNum();
		
		void displayNum();
	private:
		double real_f;
		double imag_f;
		
};


//****************************************
int main()
{
	double inputA, inputB;
	string inputTotal;
	
	
	cout << "Please enter the 'real' part of a complex number (such as 3 from 3+5i): ";
	cin >> inputA;
	cout << "\nPlease input the 'imaginary' part of a complex number (such as 5 from 3+5i): ";
	cin >> inputB;
	
	cout << "\nPlease input a full imaginary number (such as 7.5+6.7i, with no spaces): ";
	cin >> inputTotal;
	
	cpxNum test0X0A(inputA, inputB);
	cpxNum test0X0B(inputTotal);
	
	cout << "\nThe first complex number was:\n";
	test0X0A.displayNum();
	
	cout << "\nThe second complex number was:\n";
	test0X0B.displayNum();
	
	cpxNum test0X0C = test0X0A * test0X0B;
	cout << "\nThe numbers, when multiplied, equal:\n";
	test0X0C.displayNum();
	
	cpxNum test0X0D = test0X0A / test0X0B;
	cout << "\nThe numbers, when divided, equal:\n";
	test0X0D.displayNum();
	
	cpxNum test0X0E = test0X0A + test0X0B;
	cout << "\nThe numbers, when summed, equal:\n";
	test0X0E.displayNum();
	
	cpxNum test0X0F = test0X0A - test0X0B;
	cout << "\nThe numbers, when subtracted, equal:\n";
	test0X0F.displayNum();
	
	
	return 0;
}
//****************************************

cpxNum::cpxNum()
{
	real_f = 0;
	imag_f = 0;
}

cpxNum::cpxNum(double real_in, double imag_in)
{
	real_f = real_in;
	imag_f = imag_in;
}

cpxNum::cpxNum(string wholeNum)
{	
	char * tempPB_CS;
	char * tempPA_CS;
	real_f = 0;
	imag_f = 0;
	size_t pos;
	string findIt = "+";
	pos = wholeNum.find(findIt);
	string tempPA = "0";
	string tempPB = "0";
	
	if (pos != string::npos)
		{
		tempPA = wholeNum.substr(0, pos);
		tempPB = wholeNum.substr(pos + 1);
		cout << tempPA;
		cout << "\n" << tempPB << "\n";
		tempPA_CS = new char [tempPA.size() + 1];
		tempPB_CS = new char [tempPB.size() + 1];
		
		strcpy(tempPA_CS, tempPA.c_str());
		strcpy(tempPB_CS, tempPB.c_str());
		cout << tempPA_CS << " " << tempPB_CS << "\n";
		
		real_f = atof(tempPA_CS);
		imag_f = atof(tempPB_CS);
		cout << real_f << " " << imag_f << "\n";
		//delete [] tempPA_CS;
		//delete [] tempPB_CS;
		}
	else
		{
		pos = wholeNum.find("i");
		if (pos != string::npos)
			{
			tempPB_CS = new char [tempPB.size() + 1];
			strcpy(tempPB_CS, tempPA.c_str());
			imag_f = atof(tempPB_CS);
			//delete []  tempPB_CS;
			}
		else
			{
			tempPA_CS = new char [tempPA.size() + 1];
			strcpy(tempPA_CS, tempPA.c_str());
			real_f = atof(tempPA_CS);
			//delete [] tempPA_CS;
			}
		}
}

/*cpxNum::~cpxNum()
{
	
}	*/	
cpxNum cpxNum::operator +(cpxNum num2)
{
	double realout;
	double imagout;
	
	realout = real_f + num2.getRealF();
	imagout = imag_f + num2.getImagF();
	
	
	return cpxNum(realout, imagout);
}
cpxNum cpxNum::operator -(cpxNum num2)
{
	double realout;
	double imagout;
	
	realout = real_f - num2.getRealF();
	imagout = imag_f - num2.getImagF();
	
	
	return cpxNum(realout, imagout);
}

cpxNum cpxNum::operator *(cpxNum num2)
{
	double partA;
	double partB;
	double partC;
	double partD;
	
	double realOut;
	double imagOut;
	
	partA = real_f * num2.getRealF();
	partB = real_f * num2.getImagF();
	partC = imag_f * num2.getRealF();
	partD = imag_f * num2.getImagF() * -1;
		
	realOut = (partA + partD);
	imagOut = (partB + partC);
	
	return cpxNum(realOut, imagOut);
}

cpxNum cpxNum::operator /(cpxNum num2)
{
	double partA;
	double partB;
	double partC;
	double partD;
	double denom;
	
	double realOut;
	double imagOut;
	
	partA = real_f * num2.getRealF();
	partB = real_f * num2.getImagF() * -1;
	partC = imag_f * num2.getRealF();
	partD = imag_f * num2.getImagF();
	denom = (num2.getRealF() * num2.getRealF()) + (-1 * num2.getImagF() * num2.getImagF());
	
	realOut = (partA + partD)/denom;
	imagOut = (partB + partC)/denom;
	
	return cpxNum(realOut, imagOut);
}

double cpxNum::getRealF()
{
	return real_f;
}

double cpxNum::getImagF()
{
	return imag_f;
}

cpxNum cpxNum::getThisNum()
{
	return cpxNum(real_f, imag_f);
}



void cpxNum::displayNum()
{
	cout << real_f << " + " << imag_f << "i";
} 