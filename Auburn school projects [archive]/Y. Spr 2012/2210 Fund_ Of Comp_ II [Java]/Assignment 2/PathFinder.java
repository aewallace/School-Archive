import java.util.ArrayList;
import java.util.Scanner;

public class PathFinder {
	
	Library lib = new Library(); //putting the library here
	//this allows the optimizations to be run once
	
	public PathFinder()
	{}
	
	
	//public ArrayList<String> path(String start, String end)
//old constructor allowing NO special libraries to be inserted
	public ArrayList<String> path(String start, String end, Library lib)
	{
		Library lib = new Library(); //putting the library here
		//...allows the optimizations to be run once per path search
		
		//****New: automatically runs optimization
		//****note: optimization runs, by default, on words >2 in length
		//****this may be changed in Library.java, NOT here
		//****if necessary, the use of the optimization may be disabled at ANY
		//****...point by adding [Library].resetOptRun.
		//****...however, optimization method MUST be run again
		//****...and it will determine if optimized list already exists
		lib.optimize(start, end);
		
		
		ArrayList<ArrayList<String>> master = new ArrayList<ArrayList<String>>();
		ArrayList<String> finalSeq = null;
		ArrayList<String> matches;
		Boolean foundEnd = false;
		Scanner scan = new Scanner(System.in);
		
		master.add(new ArrayList<String>());
		master.get(0).add(start);
		
		do{
			
			ArrayList<ArrayList<String>> newSeqs = new ArrayList<ArrayList<String>>();
			for(int i=0; i<master.size();i++) // will go through each list in 'master'
			{
				
				matches = this.oneLetterOff(master.get(i).get(master.get(i).size()-1), lib);
				
				
				for (int j=0; j<matches.size(); j++)
				{
					ArrayList<String> sequence = master.get(i);
					String match = matches.get(j);
					if (!sequence.contains(match))
					{
						ArrayList<String> extendedSeq = new ArrayList<String>();
						for (int k=0; k<sequence.size(); k++)
							extendedSeq.add(sequence.get(k));
						extendedSeq.add(match);
						newSeqs.add(extendedSeq);
						
						if (match.equalsIgnoreCase(end))
						{
							finalSeq = extendedSeq;
							foundEnd = true;
						}
				
					}
					
				}
								
			}
			
			master.clear();
			master.addAll(newSeqs);
			System.out.println(master);
			//scan.next();
		}while(!foundEnd);
		
		
		return finalSeq;
	}
	
	
	
	//Will return all words that are one letter off from 'word'
	public ArrayList<String> oneLetterOff(String word, Library lib) 
	{
		
		int wordLength = word.length();
		ArrayList<String> matches = new ArrayList<String>();
		
		
		for (int i=0; i< lib.numberOfXLetterWords(wordLength); i++)
		{
			
			String comparWord = lib.getWords(wordLength, i);
			for (int j=0; j<comparWord.length(); j++)
			{
				String oneLet = word.substring(0,j) + word.substring(j+1, word.length());
				String oneLetComp = comparWord.substring(0,j) + comparWord.substring(j+1, comparWord.length());
				if (oneLet.equalsIgnoreCase(oneLetComp))
				{
					matches.add(comparWord);
					j= comparWord.length();
				}
			}
		}
		return matches;
	}
	
	//Albert has likely butchered good code

}
