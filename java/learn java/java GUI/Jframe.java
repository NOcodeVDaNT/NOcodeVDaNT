import java.awt.Color;

import javax.swing.*;

public class Jframe {
    public static void main(String[] args) {


        JFrame frame= new JFrame();//create a frame
        frame.setTitle("you can set tittle of your app");
        frame.setSize(420,420); //set dimenstion of frame
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//when X button click we wil exit from application
        frame.setResizable(false);//prevent frame from being resize
        ImageIcon image=new ImageIcon("logo.jpg");//create an image icon
        frame.setIconImage(image.getImage());//change icon of frame from java default logo
        frame.getContentPane().setBackground(new Color(123,50,250));//set background color of frame
        




        frame.setVisible(true);//make frame visible


    
    }
}
