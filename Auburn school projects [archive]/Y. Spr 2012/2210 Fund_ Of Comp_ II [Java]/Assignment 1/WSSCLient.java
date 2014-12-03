/*
*
*@author: Albert Wallace
*
*@version: Feb. 4, 2012
*/

public class WSSCLient 
{
	//public static String[] plaintextArray = {"ATTACKATDAWN"};
	
	public static String[] plaintextArray = {"JOKER", "ATTACKATDAWN", 
		"HELPME", "WAREAGLE"};
	
	
	public static void main(String[] args)
		{
		WSS wss = new WSS();
		int i = 0;
		 
			
			String plaintext = plaintextArray[i]; 
			String ciphertext = wss.encrypt(plaintext);
 			System.out.println("Plaintext: " + plaintext); 
 			System.out.println("Ciphertext: " + ciphertext); 
 			System.out.println();
			
			
		i++;
			plaintext = plaintextArray[i]; 
			ciphertext = wss.encrypt(plaintext);
 			System.out.println("Plaintext: " + plaintext); 
 			System.out.println("Ciphertext: " + ciphertext); 
 			System.out.println();
			
		i++;
			plaintext = plaintextArray[i]; 
			ciphertext = wss.encrypt(plaintext);
 			System.out.println("Plaintext: " + plaintext); 
 			System.out.println("Ciphertext: " + ciphertext); 
 			System.out.println();
		
		i++;
			plaintext = plaintextArray[i]; 
			ciphertext = wss.encrypt(plaintext);
 			System.out.println("Plaintext: " + plaintext); 
 			System.out.println("Ciphertext: " + ciphertext); 
 			System.out.println();		
			
		}
		
	}