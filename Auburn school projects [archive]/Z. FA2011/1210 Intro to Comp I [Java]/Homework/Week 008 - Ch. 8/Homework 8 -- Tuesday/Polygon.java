  /**
   * Represents a polygon with a specified number of sides
   * lengths. The polygon is classified based on its number of sides.
   *
   * @author Lauren Goff
   */
   public class Polygon {
      
      private double[] sideLengths;
   
      public Polygon(double[] sidesIn)
			{
         setSides(sidesIn); 
      	}
      
      public void setSides(double[] sidesIn) 
			{  
         sideLengths = sidesIn != null ? sidesIn : sideLengths;
    	  	}
   
      public double[] getSides() 
			{  
         return sideLengths;
      	}
		
		public double[] getSidesGreaterThan(double minSize)
			{
			int numberThatAre = 0, entry = 0;
			
			for (int i = 0; i < sideLengths.length; i++)
				{
				if (sideLengths[i] > minSize)
					{
					numberThatAre++;
					}
				}
				
			double[] sidesGreaterThan = new double[numberThatAre];
			if (numberThatAre > 0)
				{
				for (int i = 0; i < sideLengths.length; i++)
					{
					if (sideLengths[i] > minSize)
						{
						sidesGreaterThan[entry] = sideLengths[i];
						entry++;
						}
					}
				}
			return sidesGreaterThan;
			}
		
		public double calculatePerimeter()
			{
			double sumOfLengths = 0;
			for (int i = 0; i < sideLengths.length; i++)
				{
				sumOfLengths += sideLengths[i];
				}
			return sumOfLengths;
			}
      
      public String toString() 
			{
         switch (sideLengths.length) 
				{
            case 0:
            case 1:
            case 2:
               return "non-polygon";
            case 3:
               return "triangle";
            case 4:
               return "rectangle";
            case 5:
               return "pentagon";
            case 6:
               return "hexagon";
            case 7:
               return "heptagon";
            case 8:
               return "octagon";
            default:
               return "n-gon";
         	}   
      	}   
   }
