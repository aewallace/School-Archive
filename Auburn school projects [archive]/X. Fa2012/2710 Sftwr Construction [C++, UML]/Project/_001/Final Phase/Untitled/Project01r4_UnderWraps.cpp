/*
*Albert Wallace
*aew0024@tigermail.auburn.edu
*aew0024_hw6.cpp
*written with Vi in Linux & jGRASP in Mac OS X 10.6.
*compiled using default tools on both platforms
*/

/*****************************
 *Project 001: (Not so) Secure Teller Terminal System
 * (also, not so functional)
 ****************************/

#include <iostream>
#include <vector>
#include <ctype.h>
#include <stdio.h>
#include <termios.h>
#include <unistd.h>

using namespace std;

struct StaffRole { //allows for a staff member to be defined as a specific role, and sets up exactly what that role is
	
	bool isAdmin; //if true, administrator privileges will be granted in all menus. Else, simplify
	bool isLocked; //this is where we will store whether or not a user has been blocked out of the system
};

class Password { //allows for password objects
public:
	Password();
	~Password();
	Password(string newPass);
	bool setPassword(string newPass);
	bool isPassword(string attempt);

	string decypher();
	string wordpass;
	int length;
};

class Staff { //makes provisions for staff members -- including administrators -- to be supported
public:
	Staff();
	Staff(bool setAsAdmin, string password, string name);
	~Staff();
	StaffRole getStaffRole();
	bool lock(bool isLockedIn);
	bool isLockedCheck();
	string getName();
	bool checkPass(string passIn);
	bool changePswd();

	StaffRole role;
	string name;
	Password passwordSet;
};


class SystemLogin { //allows for login or logout objects
public:
	SystemLogin();
	~SystemLogin();
	int getCheckCredentials(vector<Staff>& staffDB, bool& asAdmin);
private:
	Staff currentStaff;
};

class Menu { //allows for menu objects
public:
	Menu();
	~Menu();
	Menu(string optionsIn[], int numOptsIn);
	bool setMenuTitle(string nameOfMenu);
	bool setOptions(string optionsIn[], int numOptsIn);
	int displayOptions();
	bool runMenu();
private:
	int numberOfOptions;
	int lastChosenOption;
	string menuTitle;
	vector<string> options;
};



class Client { //makes provisions for clients to be supported
public:
	Client();
	~Client();
	Client(vector<int> acctByIndex, vector<int> acctByID, string name, string residence, string employerIn, int SSN, int NumAssocAcct);
	bool removeAccountAssn(int accountNumber);
	vector<int> associatedAccountsByIndex;
	vector<int> associatedAccountsByID;
	string nameOfClient, residenceOfClient, employer;
	int sSN_of_client, numAssocAccounts;
	bool associateWithAccount(int index, int ID);

};

class Account { //makes provisions for clients' accounts to be supported
public:
	Account();
	~Account();
	Account(int accountNo, bool isCheckingIn, double initialBalance);
	bool removeClientAssn(int clientNumber);
	vector<int> associatedClientsByIndex;
	vector<string> associatedClientsByName;
	int numAssocNames, account_number;
	bool isChecking, isSavings;
	double addCredit(double amountUp);
	double checkBalance();
	double deductCredit(double amountDown);
	bool associateWithClient(int index, string name);

	double account_balance;
};


class ClientDataBase { //makes provisions for a collection of clients
public:
	ClientDataBase();
	ClientDataBase(vector<Client>& cDB);
	ClientDataBase(int entries, string namesIn[], string residences[], int SSNs[], string employerIn[], int numAssocAccountsIn[], int accountsByID[], int byIndex[]);
	~ClientDataBase();
	bool writeCDB();
	bool addClient();
	//vector<int> deleteClient();
	bool editClient();
	vector<Client> clientDB;
	vector<Account> acDB; //make sure to set this up as soon as the database is created/restored
};


class AccountDataBase { //makes provisions for a collection of accounts
public:
	AccountDataBase();
	AccountDataBase(vector<Account>& aDB);
	AccountDataBase(int entries, int numAssocNamesIn[], string namesIn[], int cliIndex[], int accountnumber[], int isCheckingType[], double accountbalance[]);
	int addAccount();
	~AccountDataBase();
	bool writeADB();
	//int deleteAccount();
	int editAccount();
	
