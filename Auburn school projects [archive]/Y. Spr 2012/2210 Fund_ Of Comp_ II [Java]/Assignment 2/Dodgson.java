import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Dodgson
{
	String startLine, finishLine;
	int startLength, finishLength;
	//array of vowels
	ArrayList<char> vowelList = {'a', 'e', 'i', 'o', 'u'};
	
	//array of consonants
	ArrayList<char> consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
	'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'};
	
	//array of words already tried
	ArrayList<String> toNotRetry = new ArrayList<String>();
	
	//array of arrays to do multiple word selections
	ArrayList<ArrayList> allThePaths = new ArrayList<ArrayList>();
	ArrayList<String> finalFinal = new ArrayList<ArrayList>();
	
	//will check length of input and return the word, or 0 if improper length
	//if input int is -1, then is the starting word,
	public String wordLength(String input, int lengthGoal)
	{
		if (lengthGoal == -1 && input != null)
			if (!input.isEmpty())
			{
				startLine = input;
				startLength = input.length();
			}
		else if (input != null && !input.isEmpty())
		{
			int checkLength = input.length();
			if (lengthGoal == checkLength) {
				return input; 
			}
			else {
				return "0";
			}
		}

				
	}
	
	//method to check vowel or consonant, and return the array
	// (vowel or consonant) necessary to check
	public ArrayList letterTypeCheck(char toCheck)
	{
		if (vowelList.contains(toCheck)) {
			return vowelList;
		}
		else {
			return consonants;
		}
			
	}
	
	//method to change words
	//this will be confusing.
	//get a cupcake when you are done. please.
	//returns null if the start and end words are not of the same length
	public ArrayList switcheroo(String start, String finish)
	{
		//first check for equal lengths and set words
		wordLength(start, -1);
		
		if (finish.equals(wordLength(finish, startLength)){
			finishLength = finish.length();
			finishLine = finish;
		}
		else {
			return null;
		}
			
		//now we want to see how many letters are the same
		//if 0 or 1, we have some searching to do
		//if more than 1, we have a pattern to follow
			int matches = 0;
			for (int i = 0; i < startLength; i++)
			{
				if (startLine.charAt(i) == finishLine.charAt(i))
				{
					matches++;
				}
			}
			int changes = startLength - matches;
			if (matches == startLength || changes == 1)
			{
				finalFinal.add(startLine);
				finalFinal.add(finishLine);
				return finalFinal;
			}
			
			else if (changes == 2)
			{
				return switchETT()
			}
			else
			{
				return switchGTT()
			}
		
		
	}
			//done in the event that 2 chars need changing
	public ArrayList switchETT()
			{
			String tempWord1, tempWord2;
			int loc1 = -1, loc2 = -1;
			
			for (int i = 0; loc2 < 0; i++)
			{
				if (startLine.charAt(i) != finishLine.charAt(i))
				{
					if (loc1 == -1){
						loc1 = i; }
					if (loc1 != -1 && loc2 == -1){
						loc2 = i;}
					
				}
			}
			if (loc1 != 0){
				tempWord1 = "" + startLine.substring(0, loc1 -1)
				+ finishLine.charAt(loc1) + startLine.substring(loc1 +1);
			}
			if (loc1 == 0){
				tempWord1 = "" + finishLine.charAt(loc1) 
				+ startLine.substring(loc1 +1);
			if (loc2 != startLength -1) {
				tempWord2 = "" + tempWord1.substring(0, loc2 -1)
				+ finishLine.charAt(loc2) + tempWord1.substring(loc2 +1);
			}
			if (loc2 == startLength -1) {
				tempWord2 = "" + tempWord1.substring(0, loc2 -1) 
				+ finishLine.charAt(loc2);
			}
			
			//boolean w1 = //tempWord1 check for word as boolean value
			//boolean w2 = //tempWord2 check for word as boolean value
			if (!w1 || !w2) {
				return switchGTT
			}
			else {
				finalFinal.add(startLine);
				finalFinal.add(tempWord1);
				finalFinal.add(tempWord2);
				finalFinal.add(finishLine);
				return finalFinal;
			}
			
			
		}
		
			//done in the event that more than 2 chars need changing
		public ArrayList switchGTT()
			{	
				String pseudoFirst = startLine;
				String pseudoLast = finishLine;
				ArrayList<String> witchGPTH = new ArrayList<String>();
				
				while{//big loop here not yet finished
					
				
				//the ArrayList we may add to the Big Path ArrayList
				witchGPTH.clear();
				
				
				//we want to add the original first and last
				//then add any words that match
				//but we need to be able to shift what the pseudo first and last are
				
				
				int charPtnCts = 0; //use to see how many CHARS match for a pattern
				
				//the pattern, which will be changed during iterations
				String ptn = "";
					
				//in order for the pattern to work, it has to be all, less 1
				
				//forming a new pattern between pseudo-first and pseudo-last
				for (i = 0; i < finishLength; i++) {
					if (pseudoLast.charAt(i) == pseudoFirst.charAt(i))
					{
						ptn += pseudoLast.charAt(i);
						charPtnCts++; //remember to reset this at some point
					}
					else {
						ptn += "*";
					}
				}
				
				//*****begin trying to match IF there is a pattern of all less 1
				//else, no run
				if (charPtnCts == finishLength - 1) {				
				//compiling the new pattern
				Pattern tryPtn = Pattern.compile(ptn);
				//setting a boolean for if/when we have a match
				boolean matchYes = false;
				
				//begin looping to see if we get any matches
				for (int i = 0; i < currLibrary.numberOfXLetterWords(startLength); i++) {
					//duplicate the original two, replace the middle
					ArrayList<String> derp = new ArrayList<String>();
					
					//searching for a matching pattern
					Matcher tryMch = tryPtn.matcher(currLibrary.getWords(startLength, i));
					matchYes = tryMch.matches();
					if (matchYes) {
						derp.add(pseudoFirst);
						derp.add(pseudoLast);
						derp.add(currLibrary.getWords(startLength, i));
						}
					//delete pseudo first word
					//delete pseudo last word
					//add derp to the end
					
					
					}//end of for loop if the matching algorithm could actually work
				}//end of if charPtnCts is one off
				else
				{
					return shiftLetters();
				}
				
				}//big while loop
				//figure out what to return
			}//method
			
	public ArrayList shiftLetters(){
		String derpWord;
		boolean moveOn = Yes;
		
		//transpose first letter Z to A
		if (checkLetter(0) && moveOn){
		derpWord = finishLine.getCharAt(0) + startLine.substring(1, startLength-1)
		moveOn = !checkWerd(derpWord);
			}
		//transpose last letter Z to A
		if (checkLetter(startLength-1) && moveOn){
		derpWord = startLine.substring(0, startLength-2) + finishLine.getCharAt(startLength-1);
		moveOn = !checkWerd(derpWord);
		}
		//transpose the first letter A to Z
		if (checkLetter(0) && moveOn){
		derpWord = startLine.getCharAt(0) + finishLine.substring(1, startLength-1);
		moveOn = !checkWerd(derpWord);
		}
		//transpose the last letter A to Z
		if (checkLetter(startLength-1) && moveOn){
		derpWord = finishLine.substring(0, startLength-2) + startLine.getCharAt(startLength-1);
		}
		
		//transpose any of the middle letters
		int indices = startLength - 1;
		int cycleEx = 1;
		
		while (cycleEx < indices) {
			if (cycleEx == 1) {
				
				
			}
		}//end while indices less than start length
		
		
	}//shiftLetters
			
	public boolean checkWerd(String werd){
	}
			
			
	
}