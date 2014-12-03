import java.io.*;
import java.util.Iterator;


public class Lexicon implements ILexicon {
 
	Iterator itr;
	private BufferedReader fileInput;
	File theFile;
	

	public Lexicon()
	{
	}
	
	public Lexicon(File file)
	{
		theFile = file;
		this.open(file);
		
	}
	
	public void open(File file)
	{
		try 
     	{
        fileInput = new BufferedReader(new FileReader(file));
        itr = this.iterator();
     	}
		catch (FileNotFoundException excepObj) 
			{
			System.out.println("Error: Couldn't find the file.");
			return;
        }
		  
	}
	
	public void close()
	{
		try
		{
			fileInput.close();
		}
		catch (Exception ex) {}
	}
	
	public boolean isWord(String str)
	{
		File reopenFile = theFile;
		this.close();
		this.open(reopenFile);
		Boolean isWord = false;
		
		while (itr.hasNext() && !isWord)
		{
			if (itr.next().equals(str))
				isWord= true;
		}
		
		return isWord;
		
	}
	
	public boolean isPrefix(String str)
	{
		File reopenFile = theFile;
		this.close();
		this.open(reopenFile);
		Boolean isPrefix = false;
		int length = str.length();
		
		while (itr.hasNext() && !isPrefix)
		{
			String next = (String) itr.next();
			if (next.length() >= str.length())
			{
				String prf = next.substring(0,length);
				if (prf.equals(str))
					isPrefix= true;
			}
		}
		return isPrefix;					
	}
	
	public Iterator iterator()	
	{
		// itr.next reads a bloody line
		Iterator itr = new LineIterator(theFile);
		return itr;
	}

	
	
}