	vector<Account> accountDB;
	vector<Client> cdBIn;
};

class ClientAccountFocus{
public:
	ClientAccountFocus();
	~ClientAccountFocus();
	ClientAccountFocus(ClientDataBase& cDB_primary, AccountDataBase& aDB_primary);
	bool runMenu();
	AccountDataBase accounts; //be sure to pass these in and save as soon as possible
	ClientDataBase clients; //be sure to pass these in and save as soon as possible
private:
	string clientDB_Filename;
	string accountDB_Filename;
	Menu CAFocusMenu;
};


class StaffDataBase {
public:
	StaffDataBase();
	~StaffDataBase();
	StaffDataBase(int entries, string namesIn[], string pswdIn[], bool isAdmin[], bool isLocked[]);
	vector<Staff> staffDB;
	bool addStaff();
	bool deleteStaff();
	bool reviewAllStaff();
};

class StaffFocus {
public:
	StaffFocus();
	~StaffFocus();
	int displayMenu();

	StaffDataBase staffers;
	string staffDB_Filename;
};		

class BankSystem {
public:
	BankSystem();
	~BankSystem();
	bool initialize();
	bool callLogin();
	bool callMenu();
	void endProgram();
private:
	string defaultMenu_Filename;
	Menu mainMenu;
	bool loggedInAsAdminType;
	int currentLoggedUser;
	string* menuOptions;
	StaffFocus StaffSubsys;
	ClientAccountFocus clientaccountSubsys;
	ClientDataBase cDB_primary;
	AccountDataBase aDB_primary;
	StaffDataBase sDB_primary;
	SystemLogin loginPortal;
	//vector<Staff> staffDB;
	
};

//******************************************************************************************************************************************************************
//independent function declarations
bool checkInput(string input);
string getPswd();
int mygetch(void);
bool yesORno(string restOfMessage);
int mygetch (bool clr); 
//******************************************************************************************************************************************************************

//BankSystem class functions
BankSystem::BankSystem() {
	sDB_primary.staffDB.push_back(Staff(true, "0000", "admin"));
	StaffSubsys.staffers = sDB_primary;
}
BankSystem::~BankSystem(){
	delete [] menuOptions;
}
bool BankSystem::initialize(){
	string* input;
	int numOptForAdmin = 4;
	int numOptForGenStaff = 3;
	int numToPass = 0;
	if (loggedInAsAdminType)
	{
		input = new string[numOptForAdmin];
		input[0] = "Manage Branch Staff Database";
		input[1] = "Manage Client & Account Databases";
		input[2] = "Manage your login credentials.";
		input[3] = "Log out of system.";
		numToPass = numOptForAdmin;
	}
	else //if not logged in as an administrator
	{
		input = new string[numOptForGenStaff];
		input[0] = "Manage Client & Account Databases";
		input[1] = "Manage your login credentials.";
		input[2] = "Log out of system.";
		numToPass = numOptForGenStaff;
	}
	return mainMenu.setOptions(input, numToPass);
}
bool BankSystem::callLogin(){
	currentLoggedUser = loginPortal.getCheckCredentials(sDB_primary.staffDB, loggedInAsAdminType);
	if (currentLoggedUser < 0) {
		return false;
	}
	return true;
}
bool BankSystem::callMenu(){
	int option;
	option = mainMenu.displayOptions();
	
	if (option == -1)
		return false;
	else if (option == 0 && loggedInAsAdminType)
	{StaffSubsys.displayMenu();}
	else if (option == 0 && !loggedInAsAdminType)
	{clientaccountSubsys.runMenu();}
	else if (option == 1 && loggedInAsAdminType)
	{clientaccountSubsys.runMenu();}
	else if (option == 1 && !loggedInAsAdminType)
	{StaffSubsys.staffers.staffDB[currentLoggedUser].changePswd();}
	else if (option == 2 && loggedInAsAdminType)
	{StaffSubsys.staffers.staffDB[currentLoggedUser].changePswd();}
	else if (option == 2 && !loggedInAsAdminType)
	{return true;}
	else if (option == 3 && loggedInAsAdminType)
	{return true;}

	return true;
}
void BankSystem::endProgram(){
	//unused
}
					  
