   import java.util.Scanner;
   import java.util.ArrayList;
   import java.io.File;
   import java.io.IOException;
   import java.text.NumberFormat;

/**
*This is used to help organize, say, a grocery store.
* It accepts categories for different items, and helps with calculation
* of total price for each given item. This is the potential front end.
*
*@author Albert Wallace -- section 003
*@version 9/28/2011
*/

   public class GroceryList {
   
   
   /**
   *This is the main method that will be automatically executed
   * to do all of the front end work for the grocery program.
   *
   *@param args Not used.
   *
   *@throws IOException used to avoid huge crashes
   */
      public static void main(String[] args)  throws IOException      
      {
      //...Names for categories of grocery goods.
      /**
      *General products that have no specific category.
      */
         String generalS = "General";
      /**
      *Represents the produce category of products.
      */
         String produceS = "Produce";
      /**
      *Represents refrigerated goods.
      */
         String refrigeratedS = "Refrigerated";
      /**
      *Represents items that need to remain fully frozen.
      */
         String frozenS = "Frozen";
         
         NumberFormat currencyFmt = NumberFormat.getCurrencyInstance();
      
         Scanner scan = new Scanner(System.in); //for general input
         String  fileName; //for file name input
         System.out.println("Please type the name of the input file: ");
         fileName = scan.nextLine(); //to receive the actual file name
      
         System.out.println("\n\rPlease wait...\n\r");
      
         String line;
         ArrayList<String> inputList = new ArrayList<String>();         
         Scanner inFile = new Scanner(new File(fileName)); //connects to file
      
      //to get the info from the file
         while (inFile.hasNext())
         {   
            line = inFile.nextLine();
         // System.out.println(line);  
         
         // Break line into words
            Scanner lineScan = new Scanner(line);
            while (lineScan.hasNext()) {
               inputList.add(lineScan.next());
            }     
         }
         inFile.close();
      //parsing the info now in RAM
      
      //we have inputList as our array. Things are at various indices.
      //But things are arranged in a pattern, so we can easily do this.
      //First we need an array for the food objects
         ArrayList<GroceryItem> groceries = new ArrayList<GroceryItem>();
         GroceryItem singleItem, singleItemTemp;
      
      //Now to fill the new groceries array, we throw in some objects.
      //the first index of our original list holds the local tax rate...
         double taxRate = Double.parseDouble(inputList.get(0));
      
      //...and from there, it's name + cost + base price of items
      //then we can create more items in the grocery array
         int iteration = 0, toName = 1, toCategory = 2, toBasePrice = 3;
         String name, category;
         double basePrice;
         while (iteration + 1 < inputList.size())
         {
            name = inputList.get(iteration + toName);
            category = inputList.get(iteration + toCategory);
            basePrice = 
               Double.parseDouble(inputList.get(iteration + toBasePrice));
         
            singleItem = new GroceryItem(name, category);
            singleItem.setBasePrice(basePrice);
            singleItem.calculateTotalPrice(taxRate);
         
            groceries.add(singleItem);
         
         
            iteration = iteration + 3;
         }
      
      //after creating that array, we need to calculate total and
      // print info to screen
         double groceryListCost = 0;
         int iterationOutput = 0;
         String listOutput = "Grocery List\n------------\n";
         String generalOutput = "General:";
         String produceOutput = "\n\nProduce:";
         String refrigeratedOutput = "\n\nRefrigerated:";
         String frozenOutput = "\n\nFrozen:";
      
         while (iterationOutput < groceries.size())
         {
            singleItemTemp = groceries.get(iterationOutput);
         
            groceryListCost = groceryListCost 
               + singleItemTemp.getTotalPrice();
         
         
            if ((singleItemTemp.getCategory()).equals(generalS))
            {
               generalOutput += "\n- " 
                  + singleItemTemp.getName();
            }
            else if ((singleItemTemp.getCategory()).equals(produceS))
            {
               produceOutput += "\n- "
                  + singleItemTemp.getName();
            }
            else if ((singleItemTemp.getCategory()).equals(refrigeratedS))
            {
               refrigeratedOutput += "\n- " 
                  + singleItemTemp.getName();
            }
            else if ((singleItemTemp.getCategory()).equals(frozenS))
            {
               frozenOutput += "\n- " 
                  + singleItemTemp.getName();
            }
            iterationOutput = iterationOutput + 1;
         }
         listOutput += generalOutput + produceOutput 
            + refrigeratedOutput + frozenOutput;
         listOutput += "\n\nTotal cost of items: " 
            + currencyFmt.format(groceryListCost);
         
         
         System.out.print(listOutput);
      	
      }
   
   }