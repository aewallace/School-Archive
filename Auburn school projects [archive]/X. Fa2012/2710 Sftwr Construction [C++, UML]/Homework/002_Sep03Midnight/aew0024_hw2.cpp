/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw2.cpp
*compiled with jGRASP for initial development.
* (Still unable to test in Linux at the moment).
*/

/*
*Homework 002: Interest Calculations!
*/

#include <iostream>
#include <iomanip>
using namespace std;



//main method; no other custom methods required
int main()
{
		//monthly interest rate is 1/12th of yearly interest rate; two variables needed, set in do-while loop
		double monthlyInterestRate = 0, yearlyInterestRate = 0;
				
		float currentBalance = 0; //stores the current balance
		float monthlyIntDeducted = 0; //will be used to calculate $ of interest accrued each month
		float overallInterestPaid = 0; //combination of all "monthlyIntDeducted"; all interest paid. 
		
		int numberOfMonths = 0; //the number of months required to pay off loan
		float chosenMonthlyPayment = 0; //what the person will pay each month
		float principalPaid = 0; //the amount of principal paid during that month
		
		int widthColA = 9, widthColElse = 13; //used to automatically format output with proper padding
		
		bool failInterestVSPaymentCheck = true; //used in the do-while loop to check for validity
		
				
		//input loan information with a check for validity, hence the "do while" loop
		do
			{
			cout << "Loan Amount: ";
			cin >> currentBalance;
			//currentBalance = balanceInput; //stores the balance in currentBalance for calculations
		
			cout << "\nYearly interest Rate (% per *year*): ";
			cin >> yearlyInterestRate;
			yearlyInterestRate /= 100; //converts the percent to a usable decimal for calculation
			monthlyInterestRate = yearlyInterestRate / 12; //sets the monthly interest rate
			
			cout << "\nWhat will your *monthly* payments be? (enter, in dollars): ";
			cin >> chosenMonthlyPayment;
		
		
			
			//ensure that the payment covers the interest plus at least some of the loan amount
			//if the chosen monthly payment is insufficient, set a flag and run again
			if (chosenMonthlyPayment <= (monthlyInterestRate * currentBalance))
				{
				cout << "\nError: monthly payment does not cover loan amount + interest.\n";
				cout << "Please re-enter data:\n";
				failInterestVSPaymentCheck = true;
				}
			else //if everything is okay, there is no failure and the program will continue
				{
				failInterestVSPaymentCheck = false;
				}
			}
		while (failInterestVSPaymentCheck);
		
		
		//this segment performs calculations, then prints to screen with adequate formatting
		cout <<  "\n****************************************************\n"
				<< "\tAmortization Table\n"
				<< "****************************************************\n";
		
		cout << setiosflags(ios::left) << setw(widthColA) << "Month";
		cout << setiosflags(ios::left) << setw(widthColElse + 1) << "Balance";
		cout << setiosflags(ios::left) << setw(widthColElse) << "Payment";
		cout << setiosflags(ios::left) << setw(widthColElse) << "Rate (%)";
		cout << setiosflags(ios::left) << setw(widthColElse) << "Interest";
		cout << setiosflags(ios::left) << setw(widthColElse) << "Principal";
		
		cout << "\n";
		
		cout << setiosflags(ios::left) << setw(widthColA) << "0";
		cout << "$" << setiosflags(ios::left) << setw(widthColElse) << setiosflags(ios::fixed) << setprecision(2) << currentBalance;
		cout << setw(widthColElse) << "N/A";
		cout << setw(widthColElse) << "N/A";
		cout << setw(widthColElse) << "N/A";
		cout << setw(widthColElse) << "N/A";
		
		cout << "\n";
		
		//now perform calculations
		while (currentBalance > 0)
			{
			//figure out the interest on the balance remaining
			monthlyIntDeducted = currentBalance * monthlyInterestRate;
			overallInterestPaid += monthlyIntDeducted;
			
			//if a full payment is less than the balance plus interest chgd
			if (currentBalance + (monthlyIntDeducted) > chosenMonthlyPayment)
				{
				//the chosenMonthlyPayment will remain the same for this scenario
				//figure out the principal paid
				principalPaid = chosenMonthlyPayment - monthlyIntDeducted;
				//determine the new current balance after this month
				currentBalance -= principalPaid;
				}
			else //if a full payment is greater than or equal to the balance plus interest
				{
				//you actually MUST change the monthly payment variable, as this is the end of the cycle
				//this will be equal to the remaining balance, plus interest on that remaining balance
				chosenMonthlyPayment = currentBalance * (1 + monthlyInterestRate);
				//figure out the principal paid
				principalPaid = chosenMonthlyPayment - monthlyIntDeducted;
				//determine the new current balance after this month
				currentBalance -= principalPaid;
				}
			numberOfMonths++;
			//print out data for table
			cout << setiosflags(ios::left) << setw(widthColA) << numberOfMonths;
			cout << "$" << setiosflags(ios::left) << setw(widthColElse) << setiosflags(ios::fixed) << setprecision(2) << currentBalance;
			cout << "$" << setiosflags(ios::left) << setw(widthColElse - 1) << setiosflags(ios::fixed) << setprecision(2) << chosenMonthlyPayment;
			cout << setiosflags(ios::left) << setw(widthColElse) << setiosflags(ios::fixed) << setprecision(2) << (monthlyInterestRate * 100);
			cout << "$" << setiosflags(ios::left) << setw(widthColElse - 1) << setiosflags(ios::fixed) << setprecision(2) << monthlyIntDeducted;
			cout << "$" << setiosflags(ios::left) << setw(widthColElse) << setiosflags(ios::fixed) << setprecision(2) << principalPaid;
			cout << "\n";
			}//end while loop
				
		cout << "\nIt takes " << numberOfMonths << " months to pay off the loan.\n";
		cout << "Total interest paid is: $" << overallInterestPaid;
		
		return 0;
}