//SystemLogin class functions
SystemLogin::SystemLogin(){
}
SystemLogin::~SystemLogin(){
}
int SystemLogin::getCheckCredentials(vector<Staff>& staffDB, bool& asAdmin){
	bool notSuccessfulAtName = true, notSuccessfulAtPass = true;
	int maxTries = 10, tries = 0;
	string tempName, tempPass;
	int indexToCheck = -1;
	while(notSuccessfulAtName){
		cout << "Please input user ID: ";
		//getline(cin,tempName);
		cin >> tempName;
		cout << "\n";
		for (int i = 0; i < staffDB.size() && notSuccessfulAtName; i++) {
			if (0 == tempName.compare(staffDB[i].getName())){
				notSuccessfulAtName = false;
				indexToCheck = i;
				currentStaff = staffDB[i];
			}
			
		}
		if (notSuccessfulAtName){
				cout << "Name not found; please try again.\n";
		}
	}
	if(indexToCheck > -1 && staffDB[indexToCheck].isLockedCheck())
	{
		cout << "User locked out until reset by administrator.\n";
	}
	else if(indexToCheck > -1 && !staffDB[indexToCheck].isLockedCheck())
	{
		while (notSuccessfulAtPass && tries <= maxTries) {
			cout << "Please enter password: ";
			//this is where we will have to mask password during input
			tempPass = getPswd();
			cout << "\n";
			if(!currentStaff.checkPass(tempPass))
			{
				tries++;
				cout << "You have " << maxTries - tries << " attempts left before being locked out.\n";
			}
			else
			{
				notSuccessfulAtPass = false;
				asAdmin = currentStaff.getStaffRole().isAdmin;
			}
		}
		
		if (notSuccessfulAtPass && tries > maxTries) {
			currentStaff.lock(true);
			cout << "User locked out until reset by administrator.\n";
		}
		
		staffDB[indexToCheck] = currentStaff;
		
	}
	return indexToCheck;
}
//Menu class functions
Menu::Menu(){
}
Menu::~Menu(){
}
Menu::Menu(string optionsIn[], int nOptsIn){
	setOptions(optionsIn, nOptsIn);
}
bool Menu::setMenuTitle(string nameOfMenu){
	menuTitle = nameOfMenu;
	return true;
}
bool Menu::setOptions(string optionsIn[], int numOptsIn){
	for (int i = 0; i < numOptsIn; i++) {
		options.push_back(optionsIn[i]);
	}
	numberOfOptions = numOptsIn;
	return true;
}
int Menu::displayOptions(){
	int selection;
	cout << "\n" << menuTitle;
	
	cout << "\n****************************************************\n";
	
	cout << "To cancel & exit this menu, enter -1 at the prompt. Else, choose a selection:\n";
	for (int i = 0; i < numberOfOptions; i++)
	{
		cout << "[" << i << "]: " << options[i];
		cout << "\n";
	}
	cout << "Selection...: ";
	cin>>selection;
	cin.ignore(1000,'\n');
	cout << "\n****************************************************\n";
	return selection;
}
bool Menu::runMenu(){
	if (numberOfOptions == 0) {
		cout << "This menu has not been set up. Please check code and try again. [RMB]\n:";
	}
	//this method unfinished & unnecessary
	return false;
}
//ClientAccountFocus class functions
ClientAccountFocus::ClientAccountFocus()
{
	//clients = cDB_primary;
	//accounts = aDB_primary;
	CAFocusMenu.setMenuTitle("Client & Account Management");
	int numOpt = 4;
	string menuOpt[numOpt];
	menuOpt[0]="Add Client";
	menuOpt[1]="Edit Client Info";
	menuOpt[2]="Add Account";
	menuOpt[3]="Manage/Edit Account Status";
	CAFocusMenu.setOptions(menuOpt, numOpt);
}
ClientAccountFocus::ClientAccountFocus(ClientDataBase& cDB_primary, AccountDataBase& aDB_primary){
	clients = cDB_primary;
	accounts = aDB_primary;
	CAFocusMenu.setMenuTitle("Client & Account Management");
	int numOpt = 4;
	string menuOpt[numOpt];
	menuOpt[0]="Add Client";
	menuOpt[1]="Edit Client Info";
	menuOpt[2]="Add Account";
	menuOpt[3]="Manage/Edit Account Status";
	CAFocusMenu.setOptions(menuOpt, numOpt);
}
ClientAccountFocus::~ClientAccountFocus(){
}
bool ClientAccountFocus::runMenu(){
	int choice = 0;
	while (choice != -1){
		choice = CAFocusMenu.displayOptions();
		if (choice == -1) {
			return false;
		}
		if (choice == 0) {
			//add client
			clients.addClient();
		}
		else if (choice == 1) {
			//edit client
			clients.editClient();
		}
		else if (choice == 2) {
			//add account
			accounts.addAccount();
		}
		else if (choice == 3) {
			//manage account
			accounts.editAccount();
		}
	}
	return true;
}
//ClientDataBase class functions
ClientDataBase::ClientDataBase(){
}
ClientDataBase::ClientDataBase(int entries, string namesIn[], string residences[], int SSNs[], string employerIn[], int numAssocAccountsIn[], int accountsByID[], int byIndex[])
{int acctIndex = 0;
	
	for (int i = 0; i <= entries - 1; i++){
		clientDB.push_back(Client());
		for(int j = 0; j < numAssocAccountsIn[i]-1; j++)
		{
			clientDB[i].associatedAccountsByID.push_back(accountsByID[acctIndex]);
			clientDB[i].associatedAccountsByIndex.push_back(byIndex[acctIndex]);
			acctIndex++;
		}
		clientDB[i].numAssocAccounts = numAssocAccountsIn[i];
		clientDB[i].nameOfClient = namesIn[i];
		clientDB[i].residenceOfClient = residences[i];
		clientDB[i].sSN_of_client = SSNs[i];
		clientDB[i].employer = employerIn[i];
		
}}
ClientDataBase::~ClientDataBase(){
}
bool ClientDataBase::addClient(){
	cout << "\n";
	string namae;
	cout << "Please enter the name of the new client: ";
	getline(cin, namae);
	cout << "\n";
	string residency;
	cout << "Please enter the residence of the new client: ";
	getline(cin, residency);
	cout << "\n";
	string employerR;
	cout << "Please enter the name of new client's employer: ";
	getline(cin, employerR);
	cout << "\n";
	
	int numAssociations;
	cout << "Please enter the number of accounts you want to associate with the client: ";
	cin >> numAssociations;
	
	vector<int> aByIndex;
	vector<int> aByID;
	int IDtoFind;
	for (int i = 0; i < numAssociations; i++)
	{
		cout <<"\nPlease enter associated account number " << i << ",by ID: ";
		cin >> IDtoFind;
		cout << "\n";
		bool notFound = true;
		int numIndexToAssoc = -15;
		for (int j = 0; j < acDB.size() && notFound; j++) {
			if (acDB[j].account_number == IDtoFind) {
				notFound = false;
				numIndexToAssoc = i;
			}
			else {
				numIndexToAssoc = -1;
			}
		}
		if (notFound){
			cout << "Could not perform association. Please try with another number.\n";
		}
		else if (!notFound && numIndexToAssoc > -1)
		{
			aByIndex.push_back(numIndexToAssoc);
			aByID.push_back(IDtoFind);
		}
	}
	
	int ssnN;
	cout << "Please nter the Social Security Number for the new client:  ";
	cin >> ssnN;
	cin.ignore(1000,'\n');
							//now we have name, address, employer, associated accounts, SSN. 
							//we must create the new object in the CDB vector
	clientDB.push_back(Client(aByIndex, aByID, namae, residency, employerR, ssnN, numAssociations));
	return true;
}
bool ClientDataBase::editClient(){
	string findName;
	cout << "Please enter name of client to edit: ";
	getline(cin, findName);
	cout << "\n";
	bool notFound = true;
	int indexToEdit = -1;
	for (int r = 0; r < clientDB.size() && notFound; r++) {
		if (clientDB[r].nameOfClient.compare(findName) == 0) {
			notFound = false;
			indexToEdit = r;
		}
	}
	
	if (notFound) {
		cout << "Client not found.\n";
		return false;
	}
	int nOpts = 3;
	string mnuOpts[nOpts];
	mnuOpts[0] = "Address";
	mnuOpts[1] = "Employer";
	mnuOpts[2] = "SSN";
	Menu editClientMenu(mnuOpts, nOpts);
	editClientMenu.setMenuTitle("Client Information Editing");
	int runThis = editClientMenu.displayOptions();
	
	Client thisClient;
	thisClient = clientDB[indexToEdit];
	
	if (runThis == -1) {
		return false;
	}
	
	else if(runThis == 0)
	{	
		cout << "Current address to overwrite: " << thisClient.residenceOfClient << "\n";
		cout << "Enter new address: ";
		getline(cin, thisClient.residenceOfClient);
		cout << "\nNew residence stored as: " << thisClient.residenceOfClient << "\n";
	}
	else if (runThis == 1){
		cout << "Current employer to overwrite: " << thisClient.employer << "\n";
		cout << "Enter new employer: ";
		getline(cin, thisClient.employer);
		cout << "\nNew employer stored as: " << thisClient.employer << "\n";
	}
	else if (runThis == 2) {
		cout << "Current SSN to overwrite: " << thisClient.sSN_of_client << "\n";
		cout << "Enter new SSN: ";
		cin >> thisClient.sSN_of_client;
		cin.ignore(1000,'\n');
	}
	else {
		return false;
	}

	return true;
	
}
bool ClientDataBase::writeCDB(){
	return false;
}

