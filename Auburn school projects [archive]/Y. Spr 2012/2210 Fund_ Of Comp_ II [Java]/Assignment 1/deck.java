/*
*
*@author: Albert Wallace
*
*@version: Feb. 4, 2012
*/

import java.util.ArrayList;

public class deck extends cards
{
	static ArrayList<cards> cardArray = new ArrayList();
	int ksValue;
	
	public deck()
		{
		init();
		}
	
	public void init()
	{
	cardArray.clear();
	
	int deckCCycle = 1;
	int suiteCCycle = 1;
	int suiteTypeCycle = 1;
	int totalCards = 52;
	int maxPerSuite = 13;
	int added = 0;
	String sType;
	while (deckCCycle <= totalCards)
		{
		if (suiteCCycle > maxPerSuite)
			{ 
			suiteCCycle = 1;
			suiteTypeCycle++;
			}
		
		if (suiteTypeCycle == 1)
			{
			sType = "clubs";
			added = 0;
			}
		else if (suiteTypeCycle == 2)
			{
			sType = "diamonds"; 
			added = 13;
			}
		else if (suiteTypeCycle == 3)
			{ 
			sType = "hearts";
			added = 26; 
			}
		else //if (suiteTypeCycle == 4)
			{
			sType = "spades";
			added = 39;
			}
		
		cardArray.add(new cards(suiteCCycle, sType, added)); //probably unsafe; begin fixing here
		deckCCycle++;
		suiteCCycle++;
		}
	cardArray.add(new cards(1, "joker", 0));
	cardArray.add(new cards(2, "joker", 0));
	}
	
	public int jokerSearch(String srcInput, int findFirst)
		{
		int found = -1;
		int index = -1;
		for (int i = 0; findFirst != found; i++)
			{
			if (cardArray.get(i).getName() == srcInput)
				{
					index = i;
					found++;
				}
			}
		return index;
		}
		
	public int jokerSearchC(String srcInput, String color)
		{
		int found = -1;
		int index = -1;
		for (int i = 0; found < 0; i++)
			{
			if (cardArray.get(i).getName() == srcInput
			&& cardArray.get(i).getColor() == color)
				{
					index = i;
					found++;
				}
			}
		return index;
		}
	
	public void countCut()
		{
		ArrayList<cards> temp0 = new ArrayList();
		ArrayList<cards> temp1 = new ArrayList();
		ArrayList<cards> temp2 = new ArrayList();
		
		cards tempC = cardArray.get(cardArray.size() - 1);
		
		int index0 = tempC.getDeckValue();
		//index0 = index0 + 1;
		int index1 = cardArray.size() - 1;
		
		for (int i = 0; i < index0; i++)
			{
			temp0.add(cardArray.get(i));
			}
		for (int i = index0; i <= index1 - 1; i++)
			{
			temp1.add(cardArray.get(i));
			}
			
			
		cardArray.clear();
		
		for (int i = 0; i < temp1.size(); i++)
			{	cardArray.add(temp1.get(i));	}
		for (int i = 0; i < temp0.size(); i++)
			{	cardArray.add(temp0.get(i));	}
		cardArray.add(tempC);
		

		
		}
		
	public void tripleCut()
		{
		ArrayList<cards> temp0 = new ArrayList();
		ArrayList<cards> temp1 = new ArrayList();
		ArrayList<cards> temp2 = new ArrayList();
		
		int index0 = jokerSearch("Joker", 0);
		int index1 = jokerSearch("Joker", 1);
		
		for (int i = 0; i < index0; i++)
			{
			temp0.add(cardArray.get(i));
			}
		for (int i = index0; i <= index1; i++)
			{
			temp1.add(cardArray.get(i));
			}
		for (int i = index1 + 1; i < cardArray.size(); i++)
			{
			temp2.add(cardArray.get(i));
			} 
			
		cardArray.clear();
		
		for (int i = 0; i < temp2.size(); i++)
			{	cardArray.add(temp2.get(i));	}
		for (int i = 0; i < temp1.size(); i++)
			{	cardArray.add(temp1.get(i));	}
		for (int i = 0; i < temp0.size(); i++)
			{	cardArray.add(temp0.get(i));	}
		}
		
	public int keystreamValue()
		{
		int countTo = cardArray.get(0).getDeckValue();
		ksValue = cardArray.get(countTo).getWSSValue();
		
		if (ksValue <= 26)
			{ ksValue = ksValue; }
		else
			{ ksValue = -1; }
			
		return ksValue;
		}
	
	public void jokerAD1()
		{
		int indexer = jokerSearchC("Joker", "black");
		if (indexer < cardArray.size() - 1)
			{
			cards temp0 = cardArray.get(indexer);
			cards temp1 = cardArray.get(indexer + 1);
			cardArray.remove(indexer);
			cardArray.add(indexer, temp1);
			cardArray.remove(indexer + 1);
			cardArray.add(indexer + 1, temp0);
			}
		else if (indexer == cardArray.size() - 1)
			{
			cards temp0 = cardArray.get(0);
			cards temp1 = cardArray.get(indexer);
			ArrayList<cards> temp2 = new ArrayList();
			
			for (int i = 1; i < indexer; i++)
				{
				temp2.add(cardArray.get(i));
				}
				
			cardArray.clear();
			
			cardArray.add(indexer, temp1);
			cardArray.add(indexer + 1, temp0);
			
			for (int i = 0; i < temp2.size(); i++)
				{
				cardArray.add(temp2.get(i));
				}
			}
		}
		
	public void jokerBD2()
		{
		int indexer = jokerSearchC("Joker", "red");
		if (indexer < cardArray.size() - 2)
			{
			cards temp0 = cardArray.get(indexer);
			cards temp1 = cardArray.get(indexer + 1);
			cards temp2 = cardArray.get(indexer + 2);
			cardArray.remove(indexer);
			cardArray.add(indexer, temp1);
			cardArray.remove(indexer + 1);
			cardArray.add(indexer + 1, temp2);
			cardArray.remove(indexer + 2);
			cardArray.add(indexer + 2, temp0);
			}
		else if (indexer == cardArray.size() - 2)
			{
			//just below top
			int moveLastTo = cardArray.size();
			cards temp0 = cardArray.get(0);
			cards temp1 = cardArray.get(indexer);
			cards temp3 = cardArray.get(cardArray.size() - 1);
			ArrayList<cards> temp2 = new ArrayList();
			
			for (int i = 1; i < indexer; i++)
				{
				temp2.add(cardArray.get(i));
				}
			cardArray.clear();
			
			cardArray.add(0, temp0);
			cardArray.add(1, temp1);
			
			for (int i = 0; i < temp2.size(); i++)
				{
				cardArray.add(temp2.get(i));
				}
				
			cardArray.add(temp3);
			}
		else if (indexer == cardArray.size() - 1)
			{
			//just below second
			cards temp0 = cardArray.get(0);
			cards temp3 = cardArray.get(1);
			cards temp1 = cardArray.get(indexer);
			ArrayList<cards> temp2 = new ArrayList();
			
			for (int i = 2; i < indexer; i++)
				{
				temp2.add(cardArray.get(i));
				}
				
			cardArray.clear();
			
			cardArray.add(0, temp0);
			cardArray.add(1, temp3);
			cardArray.add(2, temp1);
			
			for (int i = 0; i < temp2.size(); i++)
				{
				cardArray.add(temp2.get(i));
				}
			}
		}
}