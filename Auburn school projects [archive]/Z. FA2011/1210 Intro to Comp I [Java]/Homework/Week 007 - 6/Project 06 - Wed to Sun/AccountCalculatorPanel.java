   import javax.swing.JPanel;
   import javax.swing.JLabel;
   import javax.swing.JTextField;
   import javax.swing.JButton;
   import java.awt.Dimension;
   import java.awt.event.ActionListener;
   import java.awt.event.ActionEvent;
   import java.util.Scanner;
   import java.text.NumberFormat;
	
	 /**
	  * Creates a panel that allows users to enter account information
	  * in the format {lastname firstname cableboxes} and calculates the 
	  * total cost accordingly.
	  * Functionality for service selection has not been added; all
	  * costs will be based on the Basic cable package.
	  *
	  * @author Lauren Goff & Albert Wallace
	  * @version 9-2-2011 & 10/5/2011
	  */
   public class AccountCalculatorPanel extends JPanel {
   
      private JLabel inputLabel, outputLabel;
      private JTextField input, output;
      private JButton processButton, clearButton;
      
     /**
      * Instantiates a new panel with all of the GUI components,
   	* including input for name and # cable boxes. Includes a 
   	* button for calculating cost and a button for clearing input.
      */
      public AccountCalculatorPanel() {
        // create 3 nested panels
         JPanel topPanel = new JPanel();
         JPanel middlePanel = new JPanel();
         JPanel bottomPanel = new JPanel();
         
      	// instantiate components
         outputLabel = new JLabel("Total Cost");
         inputLabel = new JLabel("Account Information");
         processButton = new JButton("Calculate Cost");
         clearButton = new JButton("Clear");
         input = new JTextField(30);
         output = new JTextField(20);
         
         output.setEditable(false); // users can't change cost field
         output.setText("$ "); // cost field starts out with a $
         
      	// create a listener for the buttons and add it to each
         ProcessClearListener buttonListener = new ProcessClearListener();
         processButton.addActionListener(buttonListener);
         clearButton.addActionListener(buttonListener);
         
      	// add input label & box to top panel
         topPanel.add(inputLabel);
         topPanel.add(input);
      	// add buttons to middle panel
         middlePanel.add(processButton);
         middlePanel.add(clearButton);
         // add output label & box to bottom panel
         bottomPanel.add(outputLabel);
         bottomPanel.add(output);
         
      	// add nested panels to main panel
         this.add(topPanel);
         this.add(middlePanel);
         this.add(bottomPanel);
      	
      	// because there is no layout manager, set the panel size manually
         this.setPreferredSize(new Dimension(475, 150));
      }
      
   	/**
       * Calculates cost and updates cost panel if the calculate cost
   	 * button is pressed. Clears intput display and sets cost to a $
   	 * symbol if the clear button is pressed.
       */
      private class ProcessClearListener implements ActionListener {
      
         public void actionPerformed(ActionEvent event) {
            
            if (event.getSource() == processButton) {
					NumberFormat currencyFmt = NumberFormat.getCurrencyInstance();
					
               String readThisIn = input.getText();
               Scanner infoScan = new Scanner(readThisIn);
            
               String lastName = infoScan.next();
               String firstName = infoScan.next();
               int boxesForUser = infoScan.nextInt();
					
					String fullName = lastName + " " + firstName;
					
					CableAccount newAccount = new CableAccount(fullName);
					newAccount.setCableBoxes(boxesForUser);
					newAccount.setService(CableAccount.BASIC);
					
					double costs = newAccount.totalCost();
					String costOutput = currencyFmt.format(costs);
					
					output.setText(costOutput);
            }
            else if (event.getSource() == clearButton) {
               output.setText("$");
					input.setText("");
            }
            
         }
      }
   }