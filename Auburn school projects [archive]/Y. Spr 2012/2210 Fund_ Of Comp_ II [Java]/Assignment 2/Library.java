import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Library {
	
	private ArrayList<ArrayList<String>> library = new ArrayList<ArrayList<String>>();
	private ArrayList<ArrayList<String>> optLib = new ArrayList<ArrayList<String>>();
	private ArrayList<String> fOptLib = new ArrayList<String>();
	private File file = new File("sowpods.txt");
	private Lexicon lex = new Lexicon(file);
	private boolean optRun = false;
	private int optSafeSet = -15;
	
	public Library()
	{
		try
		{
		    Scanner scan = new Scanner(file);
		    String line = scan.nextLine();
			 
			 do{
				 // Sort by Length
				 int i = line.length();
				 if (i>=library.size())
					 this.increaseLib(i);
				 
				 library.get(i).add(line);
				 
				 line = scan.nextLine();
			 } while (scan.hasNext());
		 
		}catch(FileNotFoundException excepObj)
		{
			System.out.println("Could not find this file");
		}
		 
	}

	private void increaseLib(int max)
	{
		int size = library.size();
		for (int i=size; i<max+1; i++)
			library.add(i, new ArrayList<String>());
			
	}
	
	//Returns the index-th word of all words of length word-length
	public String getWords(int wordLength, int index)
	{
		if (optRun) {
			return fOptLib.get(index);
		}
		else {
		return library.get(wordLength).get(index);
		}
	}

	//Returns the amount of wordLength words
	public int numberOfXLetterWords(int wordLength)
	{
		if (optRun) {
			return fOptLib.size();
		}
		else {
		return library.get(wordLength).size();
		}
	}
	
	//Albert butchers here
	//hopefully reorganizing the list for
	//optimization will avoid issues
	//return -1 if no optimize, positive value if optimized
	public int optimize(String start, String end)
	{
		if (optSafeSet > -1) 
		{
		return optSafeSet;
		//used to avoid re-running this when optimized library exists
		//...but flag has been manually set.
		//effectively pretends that method has run fully again
		}
		lengthIndex = start.length(); //what word length is needed?
		ArrayList<String> forOptimize = library.get(lengthIndex); //plug the answer in to get all responses
		
		maxMatch = -1;
		
		if (lengthIndex < 3) {
			return maxMatch;
			//***BEWARE! Running optimization for word pairs that are
			//***...less than 3 chars in length WILL result in errors
			//***...due to LOSSY nature of optimization.
			//***Turning off this IF switch is not recommended.
		}
		for (int i = 0; i < forOptimize.size(); i++)
		{
			//************
			//CUIDADO! WARNING!
			//**We can tweak this variable for performance: We may
			//**adjust down for longer search (more options enabled)
			//**or adjust it up if searches are long (but be aware of truncation!).
			//**
			//**Note: matches will be made at ONE GREATER THAN minMatch value.
			//**Value reflects minimum requirement of matches between initial & final word.
			//**RAISING variable:MINMATCH ABOVE 2 IS NOT ADVISED UNLESS WORDS WILL BE >3 CHARS!
			//************
			int minMatch = 2;
			if (lengthIndex > 5) {
				minMatch = 5; //automatically pruning unlikely candidates with 
				//SEE WARNING ABOVE REGARDING THIS VARIABLE!
			}
			if (lengthIndex > 10) {
				minMatch = 7; //automatically pruning
				//SEE WARNING ABOVE!
			}
			String toMatch = forOptimize.get(i);
			int curMatch = matchers(start, end, toMatch);
			if (curMatch > minMatch) {
				optLib.get(curMatch).add(toMatch);
				if (curMatch > maxMatch) {
					maxMatch = curMatch;
				}
			}
		}
		
		for (int a = 0; a < optLib.size(); a++) {
			ArrayList<String> chooChoo = optLib.get(a);
			for (int g = 0; g < chooChoo.size(); g++) {
				fOptLib.add(chooChoo.get(g));
			}
		}
		optRun = true; //used to alter returns if optimization has been run.
		optSafeSet = maxMatch; //used to avoid re-running this unnecessarily
		return maxMatch;
			
	}
	
	public void resetOptRun() //used to ignore an already-run optimization
	{
		optRun = false;
	}
	
	public int matchers(String start, String end, String compared)
	{
		//used for determining good candidates in optimization
		
		int number = 0;
		int lengthR = start.length();
		for (int i = 0; i < lengthR; i++)
		{
			if (start.charAt(i) == compared.charAt(i)) {
				number++;
			}
			if (end.charAt(i) == compared.charAt(i)) {
				number++;
			}
		}
		return number;
	}
			
 }



