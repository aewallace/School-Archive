import java.util.ArrayList;

public class ItemList
{
	private ArrayList<InventoryItem> list;
	
	public ItemList()
		{
		list = new ArrayList<InventoryItem>();
		}
		
	public static void main(String[] args)
		{
		ItemList itemList = new ItemList();
		InventoryItem.setTaxRate(0.05);
		
		itemList.addItem(new ElectronicsItem("Laptop", 1234.56, 10));
		itemList.addItem(new InventoryItem("Motor Oil",9.8));
		itemList.addItem(new OnlineBook("All Things Java", 12.3));
		itemList.addItem(new OnlineArticle("Off-Color Acronyms", 3.4));
		
		System.out.println(itemList + "\n\r");
		System.out.println("Total Price: $"
			+ itemList.getTotalPrice(1.5) + "\r\n");
			
		
		}
	
	public void addItem(InventoryItem itemIn)
		{
		list.add(itemIn);
		}
	
	public double getTotalPrice(double shipRate)
		{
		double price = 0;
		
		for (InventoryItem item : list)
			{
			if (item instanceof ElectronicsItem)
				{
				price += ((ElectronicsItem) item).calculateCost(shipRate);
				}
			else
				{
				price += item.calculateCost();
				}
			}
		
		return price;
		}
		
	public String toString()
		{
		String output = "All inventory:\r\n\r\n";
		
		for (InventoryItem itemOut : list)
			{
			output += "\r\n" + itemOut + "\r\n";
			}
		
		return output;
		}
	
	
}