//Client class functions
Client::Client(){

}
Client::~Client(){
}
Client::Client(vector<int> acctByIndex, vector<int> acctByID, string name, string residence, string employerIn, int SSN, int NumAssocAcct){
	associatedAccountsByIndex = acctByIndex;
	associatedAccountsByID = acctByID;
	nameOfClient = name;
	residenceOfClient = residence;
	employer = employerIn;
	sSN_of_client = SSN;
	numAssocAccounts = NumAssocAcct;
}
bool Client::associateWithAccount(int index, int ID){
	index;
	ID;
	return true;
}
//AccountDataBase class functions
AccountDataBase::AccountDataBase(){
}
AccountDataBase::AccountDataBase(vector<Account>& aDB){
	accountDB = aDB;
}
AccountDataBase::AccountDataBase(int entries, int numAssocNamesIn[], string namesIn[], int cliIndex[], int accountnumber[], int isCheckingType[], double accountbalance[])
{
	int nameIndex = 0;
for (int i = 0; i <= entries - 1; i++){
	accountDB.push_back(Account());
	for(int j = 0; j < numAssocNamesIn[i] - 1; j++)
	{
		accountDB[i].associatedClientsByName.push_back(namesIn[nameIndex]);
		accountDB[i].associatedClientsByIndex.push_back(cliIndex[nameIndex]);
		nameIndex++;
	}
	accountDB[i].numAssocNames = numAssocNamesIn[i];
	accountDB[i].account_number = accountnumber[i];
	accountDB[i].isChecking = isCheckingType[i];
	accountDB[i].isSavings = !isCheckingType[i];
	accountDB[i].account_balance = accountbalance[i];
	
}}
AccountDataBase::~AccountDataBase(){
}
bool AccountDataBase::writeADB(){
	return false;
}
int AccountDataBase::addAccount(){
	/*bool removeClientAssn(int clientNumber);
	 vector<int> associatedClientsByIndex;
	 vector<string> assciatedClientsByName;
	 int numAssocNames, account_number;
	 bool isChecking, isSavings;
	 
	 double account_balance;*/
	string attdName;
	cout << "Please enter the name of the client to whom this account will belong: ";
	getline(cin, attdName);
	cout << "\n";
	int idxR = -5;
	bool cont = true;
	
	for (int gh = 0; gh < cdBIn.size() && cont; gh++)
	{
		if (cdBIn[gh].nameOfClient.compare(attdName) == 0) {
			idxR = gh;
			cont = false;
		}
	}
	
	if (idxR == -5 && cont) {
		return idxR;
	}
	
	cout << "Will this be a checking account?";
	bool isCheckingQ;
	isCheckingQ = yesORno("YES for checking, NO for savings");
	cout << "New Account ID: " << accountDB.size() <<".\n";
	int newID = accountDB.size();
	
	double iniBalance;
	cout << "What is the starting balance for this account? $";
	cin >> iniBalance;
	if (iniBalance < 0) {
		iniBalance = 0;
		cout << "Initial balance too low. Account set to zero.\n";
	}
	cin.ignore(1000, '\n');
	accountDB.push_back(Account(newID, isCheckingQ, iniBalance));
	accountDB.back().associateWithClient(idxR, attdName);
	
	cout << "Account successfully created.\n";
	
	return 0;
	
}
/*int deleteAccount(){
}*/ //not supported in this release
int AccountDataBase::editAccount(){
	int accountAndIndexNumber;
	Menu editAccountMenu;
	int optSize = 3;
	string menuOpt[optSize];
	menuOpt[0]="Deposit Money";
	menuOpt[1]="Withdraw Money";
	menuOpt[2]="Check balance on this account";
	//menuOpt[3]="Cancel [exit this menu]"; //covered by menu class; just implement properly with return = -1
	editAccountMenu.setOptions(menuOpt, optSize);
	editAccountMenu.setMenuTitle("Manage Checking or Savings Account");
	cout << "Please enter account number to manage: ";
	cin >> accountAndIndexNumber;
	cin.ignore(1000,'\n');
	if (accountAndIndexNumber >= accountDB.size()){
		return -1;
	}
	int chosenOption = -2;
	
	Account thisAccount;
	thisAccount = accountDB[accountAndIndexNumber];
	
	while (chosenOption != -2) {
		chosenOption = editAccountMenu.displayOptions();
		
		if (chosenOption == -1) {
			return chosenOption;
		}
		else if(chosenOption == 0){
			//depost money; no upper limit
			double amountIn;
			cout << "Enter amount to credit/deposit into account: $";
			cin >> amountIn;
			cin.ignore(1000,'\n');
			cout << "\n";
			if (amountIn <= thisAccount.addCredit(amountIn))
			{
				cout << "Amount successfully added.\n";
			}
		}
		else if(chosenOption == 1){
			double amountOut;
			if (thisAccount.checkBalance() <= 0) {
				cout << "Withdrawal not allowed; insufficient funds.\n";
				return -1;
			}
			cout << "Enter amount to withdraw from account: $";
			cin >> amountOut;
			cin.ignore(1000,'\n');
			if (thisAccount.deductCredit(amountOut) < 0)
			{
				cout << "Insufficient funds. Please check balance and try again.\n";
			}
		}
		else if(chosenOption == 2){
			cout << "Your current balance: $" << thisAccount.checkBalance() <<".\n";
		}
		else {
			return -1;
		}
		
		accountDB[accountAndIndexNumber] = thisAccount;

	}
	return -15;
}
//Account class functions
Account::Account(){
	/*bool removeClientAssn(int clientNumber);
	vector<int> associatedClientsByIndex;
	vector<string> assciatedClientsByName;
	int numAssocNames, account_number;
	bool isChecking, isSavings;
	
	double account_balance;*/
	isChecking = true;
	isSavings != isChecking;
	account_balance = 0;
	account_number = 0110;
}

