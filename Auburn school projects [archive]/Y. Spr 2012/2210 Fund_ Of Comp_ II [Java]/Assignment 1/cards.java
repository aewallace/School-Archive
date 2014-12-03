/*
*
*@author: Albert Wallace
*
*@version: Feb. 4, 2012
*/

public class cards
{
	int cardValSuite;
	int cardValWSS;
	int fullValue = 0;
	String suiteTypeA;
	String cardName;
	String color;
	String DIAMONDS = "diamonds", SPADES = "spades", 
		HEARTS = "hearts", CLUBS = "clubs";
	
	public cards()
		{
		}
	
	public cards(int cardNumber, String suiteType, int toDeckValue)
		{
		creatorBE(cardNumber, suiteType);
		fullValue = cardNumber + toDeckValue;
		}
	
	public int creatorBE(int cardNumber, String suiteType)
		{
		if (suiteType == "joker")
			{
			fullValue = 53;
			cardValWSS = 53;
			cardName = "Joker";
			if (cardNumber == 1)
				{
				color = "black";
				cardValSuite = 53;
				}
			if (cardNumber == 2)
				{
				color = "red";
				cardValSuite = 53;
				}
			return 0;
			}

		String suiteIn = suiteType.toLowerCase();
		if (suiteIn == DIAMONDS || suiteIn == SPADES)
			{
			cardValWSS = cardNumber + 13;
			}
		else	{ cardValWSS = cardNumber; }
		cardValSuite = cardNumber;
		suiteTypeA = suiteIn.toLowerCase();
		cardName = cardNameFV(cardNumber);
		if (suiteIn == DIAMONDS || suiteIn == HEARTS)
			{ color = "red"; }
		else { color = "black"; }
		return 0;
				}
	
	public String getName()
		{
		return cardName;
		}
	
	public String getColor()
		{
		return color;
		}
	
	public int getDeckValue()
		{
		return fullValue;
		}
	
	public int getWSSValue()
		{
		return cardValWSS;
		}
	
	public String cardNameFV(int cardValue)
		{
		String output = "";

		switch (cardValue)
			{
			case 1:
				output = "Ace";
				break;
			case 2:
				output = "Two";
				break;
			case 3:
				output = "Three";
				break;
			case 4:
				output = "Four";
				break;
			case 5:
				output = "Five";
				break;
			case 6:
				output = "Six";
				break;
			case 7:
				output = "Seven";
				break;
			case 8:
				output = "Eight";
				break;
			case 9:
				output = "Nine";
				break;
			case 10:
				output = "Ten";
				break;
			case 11:
				output = "Jack";
				break;
			case 12:
				output = "Queen";
				break;
			case 13:
				output = "King";
				break;
			default:
				output = "Joker";
				break;
			}
		return output;
		}
}
