import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

//easy way to use buttons

public class asyButton {
    static JButton button;
    public static void main(String[] args) {

        button = new JButton("click");
        button.setToolTipText("This is a tooltip");
        button.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2)); // Custom border
        button.setBorderPainted(false);  // Remove the border

        button.setBounds(200, 200, 100, 100); 
        


        // ActionListener for button clickP
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Button clicked");
                button.setText("New Text"); // Change button text
                button.setBackground(Color.RED); // Set background color to red
                button.setForeground(Color.WHITE); // Set text color to white
            }
        });

        // MouseAdapter for detecting double-click
        button.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 2) {
                    System.out.println("Button double-clicked");
                    ImageIcon icon = new ImageIcon("photo.jpeg");
                    button.setIcon(icon);
                }
            }
        });

        JFrame frame = new JFrame(); 
        frame.setSize(500, 500); 
        frame.setLayout(null); 
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        frame.add(button);
        frame.setVisible(true);
    }
}
