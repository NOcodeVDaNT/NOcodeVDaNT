import java.util.*;// use to import scanner class

public class stringss {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);

        //string are immutable(unchangeble)

        System.out.println("enter your name");
        String tony=sc.nextLine();
        System.out.println(tony);

        String firstname="tony";
        String lastname= "stark";
        String fullname=firstname+" "+lastname;
        System.out.println(fullname);

        System.out.println(fullname.length()); //include spaces too

        //will print character at index i
        for(int i=0;i<fullname.length();i++){
            System.out.println(fullname.charAt(i));
        }


        //campare two strings

        String name1="tony";
        String name2="tony";


        //it compare by:-
        //s1>s2 : +ve
        //s1==s2 : 0
        //s1<s2 : -ve

        
        if(name1.compareTo(name2)==0){
            System.out.println("both name are same");

        }

        //another way of making string which do not store in variable is :
        //   * new String("tony"); *


        //substring
        String sentence="my name is tony stark";
        String name=sentence.substring(11 ,sentence.length());
        System.out.println(name);


        //STRING BUILDER :- use to modify (add,delete,etc..)string without creating a new one inside heap becoz when we change syring using "+" it create a new variable in heap which take time 

        StringBuilder sb=new StringBuilder("tony");
        System.out.println(sb);

        System.out.println(sb.charAt(0));
       
        sb.setCharAt(0, 'p');
        System.out.println(sb);

        sb.insert(0, 's');
        System.out.println(sb);

        sb.delete(0, 1);
        System.out.println(sb);

        sb.append("stark");
        System.out.println(sb);


        //REVRSING A STRING
     


        for(int i=0;i<sb.length()/2;i++){
            int front =i;
            int back =sb.length()-1-i;

            char frontchar=sb.charAt(front);
            char backchar=sb.charAt(back);

            sb.setCharAt(front, backchar);
            sb.setCharAt(back, frontchar);

        }


        System.out.println(sb);

        
        








    }

    
}
