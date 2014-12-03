import java.util.ArrayList;
import java.io.File;

public class Library {
	
	private ArrayList<ArrayList<String>> library = new ArrayList<ArrayList<String>>();
	private File file = new File("sowpods.txt");
	private Lexicon lex = new Lexicon(file);
	private LineIterator itr = (LineIterator) lex.iterator();
	
	public Library()
	{	 
		String line = (String) itr.next();
		
		 do{
			 // Sort by Length
			 int i = line.length();
			 if (i>=library.size())
				 this.increaseLib(i);
			 
			 library.get(i).add(line);
			 
			 line = itr.next();
		 } while (itr.hasNext());
	 	 
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
		return library.get(wordLength).get(index);
	}

	//Returns the amount of wordLength words
	public int numberOfXLetterWords(int wordLength)
	{
		return library.get(wordLength).size();
	}
	
	 }



