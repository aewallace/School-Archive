   import org.junit.Assert;
   import org.junit.Test;

   /** Tests the functionality of the ApparelItem class. 
	 * 
	 * As you implement your methods, uncomment the test contents
	 * below by selecting the code, right clicking, and selecting
	 * Edit -> uncomment. For example, when you have completed your
	 * constructor and getName, uncomment the first 3 tests.
	 *
	 * You will have to fill in many of the methods below to set
	 * up the object and complete the assert statments. More than 
	 * one assert statement is allowed per method, but you should try
	 * to not have more than 2-3.
	 *
	 * These tests do not represent all of the tests on Web-CAT; you
	 * should add your own methods to this file to test additional
	 * functionality.
	 *
	 * @author Lauren Goff
	 * @author Albert Wallace
	 **/
	
   public class ApparelItemTest {
   
       /*-------------------- getName tests --------------------*/
     
       /** Test getName after constructor is invoked. **/
      @Test public void nameTest() {      
		
      /* set up item Coat with item # 45352 at $10.2 */
         ApparelItem item = new ApparelItem("Coat,45352,10.2");
      /* verify that name matches expected output */
         Assert.assertEquals("Coat", item.getName());
      }
       
       /** Test getName with leading / trailing spaces in item code. **/
      @Test public void nameWithSpaceTest() {
         ApparelItem item = new ApparelItem(" Wool Scarf  ,8564,10.2");
         Assert.assertEquals("Wool Scarf", item.getName());
      }
   	
       /** Test getName after resetting the code. **/
      @Test public void nameAfterSetTest() {
         ApparelItem item = new ApparelItem("Coat,45352,10.2");
         item.setItemCode("Gloves,326,10.2");
         Assert.assertEquals("Gloves", item.getName());
      }
   
   
   
        /*-------------------- getId tests --------------------*/
   	  
       /** Test getId after constructor is invoked. **/
      @Test public void idTest() {
      //   
      /* set up item Coat with item # 45352 at $10.2 */
         ApparelItem item = new ApparelItem("Coat,45352,10.2");
      /* verify that id matches expected output */
         Assert.assertEquals(45352, item.getId());
      }
      
       /** Test getId with leading / trailing spaces in item code. **/
      @Test public void idWithSpaceTest() {
         ApparelItem item = new ApparelItem("Wool Scarf,  8564  ,10.2");
         Assert.assertEquals(8564, item.getId());
      }
    	
       /** Test getId after resetting the code. **/
      @Test public void idAfterSetTest() {
         ApparelItem item = new ApparelItem("Coat,45352,10.2");
         item.setItemCode("Gloves,326,10.2");
         Assert.assertEquals(326, item.getId());
      }
   
   
   
   
   
   
      	/*-------------------- getPrice tests --------------------*/
   		
   	/** Test getPrice after constructor is invoked. **/
      @Test public void priceTest() {
         
      /* set up item with price 10.99 */
			ApparelItem item = new ApparelItem("Jacket,06609,10.99");
         
      /* verify that getPrice matches expected output */
         Assert.assertEquals(10.99, item.getPrice(), 0.01);
      }
       
      /** Test getPrice with leading / trailing spaces in item code. **/
      @Test public void priceWithSpaceTest() {
         
       /* set up item with price 10.99 with leading / trailing spaces */
		 ApparelItem change = new ApparelItem("  Shorts , 5768 , 10.99 ");
        
       /* verify that getPrice matches expected output */
         Assert.assertEquals(10.99, change.getPrice(), 0.01);
      }
   	
       /** Test getPrice after resetting the code. **/
      @Test public void priceAfterSetTest() {
         
        /* set up item with price 10.99 with leading / trailing spaces */
		  ApparelItem frank = new ApparelItem("Scarf, 3429, 10.99");
        
        /* change price to 5.99 using setItemCode */
        frank.setItemCode("Scarf, 3429, 5.99");
        /* verify that getPrice matches expected output */
         Assert.assertEquals(5.99, frank.getPrice(), 0.01);
      }
   
   
   
         /*----------- sellItem and totalItemSales tests ------------*/
   		
       /** Test sellItem and totalItemSales. **/
      @Test public void sellItemTest() {
         ApparelItem item = new ApparelItem(" Wool Scarf  ,8564,10.2");
         item.sellItem();
         Assert.assertEquals(10.2, item.totalItemSales(), 0.01);
         item.sellItem();
         item.sellItem();
         item.sellItem();
         Assert.assertEquals(40.8, item.totalItemSales(), 0.01);
      }
       
    	/** Test sellItem and totalItemSales after setItemCode. **/
      @Test public void sellItemAfterSetTest() {
         ApparelItem item = new ApparelItem("Hat,45673,5.54");
         item.sellItem();
         Assert.assertEquals(5.54, item.totalItemSales(), 0.01);
         item.setItemCode("Hat,45673,10.54");
       	/* the price has changed and so the NEW price should be added
       	 in the code below */
         item.sellItem();
         item.sellItem();
         Assert.assertEquals(26.62, item.totalItemSales(), 0.01);
      }
   
   
   
   /*----------- toString tests (you should add more) ------------*/
   
   /** Make sure that toString output contains name. **/
      @Test public void nameInToStringTest() {
      
      /* check toString output for name (see slides on testing) */
       ApparelItem item = new ApparelItem("Hat,45673,5.54");
         item.sellItem();
         item.setItemCode("Hat,45673,10.54");
         item.sellItem();
         item.sellItem();
			boolean hasExp = item.toString().contains(item.getName());
			Assert.assertTrue(hasExp);
      }
		/** Make sure that toString output contains ID. **/
      @Test public void identityInToStringTest() {
      
      /* check toString output for ID */
       ApparelItem item = new ApparelItem("Hat,45673,5.54");
         item.sellItem();
         item.setItemCode("Folding cap,45958,16.54");
         item.sellItem();
         item.sellItem();
			boolean hasExp = item.toString().contains("45958");
			Assert.assertTrue(hasExp);
      }
		
		
		/** Make sure that toString output contains price. **/
      @Test public void priceInToStringTest() {
      
      /* check toString output for price */
       ApparelItem item = new ApparelItem("Hat,45673,5.54");
         item.sellItem();
         item.setItemCode("Orange socks,48935,8.84");
			boolean hasExp = item.toString().contains("8.84");
			Assert.assertTrue(hasExp);
      }
   
   
   
       /*----------- static mehtods tests (completed) ------------*/
       /** Test allItemSales. **/
      @Test public void allItemSalesTest() {
        
        /* get the latest allItemSales (might have been updated in 
           previous test */
         double salesBefore = ApparelItem.allItemSales();
         ApparelItem jeansItem = new ApparelItem("Jeans,45673,35.00");
         ApparelItem scarfItem = new ApparelItem("Scarf,45673,5.00");
         jeansItem.sellItem();
         scarfItem.sellItem();
         scarfItem.sellItem();
         /* offset sales to account for previous tests */
         Assert.assertEquals(45, ApparelItem.allItemSales() - salesBefore,
            0.01);
      }
   	
       /** Test highestSeller. **/
      @Test public void highestSellerTest() {
        
        /* get the current highest seller's sales (might have been 
           updated in previous test) */
         double currentHighest 
            = ApparelItem.highestSeller().totalItemSales();
            
         ApparelItem jeansItem = new ApparelItem("Jeans,45673,35.00");
         /* ensure that jeansItem is the new highest seller */
         while (jeansItem.totalItemSales() <= currentHighest) {  
            jeansItem.sellItem();
         }
       
         Assert.assertEquals(jeansItem, ApparelItem.highestSeller());
      }
   
   }
