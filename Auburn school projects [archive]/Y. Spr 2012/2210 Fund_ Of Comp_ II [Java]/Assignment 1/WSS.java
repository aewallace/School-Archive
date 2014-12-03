/*
*
*@author: Albert Wallace
*
*@version: Feb. 4, 2012
*/

import java.util.ArrayList;

public class WSS extends deck
{
	static deck gDeck = new deck();
	
	public WSS()
		{
		//gDeck.init();
		}
	
	public void initDeck()
		{
		gDeck.init();
		}
		
	public String encrypt(String plaintext)
		{
		while (plaintext.length()%5 > 0)
			{
			plaintext += "X";
			}
		String output = "";
		int jokerBreak = 0;
		int keyValue = 0;
		int[] inLetters = new int[54];
		for (int i = 0; i < plaintext.length(); i++)
			{
			int letnum = (int) plaintext.charAt(i);
			inLetters[i] = letnum;
			}
		for (int i = 0; i < plaintext.length(); i++)
		{
			
			//jokerBreak = 0;
			//do
			
				gDeck.jokerAD1();
				gDeck.jokerBD2();
				gDeck.tripleCut();
				gDeck.countCut();
				jokerBreak = gDeck.keystreamValue();
			if (jokerBreak != -1)
				{	
				keyValue = jokerBreak;
				}
			while (jokerBreak == -1)
				{
				gDeck.jokerAD1();
				gDeck.jokerBD2();
				gDeck.tripleCut();
				gDeck.countCut();
				jokerBreak = gDeck.keystreamValue();
				}
			if (jokerBreak != -1)
				{
				keyValue = jokerBreak;
				}
			int num = (int)inLetters[i];
			int numnum = num + keyValue;
			if (numnum >= 26 + 65)
				{
				numnum = numnum - 26;
				}
			char numlet = (char) numnum;
			output += numlet;
		}
			
			
		return output;
		}
		
}