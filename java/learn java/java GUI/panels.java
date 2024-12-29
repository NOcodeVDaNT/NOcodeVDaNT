import javax.swing.*;
import java.awt.Color;
import java.awt.Image;
import java.awt.BorderLayout;


public class panels {
    public static void main(String[] args) {

        //panel are component that functions as a container to hold other component
        JPanel redpanel =new JPanel();
        redpanel.setBackground(Color.red);
        redpanel.setBounds(0, 0, 250, 250);
        //positioning label within the panel
        redpanel.setLayout(new BorderLayout());
        
        


        JPanel bluepanel =new JPanel();
        bluepanel.setBackground(Color.blue);
        bluepanel.setBounds(251, 0, 250, 250);
        bluepanel.setLayout(null);
        

        JPanel greenpanel =new JPanel();
        greenpanel.setBackground(Color.green);
        greenpanel.setBounds(0, 251, 500, 250);

        //lets now add a component for that create a label
        JLabel label = new JLabel();
        JLabel redlabel = new JLabel("ghost");
        redlabel.setVerticalAlignment(JLabel.CENTER); //positon 
        redlabel.setHorizontalAlignment(JLabel.CENTER);

        JLabel bluelabel = new JLabel("ghost");
        bluelabel.setForeground(new Color(255,255,255));
        bluelabel.setBounds(100,50,200,200); //without setting any layout manager we can also position labels



        label.setText("ghost are not real");
        
        ImageIcon img= new ImageIcon("photo.jpeg");
        Image image = img.getImage();
        Image resizedImage = image.getScaledInstance(100, 100, Image.SCALE_SMOOTH);
        ImageIcon resizedIcon = new ImageIcon(resizedImage);

        label.setIcon(resizedIcon);
        greenpanel.add(label);
        redpanel.add(redlabel);
        bluepanel.add(bluelabel);
        

        //movement of lebels within panel
        greenpanel.setLayout(new BorderLayout()); //by border layout(by default layour manager) now we can use set vertical/hoorizontal function 
        label.setVerticalAlignment(JLabel.CENTER); //positon 
        label.setHorizontalAlignment(JLabel.CENTER);
        greenpanel.add(label, BorderLayout.CENTER); //The BorderLayout is a layout manager that divides the container (in this case, greenPanel) into five regions: NORTH, SOUTH, EAST, WEST, and CENTER.



        JFrame frame= new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);
        frame.setSize(750,750);
        frame.setVisible(true);
        frame.add(redpanel);
        frame.add(bluepanel);
        frame.add(greenpanel);

    }

    
}
