import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Button implements ActionListener {
    static JButton button;

    public static void main(String[] args) {

        // Create a button
        button = new JButton("Click Me");
        button.setBounds(200, 200, 100, 100); 

        // Create a frame
        JFrame frame = new JFrame(); 
        frame.setSize(500, 500); 
        frame.setLayout(null); 
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        frame.add(button);

        // Add ActionListener to the button
        Button btnHandler = new Button(); // Create an instance of the class to handle the button action
        button.addActionListener(btnHandler);

        // Make the frame visible
        frame.setVisible(true);
    }

    // Override the actionPerformed method to define what happens when the button is clicked
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button) {
            System.out.println("Button clicked!");
        }
    }
}
