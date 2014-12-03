public class Activity4A {

	public static void main(String[] args) {
	
	ProfileInformation p1, p2, p3;
	p1 = new ProfileInformation("Bob", "Smith");
	p1.setAge(70);
	p1.setLocation("Auburn");
	p1.logOn();
	System.out.println(p1 + "\n\r");
	
	p2 = new ProfileInformation("James", "Bond");
	p2.setAge(45);
	p2.setLocation("Saving The World");
	p2.logOn();
	System.out.println(p2 + "\n\r");
	
	p3 = new ProfileInformation("Albert", "Wallace");
	p3.setAge(21);
	p3.setLocation("In His Own Little World");
	p3.logOff();
	System.out.println(p3 + "\n\r");
	
		}

	}