Account::Account(int accountNo, bool isCheckingIn, double initialBalance){
	isChecking = isCheckingIn;
	isSavings != isCheckingIn;
	account_number = accountNo;
	account_balance = initialBalance;
}
Account::~Account(){
	
}
double Account::addCredit(double amountUp){
	account_balance += amountUp;
	return account_balance;
}
double Account::deductCredit(double amountDown){
	if (account_balance <= 0) {
		return -1;
	}
	else
	{
		if (account_balance - amountDown <= 0) {
			return -1;
		}
		else {
			account_balance -= amountDown;
			return account_balance;
		}

	}
}
bool Account::associateWithClient(int index, string name){
	associatedClientsByIndex.push_back(index);
	associatedClientsByName.push_back(name);
	return true;
}
double Account::checkBalance(){
	return account_balance;
}
//StaffFocus class functions~~~~~~~~~~~~~~~~~~~~~~~~
StaffFocus::StaffFocus(){
	
}
StaffFocus::~StaffFocus(){
}
int StaffFocus::displayMenu(){
	int numOpt = 3;
	string choices[numOpt];
	choices[0]="Add New Branch Staff or Administrator";
	choices[1] = "View All Current Branch Staff & Admin";
	choices[2] = "Delete Branch Staff or Administrator";
	Menu staffMenu(choices, numOpt);
	
	int qryopt = 0;
	while (qryopt >= 0) {
		qryopt = staffMenu.displayOptions();
		if (qryopt == -1) {
			return -1;
		}
		else if (qryopt == 0) {
			//add new branch staff
			staffers.addStaff();
		}
		else if (qryopt == 1) {
		//view branch staff	
			staffers.reviewAllStaff();
		}
		else if (qryopt == 2) {
		//delete branch staff
			staffers.deleteStaff();
		}
		else {
			return -1;
		}

	}
	return qryopt;
}
//StaffDataBase class functions~~~~~~~~~~~~~~~~~~~~~~
StaffDataBase::StaffDataBase() {
}
StaffDataBase::StaffDataBase(int entries, string namesIn[], string pswdIn[], bool isAdmin[], bool isLocked[])
{
	/*
	 StaffRole role;
	 string name;
	 Password passwordSet;
	 */
	for (int i = 0; i <= entries - 1; i++){
		staffDB.push_back(Staff(isAdmin[i], pswdIn[i], namesIn[i]));
		staffDB[i].lock(isLocked);
}}
StaffDataBase::~StaffDataBase(){
}
bool StaffDataBase::addStaff(){
	string nameOrID;
	string passwordT;
	bool isAnAdmin;
	cout << "Please enter the name/ID for the staff member: ";
	getline(cin, nameOrID);
	cout << "\n";
	if (!checkInput(nameOrID)) {
		cout << "Invalid name.\n";
		return false;
	}
	for (int vm = 0; vm < staffDB.size(); vm++) {
		if (0 == staffDB[vm].name.compare(nameOrID)) {
			nameOrID = "Name could not be added. User already exists.\n";
			return false;
		}
	}
	//else, assume nameOrID is valid
	cout << "Please enter the password for the staff member.";
	passwordT = getPswd(); //a helper method must be called
	
	cout << "\nPlease indicate if the user is an administrator.\n";
	isAnAdmin = yesORno("[YES for administrator, NO for general staff].");
	cout << "\n";
	return true;
}
bool StaffDataBase::deleteStaff(){
	string toDelete;
	cout << "Please enter the user name/ID to be deleted: ";
	getline(cin, toDelete);
	cout << "\n";
	bool notFound = true;
	
	if (toDelete.compare("admin") == 0) {
		cout << "Cannot delete default administrator.\n";
		return false;
	}
	
	for (int g = 0; g < staffDB.size() && notFound; g++) {
		if (0 == staffDB[g].name.compare(toDelete)) {
			staffDB.erase(staffDB.begin()+g);
			notFound = false;
		}
		else {
			notFound = true;
		}

	}
	if (notFound) {
		cout << "User not found. Database untouched.\n";
	}
	if (!notFound) {
		cout << "User deleted. Database edited. Please remember to save changes if writing to file.\n";
	}
	return !notFound;
}
bool StaffDataBase::reviewAllStaff()
{
	if (staffDB.size() < 1)
		return false;
	for (int i = 0; i << staffDB.size(); i++)
	{
		cout << "Name/ID: " << staffDB[i].name;
		if(staffDB[i].role.isAdmin)
		{
			cout << " ::: Role: System Administrator.\n";
		}
		else {
			cout << " ::: Role: General Staff Member.\n";
		}

	}
	return true;
}
//Staff class functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Staff::Staff(){
	role.isAdmin = false;
	name = "[default/not set]";
}
Staff::Staff(bool setAsAdmin, string password, string nameIn)
{
	role.isAdmin = setAsAdmin;
	if (!checkInput(nameIn)) {
		cout << "Default name set. [BSSPSNn]\n";
		name = "[default/not set]";
	}
	else {
		name = nameIn;
	}
	if (!checkInput(password)) {
		cout << "Default password set. [BSSPSNp]\n";
	}
	else {
		passwordSet.setPassword(password);
	}
}
bool Staff::isLockedCheck(){
	return role.isLocked;
}
bool Staff::lock(bool isLockedIn)
	{
		role.isLocked = isLockedIn;
		return isLockedIn;
	}
