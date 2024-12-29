import java.util.*;
class Car{
    public void start(){
        System.out.println("starting");
    }
    public void stop(){
        System.out.println("stop");
    }
    String price;
    public void price(){
        System.out.println("the price of the car is "+this.price);
    }
    
}
class Audi extends Car{
    String model;
}
public class inheritance{
    public static void main(String[] args) {
        Audi car1=new Audi();
        car1.model="R8";
        car1.price="272crore";
        car1.price();


        
    }
    
    
}
