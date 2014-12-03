import java.util.ArrayList;

public class Dodgson {
	
	Library lib;
	
	public Dodgson()
	{
		lib = new Library();
	}
	
	//Will find a word ladder between the start and end word
	public ArrayList<String> findSequence(String start, String end)
	{
		ArrayList<ArrayList<String>> frontSeq = new ArrayList<ArrayList<String>>();
		ArrayList<ArrayList<String>> endSeq = new ArrayList<ArrayList<String>>();
		ArrayList<String> finalSeq = null;
		ArrayList<ArrayList<String>> newFrontSeq;
		ArrayList<ArrayList<String>> newEndSeq;
		ArrayList<String> matches;
		Boolean foundEnd = false;
				
		frontSeq.add(new ArrayList<String>());
		frontSeq.get(0).add(start);
		endSeq.add(new ArrayList<String>());
		endSeq.get(0).add(end);
		
		do{
			
			newFrontSeq = new ArrayList<ArrayList<String>>();
			matches = this.oneLetterOff(frontSeq.get(0).get(frontSeq.get(0).size()-1));
							
			for (int i=0; i<matches.size(); i++)//front end arrays
			{
				ArrayList<String> sequence = frontSeq.get(0);
				String match = matches.get(i);
				ArrayList<String> extendedSeq = new ArrayList<String>();
				for (int k=0; k<sequence.size(); k++)
					extendedSeq.add(sequence.get(k));
				extendedSeq.add(match);
				newFrontSeq.add(extendedSeq);
			}
			
			newEndSeq = new ArrayList<ArrayList<String>>();
			matches = this.oneLetterOff(endSeq.get(0).get(endSeq.get(0).size()-1));
			for (int j=0; j<matches.size(); j++)//Back end arrays
			{
				ArrayList<String> sequence = endSeq.get(0);
				String match = matches.get(j);
				ArrayList<String> extendedSeq = new ArrayList<String>();
				for (int k=0; k<sequence.size(); k++)
					extendedSeq.add(sequence.get(k));
				extendedSeq.add(match);
				newEndSeq.add(extendedSeq);					
			}
								
			frontSeq.remove(0);
			frontSeq.addAll(newFrontSeq);
			endSeq.remove(0);
			endSeq.addAll(newEndSeq);
			
			finalSeq = this.findPath(frontSeq, endSeq);
			if (finalSeq != null)
				foundEnd = true;
			
		}while(!foundEnd);
		
		return finalSeq;
	}
	
	//given two array lists of array lists of strings, finds any shared strings and links the two lists the shared word belongs in 
	private ArrayList<String> findPath(ArrayList<ArrayList<String>> front, ArrayList<ArrayList<String>> end)
	{	
		ArrayList<String> finalSeq = null;
		//searches for any word to be present in front and end. location1 is it's location in front, location 2 in end
		int[] location1 = {-1, -1};
		int[] location2 = {-1, -1};
		boolean found = false;
		
		
		for (int i=0; i<front.size() && found==false; i++)
		{
			for (int j=0; j<front.get(i).size() && found == false; j++)
			{
				String first = front.get(i).get(j);
				for(int k=0; k<end.size() && found == false; k++)
				{
					if( end.get(k).indexOf(first.toUpperCase())>0 || end.get(k).indexOf(first.toLowerCase())>0 )
					{
						location1[0] = i;
						location1[1] = j;
						location2[0] = k;
						location2[1] = end.get(k).indexOf(first.toUpperCase());
						if (location2[1] == -1)
							location2[1] = end.get(k).indexOf(first.toLowerCase());
						
						found = true;
					}
				}
			}
		}
		 
		if (location1[0] != -1)
		{
			finalSeq = new ArrayList<String>();
			for (int i=0; i<location1[1]; i++)
			{
				finalSeq.add( front.get(location1[0]).get(i) );
			}
			for (int i=location2[1]; i>=0; i--) 
			{
				finalSeq.add(  end.get(location2[0]).get(i) );
			}
		}
		
		return finalSeq;
	}
	
	//Given a word, returns an array list of all other words that are one letter different
	private ArrayList<String> oneLetterOff(String word)
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
}