string Staff::getName(){
	return name;
	}
Staff::~Staff(){
	
}
bool Staff::checkPass(string passIn){
	return passwordSet.isPassword(passIn);
}
StaffRole Staff::getStaffRole(){
	StaffRole temporaryRole;
	temporaryRole.isAdmin = role.isAdmin;
	temporaryRole.isLocked = role.isLocked;
	return temporaryRole;
}
		
bool Staff::changePswd()
{
	cout << "Please enter intended new password: ";
	string intenty = getPswd();
	return passwordSet.setPassword(intenty);
}			
//Password class functions
Password::Password(){
	if (!setPassword("0000")) {
		cout << "!!! Default not set! Coding error! [GC]\n";
	}
}
Password::Password(string newPass){
	if(!setPassword(newPass))
	{
		cout << "Error: Password not set to desired!\n";
		if (!setPassword("0000")) {
			cout << "!!! Default not set! Coding error! [SNP]\n";
		}
		else{
			cout << "Default used.\n";
		}
	}
}
Password::~Password(){
}
bool Password::setPassword(string newPass){
	if (newPass.length() < 4) {
		return false;
	}
	wordpass = newPass;
	length = newPass.length();
	return true;

}
string Password::decypher(){
	string output = wordpass;
	return output;
}
bool Password::isPassword(string attempt){
	if(wordpass.compare(attempt) == 0)
		return true;
	else {
		return false;
	}

}










