/*
 *Contains code from Project 2
 */

import java.util.Iterator;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.File;


public class LineIterator implements Iterator<String> {
	
	private String line = null;
	private BufferedReader bReader;
	
	public LineIterator(File file)
	{
		Reader read;
		try {
			read = new FileReader(file);
			bReader = new BufferedReader(read);
		}catch(FileNotFoundException excepObj)
		{
			System.out.println("Could not find this file");
		}
	}
	

    public boolean hasNext() 
    {
    	boolean next=false;
    	line = null;
   
	   try {
	    	bReader.mark(100);
	    	line = bReader.readLine();
	    	bReader.reset();
		} catch (IOException e1) {
			System.out.println("IO Exception, " + e1);
		}
	    
	    if (line != null)
	    	next = true;
	    return next;
	}

    //reads a LINE
    public String next() 
    {
    	try {
			line = bReader.readLine();
		} catch (IOException e) {
			System.out.println("IO Exception, no Next iteration");
		}
    	return line;
    }

    public void remove()
    {
    //
    }
        
}
