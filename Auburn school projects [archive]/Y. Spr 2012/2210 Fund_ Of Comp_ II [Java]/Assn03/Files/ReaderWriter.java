//use for general reading and writing of files
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.BufferedWriter;


public class ReaderWriter
{
	//***************************************
	//this is where our IO contents are stored.
	//do not butcher this.///////////////////
	//***************************************
	private String writeOut = "";////////////
	private String inputFileSrg = "";////////
	//***************************************
	
	boolean successFileInSet = false;
	private int inputLengthQA = 0;
	
	
	private File file;
	//private File file = new File("sowpods.txt");
	private TempFileAccess tFS;
	//private TempFileAccess tFS = new TempFileAccess(file);
	private LineIterator itr;
	//private LineIterator itr = (LineIterator) tFS.iterator();
	
	public ReaderWriter()
	{}

	
	//will open the input file for use.
	public boolean openFile(String fileName)
	{
		file = new File(fileName);
		tFS = new TempFileAccess(file);
		itr = (LineIterator) tFS.iterator();
		
		String line = (String) itr.next();
		
		 do{
			 inputFileSrg += line;
			 
			 line = itr.next();
		 }
		 while (itr.hasNext());
		 successFileInSet = true;
		 inputLengthQA = inputFileSrg.length();
	 	 return successFileInSet;
	}
	
	//adds characters to be written to the output string
	public boolean addToWrite(String addition)
	{
		writeOut += addition;
		return successFileInSet;
	}
	
	//allows recheck of successful input file opening
	public boolean canRead()
	{
		return successFileInSet;
	}
	
	//returns character count of the input file
	public int charCount()
	{
		return inputLengthQA;
	}
	
	//retrieve input file contents
	public String retrieveInput()
	{
		return inputFileSrg;
	}
	
	//used to write the file after string is filled
	public boolean writeFile(String fileName)
	{
		boolean canBeWritten = false;
		//if you can write the file
		//change 'canBeWritten' to true
		//and write it
		try{
  			// Create file 
  			FileWriter fstream = new FileWriter(fileName);
  			BufferedWriter out = new BufferedWriter(fstream);
  			out.write(writeOut); //writes the stored string
  			//Close the output stream
  			out.close();
			canBeWritten = true;
		}
		catch (Exception e){//Catch exception if any
			System.err.println("Error: " + e.getMessage());
		}

		return canBeWritten;
	}
	
}