//***Independent function defintions
bool checkInput(string input){
	bool itsOkay = false;
	/*for (int i = 0; i < input.length() - 1; i++) {
		if (0 != isalnum(input[i]))
		{
			return false;
		}
	}*/
	itsOkay = true;
	return itsOkay;
}
/*Imported method to deal with hiding password input!
 *Plagiarism imminent!
 */
	/*
	 * This program shows how to hide passwords.
	 *
	 * 2012 Xiao Qin <xqin@auburn.edu>
	 *
	 * Samuel Ginn College of Engineering
	 * Auburn University, AL 36849-5347 
	 * http://www.eng.auburn.edu/~xqin/
	 *
	 */ 

	
		
int mygetch ( void ) 
	{
		int ch;
		struct termios oldt, newt;
		
		tcgetattr ( STDIN_FILENO, &oldt );
		newt = oldt;
		newt.c_lflag &= ~( ICANON | ECHO );
		tcsetattr ( STDIN_FILENO, TCSANOW, &newt );
		ch = getchar();
		tcsetattr ( STDIN_FILENO, TCSANOW, &oldt );
		
		return ch;
	} 
int mygetch (bool clr) 
	{
		int ch;
		struct termios oldt, newt;
		
		tcgetattr ( STDIN_FILENO, &oldt );
		newt = oldt;
		newt.c_lflag &= ~( ICANON | ECHO );
		tcsetattr ( STDIN_FILENO, TCSANOW, &newt );
		ch = getchar();
		tcsetattr ( STDIN_FILENO, TCSANOW, &oldt );
		
		return ch;
	} 		
