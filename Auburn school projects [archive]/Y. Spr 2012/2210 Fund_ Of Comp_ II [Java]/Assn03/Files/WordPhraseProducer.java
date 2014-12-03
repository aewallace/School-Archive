import java.util.Random;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class WordPhraseProducer
{
	Random decision = new Random();
	ReaderWriter fileTweaker = new ReaderWriter();
	//String getNewSeed = "Get New Seed; used for prompting cycle refresh later.";
	boolean remoteWriteThis = true;
	//empty constructor
	public WordPhraseProducer()
		{}
	
	//will write directly to the potential output, BUT requires a call of
	// a flusher method (also in the class) to do the final write.
	// use of driver method is required to avoid issues
	// as well as to determine to/from where the code will read & write files.
	public boolean processingMiddleMan(int seedLength, int endLength)
	{
		//retrieve the file from fileTweaker
		//see how many characters there are
		//begin loop
		//randomly choose a seed from within (the index (minus (k seed length + 1)))
		//find however many single characters fit the seed
		//choose at random, though with multiple entries
		//write that character, then tweak the seed!
		//move forward by finding things that fit the new seed
		//if no fit (End of File), randomize new seed & continue
		String source = fileTweaker.retrieveInput();
		int srcLength = fileTweaker.charCount();
		
		seedLength++;
		
		boolean postProcessed = false;
		int cycles = 0;
		int seedIndex = chooseOpt(srcLength - (seedLength + 1));
		String seed = "";
		//hard code first seed using beginning of file
		seed = source.substring(0, seedLength);
		//seed = seedChoice(seedIndex, source, seedLength);
		String kimchi = charAfterSeed(source, seed); 
		addToWrite(kimchi);
		cycles++;
		String charAST = "";
		
		while (cycles < endLength)
			{
			//if needed, make new seed
			//if no new seed needed, remove the first letter of the seed, add
			if (!remoteWriteThis)
				{
				seedIndex = chooseOpt(srcLength - (seedLength));
				seed = seedChoice(seedIndex, source, seedLength);
				remoteWriteThis = true;
				}
			else
				{
				System.out.println("Orig" + (seed.length()) + "");
				String seedE = seed.substring(1, seed.length());
				System.out.println("seedE" + seedE.length());
				seed = seedE + kimchi;
				System.out.println("mod" + seed.length());
				}
			//stopped where I retrieve the singular character to be added
			//the randomization of char choice will have been done
			charAST = charAfterSeed(source, seed);
			if (remoteWriteThis)
				{
				addToWrite(charAST);
				kimchi = charAST;
				cycles++;
				}
			}
		if (cycles == endLength)
			{ postProcessed = true; }
		
		return postProcessed;
	}
	
	//counts the number of characters in the input file	
	public int charCount()
		{
		return fileTweaker.charCount();
		}
		
	//checks to see if the input file
	//has at least minCheck (k) characters
	public boolean charCheck(int minCheck)
		{
		if (charCount() < minCheck)
			{ return false; }
		else
			{ return true; }
		}

	//decides which character/index will be chosen from a range of "m" choices
	//returns decision as an int to go directly to an index
	public int chooseOpt(int mChoices)
	{
		return decision.nextInt(mChoices);
	}
	
	//determines which character will match our given seed
	public String charAfterSeed(String source, String match)
	{
		String matchLiteral = match;
		
		System.out.println("matchCharAfterSeed" + match.length());
		System.out.println("matchLiteral_charAfter" + matchLiteral.length());
		
		match = match.replaceAll("\\W", ".");
		Pattern p = Pattern.compile(match);
 		Matcher m = p.matcher(source);
		boolean runContd = m.find();
		int indR = 0;
		int indH = 0;
		int avoidWall = (source.length() - match.length()) - 1;
		
		ArrayList<String> potential = new ArrayList<String>(); //potential char addition
		while (runContd && indR + 1 < avoidWall) //runs if there is a match
			{
			indH = m.start();
			indR = m.end(); //the index of the next match
			String tmo = source.substring(indH, indR);
			if (tmo.equals(match)){ //new match only added if a real match
				char tmp = source.charAt(indR);
				String tmq = Character.toString(tmp);
				potential.add(tmq);
				}	//add to potential
			runContd = m.find(); //stores if another match can be found
								//should push, when a new run is done, a new index
			}
		//in case there were no matches (like reaching the end of the source)
		//we return a special string of failure to invoke a new seed randomization
		if (potential.size() < 1 || potential.isEmpty())
			{
			remoteWriteThis = false;
			return "";
			}
		int letterIndex = decision.nextInt(potential.size());
		return potential.get(letterIndex);
	}
	
	//determines what our seed will be
	public String seedChoice(int selectIndex, String source, int seedLength)
	{
		String seedly = "";
		seedly = source.substring((selectIndex), (selectIndex - 1 + seedLength));
		return seedly;
	}
	
	//provides access to file check
	public boolean canRead()
	{
		return fileTweaker.canRead();
	}
	
	public boolean openFile(String fileName)
	{
		return fileTweaker.openFile(fileName);
	}
	
	public boolean addToWrite(String input)
	{
		return fileTweaker.addToWrite(input);
	}
	
	public boolean writeFile(String fileName)
	{
		return fileTweaker.writeFile(fileName);
	}
		
}