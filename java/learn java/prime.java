import java.util.*;

public class prime {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        

        int length=0;

        System.out.println("enter a number");

        int n=sc.nextInt();

        for(int i=2;i<=9;i++){
         
            if(n%i==0 && n!=i ){
                length=10;
        
           }
         
        }

        if (length==10) {
            System.out.println("not prime");
            
        }

        else if (length==0) {
            System.out.println("prime");
            
        }
       
}

}