string getPswd()
	{
		
		int ch;
		char pword[BUFSIZ];
		int i = 0;
		
		mygetch(true); //You must have this line. Otherwise the password segment below can NOT work!
		
		cout << "\n[Characters will be hidden.]";
		fflush(stdout);
		
		while ((ch = mygetch()) != EOF 
				&& ch != '\n' 
			   && ch != '\r' 
			   && i < sizeof(pword) - 1)
		{
			if (ch == '\b' && i > 0) 
			{
				cout << "\b \b";
				fflush(stdout);
				i--;
				pword[i] = '\0';
			}
			else if (isalnum(ch))
			{
				cout << '*';
				pword[i++] = (char)ch;
			}
		}
		
		pword[i] = '\0';
		
		string passOut = "";
		
		for (int lm = 0; lm < i /*to ignore the null char, don't do i+1 */; lm++)
		{
			passOut += pword[lm];
		}
		
		cout << "\n";
		
		return passOut;
	}
/*
 *End copied method
 */

bool yesORno(string restOfMessage){
	string perform;
	
	cout << restOfMessage;
	getline(cin, perform);
	cout << "\n";
	for (int i = 0; i < perform.length(); i++)
	{
		perform[i] = tolower(perform[i]);
	}
	if (0 != perform.compare("yes"))
		{
		return false;
		}
	return true; //else, return true
	}		
//************MAIN****************
int main(){
	bool doRun = true;
	BankSystem Teller;
while (doRun){
	
	doRun = Teller.callLogin();
	if (doRun) {
		
	Teller.initialize();
	Teller.callMenu();
	//rest of main goes here
	
}
	doRun = yesORno("Continue running? YES to continue, NO to exit.");}
	return 0;
}

