/*
*Contains recycled code written by Professor Dean Hendrix
* and undergrad student Lizzy Shackleford
* from Lab Assignment Number 2.
*/

import java.io.*;
import java.util.Iterator;

public class TempFileAccess implements Iterable
{

	Iterator itr;
	private BufferedReader fileInput;
	File theFile;
	

	public TempFileAccess()
	{
	}
	
	public TempFileAccess(File file)
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
	
	
	
	public Iterator iterator()	
	{
		// itr.next reads a bloody line
		Iterator itr = new LineIterator(theFile);
		return itr;
	}

	
	
}
