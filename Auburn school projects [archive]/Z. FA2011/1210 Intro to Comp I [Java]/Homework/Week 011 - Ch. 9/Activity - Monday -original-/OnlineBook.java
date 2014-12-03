public class OnlineBook extends OnlineTextItem
{
	protected String author;
	
	public OnlineBook(String bookNameIn, double priceIn)
	{
		super(bookNameIn, priceIn);
		author = "Author Not Listed";
	}
	
	public void setAuthor(String authorName)
	{
		author = authorName;
	}
	
	public String toString()
	{
	return name + " - " + author + ": " + price;
	}
}