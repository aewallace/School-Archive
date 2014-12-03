#include <iostream>
#include <vector>
#include <ctype.h>

class BankSystem {
public:
	BankSystem();
	~BankSystem();
	bool initialize();
	bool callLogin();
	bool callMenu();
	bool continueRunning();
	void endProgram();
private:
	string defaultMenu_Filename;
	Menu mainMenu;
	string* menuOptions;
	StaffFocus StaffSubsys;
	ClientAccountFocus clientaccountSubsys;
	
};

class SystemLogin { //allows for login or logout objects
public:
	SystemLogin();
	~SystemLogin();
private:
};

class Menu { //allows for menu objects
public:
	Menu();
	~Menu();
	bool setOptions(string[] optionsIn);
	int displayOptions();
	bool runMenu();
private:
	int numberOfOptions;
	int lastChosenOption;
	vector<string> options;
};
class ClientAccountFocus{
public:
	ClientAccountFocus();
	~ClientAccountFocus();
private:
	AccountDataBase accounts;
	ClientDataBase clients;
	string clientDB_Filename;
	string accountDB_Filename;
	string* caMenuOptions;
};
class ClientDataBase { //makes provisions for a collection of clients
public:
	ClientDataBase();
	ClientDataBase(int entries, string[] namesIn, string[] residences, int[] SSNs, string[] employerIn, int[] numAssocAccountsIn, int[] accountsByID, int[] byIndex);
	~ClientDataBase();
	bool writeCDB();
	vector<int> addClient();
	vector<int> deleteClient();
	vector<int> editClient();
private:
	vector<Client> clientDB;
};
	
class Client { //makes provisions for clients to be supported
public:
	bool removeAccountAssn(int accountNumber);
	vector<int> associatedAccountsByIndex;
	vector<int> associatedAccountsByID;
	string nameOfClient, residenceOfClient, employer;
	int sSN_of_client, numAssocAccounts;

};

class AccountDataBase { //makes provisions for a collection of accounts
public:
	AccountDataBase();
	AccountDataBase(int entries, int[] numAssocNamesIn, string[] namesIn, int[] cliIndex, int[] accountnumber, int[] accounttype, double[] accountbalance);	
	~AccountDataBase();
	bool writeADB();
	vector<int> addAccount();
	vector<int> deleteAccount();
	vector<int> editAccount();
private:
	vector<Account> accountDB;
};

class Account { //makes provisions for clients' accounts to be supported
public:
	bool removeClientAssn(int clientNumber);
	vector<int> associatedClientsByIndex;
	vector<string> assciatedClientsByName;
	int numAssocNames, account_number, account_type;
	
	double account_balance;
};
class StaffFocus {
public:
	StaffFocus();
	~StaffFocus();
private:
	StaffDataBase staffers;
	string staffDB_Filename;
	string* sMenuOptions;
};			

class StaffDataBase {
public:
	StaffDataBase();
	~StaffDataBase();
	vector<staff> staffDB;
	bool addStaff();
	bool deleteStaff();
}
class Staff { //makes provisions for staff members -- including administrators -- to be supported
public:
	Staff();
	Staff(bool setAsAdmin, string password, string name);
	~Staff();
	StaffRole getStaffRole();
	bool lock(bool isLockedIn);
	boot isLockedCheck();
	string getName();
	int checkPass(string passIn);
private:
	StaffRole role;
	string name;
	Password passwordSet;
};
struct StaffRole { //allows for a staff member to be defined as a specific role, and sets up exactly what that role is

	bool isAdmin; //if true, administrator privileges will be granted in all menus. Else, simplify
	bool isLocked; //this is where we will store whether or not a user has been blocked out of the system
};

class Password { //allows for password objects
public:
	Password();
	~Password();
	bool setPassword();
	bool isPassword(string attempt);
private:
	string decypher();
	char* pHashA;
	char* pHashB;
	int length;
};


//******************************************************************************************************************************************************************
bool checkInput(string input);
//******************************************************************************************************************************************************************

