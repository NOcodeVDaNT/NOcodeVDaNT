import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.BorderFactory;
import javax.swing.border.Border;
import java.awt.Font;
import java.awt.Color;
import java.awt.Image;


public class JLabelExample {
    public static void main(String[] args) {
        // Load the image
        ImageIcon img = new ImageIcon("logo.jpg");

        // Resize the image to 100x100 (you can adjust the size)
        Image image = img.getImage(); // Get the original image
        Image resizedImage = image.getScaledInstance(100, 100, Image.SCALE_SMOOTH); // Resize it to 100x100
        ImageIcon resizedIcon = new ImageIcon(resizedImage); // Create a new ImageIcon with the resized image

        //create a border
        Border border= BorderFactory.createLineBorder(Color.CYAN,5);

        // Create a label
        JLabel label = new JLabel(); // JLabel is a display area for text, images, or both.
        label.setText("Ghosts are real, I have seen them!"); // Set text for label
        label.setIcon(resizedIcon); // Set the resized icon on the label
        label.setHorizontalTextPosition(JLabel.CENTER); // Center the text horizontally(left,right,centre to the imageicon)
        label.setVerticalTextPosition(JLabel.TOP); // Position the text below the icon(top,bottom,centre to the imageicon)
        label.setForeground(new Color(123,50,250)); // font color change
        label.setFont(new Font("MV Boli",Font.BOLD,20)); //font style,size,family
        label.setIconTextGap(25); //gap between text and image
        label.setBackground(Color.BLACK); // this will set backgorund to only label but  frame.getContentPane().setBackground() will set in entire frame
        label.setOpaque(true);//display background on frame
        label.setBorder(border);  // Apply the cyan border to the label

        //allign label :set position of Icon+text within label
        label.setVerticalAlignment(JLabel.CENTER);
        label.setHorizontalAlignment(JLabel.CENTER);



        //limit size of label

        /*By default, a JFrame uses a BorderLayout, which may stretch components like JLabel to fill the available space.
        You can use other layout managers or off layout manager to limit the size of the label. [frame.setLayout(null);]*/
        label.setBounds(0, 0, 300, 300); // (x, y, width, height) of label




        










        // Create a frame
        JFrame frame = new JFrame(); // JFrame
        frame.setSize(500, 500); // Set the size of the frame
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Close the frame when the user clicks the close button

        // Add the label to the frame
        frame.add(label);

        // Make the frame visible
        frame.setVisible(true);
    }
}
