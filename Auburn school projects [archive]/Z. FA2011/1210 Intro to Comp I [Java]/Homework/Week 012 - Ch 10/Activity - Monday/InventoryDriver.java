public class InventoryDriver
{
	public static void main(String[] args)
	{
	InventoryItem.setTaxRate(0.05);
	InventoryItem oic = new InventoryItem("Oil change kit", 39.99);
	System.out.print(oic + "\n\r");
	
	ElectronicsItem cphone = new ElectronicsItem("Cordless phone", 80.00, 1.8);
	System.out.print(cphone + "\n\r");
	
	OnlineArticle jnews = new OnlineArticle("Java News", 8.50);
	jnews.setWordCount(700);
	System.out.print(jnews + "\n\r");
	
	OnlineBook jnoob = new OnlineBook("Java for Noobs", 13.37);
	jnoob.setAuthor("Lauren G");
	System.out.print(jnoob);
	}
}