//BankSystem class functions
BankSystem::BankSystem() {
	
}
BankSystem::~BankSystem(){
	delete [] menuOptions;
}
bool BankSystem::initialize(){
}
bool BankSystem::callLogin(){
}
bool BankSystem::callMenu(){
	mainMenu.runMenu();
}
bool BankSystem::continueRunning(string restOfMessage){
	string perform;
	
	cout << "Would you like to " << restOfMessage << "?\n";
	cout << "(YES to perform action, NO to break):";
	getline(cin, perform);
	for (int i = 0; i < mystr.length(); i++)
		{
			mystr[i] = tolower(mystr[i]);
		}
	if (0 != mystr.compare("yes"))
		{
			return false;
		}
	return true;
}
//SystemLogin class functions
SystemLogin::SystemLogin(){
}
SystemLogin::~SystemLogin(){
}
bool SystemLogin::getCheckCredentials(vector<staff>& staffDB){
	bool notSuccessfulAtName = true, notSuccessfulAtPass;
	int maxTries = 10, tries = 0;
	string tempName, tempPass;
	int indexToCheck = -1;
	while(notSuccessfulAtName){
		cout << "Please input user ID: ";
		getline(cin,tempName);
		cout << "\n";
		for (int i = 0; i < staffDB.size(); i++) {
			if (0 == tempName.compare(staffDB[i].getName())){
				notSuccessfulAtName = false;
				indexToCheck = i;
				activeName = tempName;
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
		while (notSuccessfulAtPass || tries <= maxTries) {
			cout << "Please enter password: ";
			//this is where we will have to mask password during input
			getline(cin, tempPass);
			cout << "\n";
			if(!staffDB[i].checkPassword(tempPass))
			{
				tries++;
				cout << "You have " << maxTries - tries << " attempts left before being locked out.\n";
			}
			else
			{
				notSuccessfulAtPass = false;
			}
		}
		
		if (notSuccessfulAtPass && tries > maxTries) {
			staffDB[i].lock(true);
			cout << "User locked out until reset by administrator.\n";
		}
		
	}
	return !notSuccessfulAtPass;
}
//Menu class functions
Menu::Menu(){
}
Menu::~Menu(){
}
bool Menu::setOptions(string[] optionsIn){
	for (int i = 0; i < optionsIn.size(); i++) {
		options.push_back(optionsIn[i]);
	}
	return true;
}
int Menu::displayOptions(){
	int selection;
	cout << "To exit this menu, enter -1 at the prompt. Else, choose a selection:\n";
	for (int i = 0; i < numberOfOptions; i++)
	{
		cout << options[i];
	}
	cin>>selection;
	cin.ignore(1000,"");
	return selection;
}
bool Menu::runMenu(){
	if (numberOfOptions == 0) {
		cout << "This menu has not been set up. Please check code and try again. [RMB]\n:";
	}
}
//ClientAccountFocus class functions
ClientAccountFocus::ClientAccountFocus(){
}
ClientAccountFocus::~ClientAccountFocus(){
}
//ClientDataBase class functions
ClientDataBase::ClientDataBase(){
}
ClientDataBase::ClientDataBase(int entries, string[] namesIn, string[] residences, int[] SSNs, string[] employerIn, int[] numAssocAccountsIn, int[] accountsByID, int[] byIndex)
{int acctIndex = 0;
	for (int i = 0; i <= entries - 1; i++){
		clientDB.push_back(new Client())
		for(int j = 0; j < numAssocAccounts[i - 1]; j++)
		{
			clientDB[i].associatedAccountsByID.push_back(accountsByID[acctIndex]);
			clientDB[i].associatedAccountsByIndex.push_back(byIndex[acctIndex]);
			acctIndex++;
		}
		numAssocAccounts = numAssocAccountsIn[i];
		nameOfClient = namesIn[i];
		residenceOfClient = residences[i];
		sSN_of_client = SSNs[i];
		employer = employerIn[i];
		
}}
ClientDataBase::~ClientDataBase(){
	delete [] clientDB;
}
bool ClientDataBase::writeCDB(){
}

//Client class functions
Client::Client(){
	vector<int> associatedAccountsByIndex;
	vector<int> associatedAccountsByID;
	string nameOfClient, residenceOfClient, employer;
	int sSN_of_client, numAssocAccounts;
}
Client::~Client(){
	delete [] associatedAccountsByIndex;
	delete [] associatedAccountsByID;
}
//AccountDataBase class functions
AccountDataBase::AccountDataBase(){
}
AccountDataBase::AccountDataBase(int entries, int[] numAssocNamesIn, string[] namesIn, int[] cliIndex, int[] accountnumber, int[] accounttype, double[] accountbalance)
{int nameIndex = 0;
for (int i = 0; i <= entries - 1; i++){
	accountDB.push_back(new Account())
	for(int j = 0; j < numAssocNames[i - 1]; j++)
	{
		accountDB[i].associatedClientsByName.push_back(namesIn[nameIndex]);
		accountDB[i].associatedClientsByIndex.push_back(cliIndex[nameIndex]);
		nameIndex++;
	}
	numAssocNames = numAssocNamesIn[i]
	account_number = accountnumber[i];
	account_type = accounttype[i];
	account_balance = accountbalance[i];
	
}}
AccountDataBase::~AccountDataBase(){
	delete [] accountDB;
}
bool AccountDataBase::writeADB(){
}
vector<int> addAccount(){
}
vector<int> deleteAccount(){
}
vector<int> editAccount(){
	int accountAndIndexNumber;
	cout << "Please enter account number to edit: ";
	cin >> accountAndIndexNumber;
	cin.ignore(1000,'');
	if (accountAndIndexNumber >= accountDB.size())
		return -1;
	else {
		accountDB[accountAndIndexNumber].
	}
}
//Account class functions
Account::Account(){
	vector<int> associatedClientsByIndex;
	vector<string> assciatedClientsByName;
	int numAssocNames, account_number, account_type;
	double account_balance;
}
Account::~Account(){
	delete [] associatedClientsByIndex;
	delete [] assciatedClientsByName;
}
//StaffFocus class functions
StaffFocus::StaffFocus(){
}
StaffFocus::~StaffFocus(){
}
//StaffDataBase class functions
StaffDataBase::StaffDataBase() {
}
StaffDataBase::StaffDataBase(int entries, string[] namesIn, string[] pswdIn, bool[] isAdmin, bool[] isLocked)
{
	/*
	 StaffRole role;
	 string name;
	 Password passwordSet;
	 */
	for (int i = 0; i <= entries - 1; i++){
		staffDB.push_back(new Staff(isAdmin[i], pswdIn[i], namesIn[i]))
		staffDB[i].lock(isLocked);
}}
StaffDataBase::~StaffDataBase(){
	delete [] staffDB;
}
//Staff class functions
Staff::Staff(){
	role.isAdmin = false;
	name = "[default/not set]";
}
Staff::Staff(bool setAsAdmin, string password, string name)
{
	role.isAdmin = setAsAdmin;
	if (!checkInput(name)) {
		cout << "Default name set. [BSSPSNn]\n";
		name = "[default/not set]";
	}
	else {
		name = name;
	}
	if (!checkInput(password) {
		cout << "Default password set. [BSSPSNp]\n";
	}
	else {
		passwordSet.setPassword(password);
	}
}
boot Staff::isLockedCheck(){
	return role.isLocked;
}
bool Staff::lock(bool isLockedIn)
	{
		role.isLocked = isLockedIn;
		return isLockedIn;
	}
string getName(){
	return name;
	}
Staff::~Staff(){
	
}
bool checkPass(string passIn){
	return passwordSet.isPassword(passIn);
}
StaffRole Staff::getStaffRole(){
	StaffRole temporaryRole;
	temporaryRole.isAdmin = role.isAdmin;
	temporaryRole.isLocked = role.isLocked;
	return temporaryRole;
}
//Password class functions
Password::Password(){
	if (!setPassword("001100110011")) {
		cout << "!!! Default not set! Coding error! [GC]\n";
	}
}
Password::Password(string newPass){
	if(!setPassword(newPass))
	{
		cout << "Error: Password not set to desired!\n";
		if (!setPassword("001100110011")) {
			cout << "!!! Default not set! Coding error! [SNP]\n";
		}
		else{
			cout << "Default used.\n";
		}
	}
}
Password::~Password(){
	delete [] phashA;
	delete [] pHashB;
}
bool Password::setPassword(string newPass){
	if (newPass.length() < 4) {
		return false;
	}
	if (newPass.length()%2 = 0) {
		pHashA = new char[newPass.length() / 2];
		pHashB = new char[newPass.length() / 2];
	}
	else {
		pHashA = new char[newPass.length()/2];
		pHashB = new char[newPass.length()/2];
		pHashA[newPass.length()/2 - 1] = '1';
	}
	length = newPass.length();
	return true;

}
String Password::decypher(){
	string output = "";
	for (int i = 0; i < pHashA.size() + pHashB.size() - 2; i++) {
		if (i % 2 = 0)
		{
			output += pHashB[i/2];
		}
		else if (i < pHashA.size() + pHashB.size() - 3)
			output += pHashA[(i-1)/2];
		}
		else if (length % 2 = 0) {
			output += pHashA[(i-1)/2];
		}
		else {
			//do nothing; discard last character
		}
	}
	return output;
}
bool Password::isPassword(string attempt){
	if(decypher().compare(attempt) == areEqual)
		return true;
	else {
		return false;
	}

}










//***unassociated methods
bool checkInput(string input){
	bool itsOkay = false;
	for (int i = 0; i < input.size(); i++) {
		if (0 != isalnum(input.at(i)))
		{
			return false;
		}
	}
	itsOkay = true;
	return itsOkay;
}
//************MAIN****************
int main(){
	bool doRun = true;
	BankSystem Teller;
while (doRun){
	
	
	
doRun = Teller.continueRunning()}
	return 0;
}