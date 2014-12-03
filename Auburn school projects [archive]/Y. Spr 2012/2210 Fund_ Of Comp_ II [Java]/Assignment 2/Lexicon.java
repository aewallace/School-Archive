import java.util.Scanner;
import java.util.Iterator;
import java.io.*;


public class Lexicon implements ILexicon
 {
   private BufferedReader fileInput;
   /**
    * Associates the lexicon with the words contained
    * in fileName.
    *
    * @param filename	the file containing strings
    * 						to be included in the lexicon
    */
      public void open(File filename)
		{
			try 
         	{
            fileInput = new BufferedReader(new FileReader(filename));
         	}
			catch (FileNotFoundException excepObj) 
				{
				System.out.println("Error: Couldn't find the file.");
				return;
            }
			  
		}
   
   /**
    * Closes the currently open lexicon. 
    *
    */
      public void close()
		{
			try
			{
				fileInput.close();
			}
			catch (Exception ex) {}
		}
   
   /**
    * Determines if str is a word.
    *
    * @param str	the string to be validated as a word
    * @return		true is str is in the lexicon, false
    *					otherwise
    */   
      public boolean isWord(String str)
		{
		return true;
		}
      
   /**
    * Determines if str begins any word.
    *
    * @param str	the string to be validated as a word
    *					prefix
    * @return		true is str begins any word in the
    *					lexicon, false otherwise
    */   
      public boolean isPrefix(String str)
		{
		return true;
		}
      
   /**
    * Instantiates and returns an iterator on this
    * lexicon.
    *
    * @return 	an iterator object for this lexicon
    */	
      public Iterator iterator()
		{
	
		}
   
   }