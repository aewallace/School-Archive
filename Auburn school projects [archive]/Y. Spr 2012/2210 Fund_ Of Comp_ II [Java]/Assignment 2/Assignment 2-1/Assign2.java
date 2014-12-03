import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Assign2 {

	public static void main(String[] args)
	{
		Dodgson dodgson = new Dodgson();
		File file = new File("diller.txt");
		Scanner scan;
		String startWord, endWord;
		ArrayList<String> wordLadder;
		try {
			scan = new Scanner(file);
			
			while (scan.hasNext())
			{
				
				startWord = scan.nextLine();
				endWord = scan.nextLine();
				wordLadder = dodgson.findSequence(startWord, endWord);
				
				for (int i=0; i<wordLadder.size()-1; i++)
				{
					String word = wordLadder.get(i).toLowerCase();
					System.out.print(word + ", ");
				}
				System.out.println(wordLadder.get(wordLadder.size()-1).toLowerCase());
				
			}
			
			
			
			
			
			
			
		}catch(FileNotFoundException excepObj)
		{
			System.out.println("Could not find this file");
		}
		
		
	}
}
