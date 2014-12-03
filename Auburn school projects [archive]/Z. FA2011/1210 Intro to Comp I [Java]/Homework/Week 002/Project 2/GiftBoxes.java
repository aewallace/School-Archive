import java.util.Scanner;
/**
*This program will determine whether a gift box can successfully
* house a given gift. If so, it will output the amount of
* materials needed to make a proper presentation of the gift.
*Project 002
*
*@author Albert Wallace, Section 003
*@version 9/02/2011
*/
public class GiftBoxes {
	/**
	*This method will ask the user for a number of parameters
	* related to the size of the gift & the potential gift box.
	* It will then do the calculations necessary to help the
	* user properly pack and box the gift, if possible.
	*
	*@param args User-defined command line arguments (Not used).
	*/
	public static void main(String[] args) {
	
		Scanner userInput = new Scanner(System.in);
		
		//initializing variables to be used in calculations
		double materialSABox, lengthBox, widthBox, heightBox, volumeBox;
		double peanutsReqd;
		double volumeGift;
		
		//getting the necessary measurements from the user
		System.out.print("Please type the length of the box in inches: ");
		lengthBox = userInput.nextDouble();
		System.out.print("Please type the width of the box in inches: ");
		widthBox = userInput.nextDouble();
		System.out.print("Please enter the height of the box in inches: ");
		heightBox = userInput.nextDouble();
		System.out.print("Please enter the volume of the gift"
			+ " in cubic inches: ");
		volumeGift = userInput.nextDouble();
		
		//calculating the volume of the box and comparing to volume of gift
		volumeBox = lengthBox * widthBox * heightBox;
		
		
		//screen output, depending on volume of box vs volume of gift
		if (volumeBox < volumeGift) {
			System.out.println("\nThe gift is too large for the box.");
			}
		else {
			peanutsReqd = (volumeBox - volumeGift);
			materialSABox = (lengthBox * widthBox + heightBox * widthBox 
				+ lengthBox * heightBox) * 2;
				
			System.out.println("\nThe amount of material needed for the box is "
				+ materialSABox + " square inches.");
			System.out.println("The volume of the box is " + volumeBox
				+ " cubic inches.");
			System.out.println("The box will need " + peanutsReqd
				+ " cubic inches of \"peanuts\" for shipping.");
			}
		
		
		}
		
}