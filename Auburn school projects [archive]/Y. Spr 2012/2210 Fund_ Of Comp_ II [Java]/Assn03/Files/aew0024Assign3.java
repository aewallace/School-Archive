//main class for user interaction
import java.util.Scanner;

public class aew0024Assign3
{
	/*
	*Virtual Params (Parsed in this order):
	*@param k : the minimum number of characters to choose as
	* ...a seed from "source". Also, check for k>0; else error.
	*@param length : The tentative length of "result". Also, check for length>0; else error.
	*@param source : the name of the source file
	*@param result : the name of the output file
	*/
	
	//NOTE: the command line is really used for value setting
	//You are NOT asked to input values...just because that would make too much sense.
	
	public static void main(String[] args)
	{
	int k = 0;
	int length = 0;
	String source = "";
	String result = "";
	
	System.out.println("If you entered variables as command "
		+ "line arguments, press enter to continue. If you need to change "
		+ "or enter variables, please enter CHNG.");
	Scanner scan = new Scanner(System.in);
	String runInterfaceMore = scan.nextLine();
	if (runInterfaceMore.equals("CHNG"))
		{
		System.out.println("Please enter the value for k, the seed length:");
		k = scan.nextInt();
		System.out.println("Please enter the int value for target output length:");
		length = scan.nextInt();
		System.out.println("Please enter the name of the source file:");
		source = scan.nextLine();
		System.out.println("Please enter the name of the output file:");
		result = scan.nextLine();
		}
	
	if (args.length > 0)
		{
		k = Integer.parseInt(args[0]);
		length = Integer.parseInt(args[1]);
		source = args[2];
		result = args[3];
		}
	
	WordPhraseProducer workWPD = new WordPhraseProducer();
	String fileRead, fileWrite;
	boolean exitNow = false;
	int exitSet = 0, noExitIfMatched = 4;
	
	if (k < 0) {
		System.out.println("The target seed length is not a valid target.");
		exitNow = true;
		exitSet++;
		}
	if (length < 0){
		System.out.println("The target output length is not a valid target.");
		exitNow = true;
		exitSet++;
		}
	if (source == null || source.length() < 0)
		{
		exitNow = true;
		exitSet++;
		//do something
		}
	if (result == null || result.length() == 0)
		{
		exitSet++;
		exitNow = true;
		//do something
		}
	
	//if criteria are not met (ignores all blank input)
	//will exit
	if (exitSet != noExitIfMatched && exitNow)
		{
		System.out.println("One or more parameters were not met for proper processing."
			+ "\n\rNumber of errors: " + exitSet + " problems. Exiting...");
		return;
		}
	
	if (length < k)
		{
		System.out.println("Base seed size exceeds intended length. Exiting...");
		return;
		}
	//sets the INPUT file name
	if (source == null || source.length() < 0)
		{
		source = "banana.txt";
		}
		
	//try to find the file...
	//if fails, will exit with message
	boolean continueFwd = workWPD.openFile(source);
	if (!continueFwd)
		{
		System.out.println("Attempt at finding source "
			+ source + " failed. Please restart program to try again.");
		return;
		}
	
	
	//checks to see if character counts are fine
	//if not fine, will exit.
	boolean runIfCharLthWorks = workWPD.charCheck(k);
	if (!runIfCharLthWorks)
		{
		System.out.println("The minimum length of " + k
			+ " characters was not met. Exiting...");
		return;
		}
	//do this if everything checks out fine
	
	//set the output file
	if (result == null || result.length() == 0)
		{
		result = "output.txt";
		}
	
	//process everything; DOES NOT WRITE FILE!
	workWPD.processingMiddleMan(k, length);
	
	//finally write the file
	workWPD.writeFile(result);
	}


}