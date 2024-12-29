import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class arraylist {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        ArrayList<Integer> list =new ArrayList<Integer>(); // declaration
        ArrayList<String> list2 =new ArrayList<String>();  // declaration

        //add elements
        list.add(0);
        list.add(1);
        list.add(2);
        list.add(3);

        //printing a list
        System.out.println(list);

        //getting an element from index
        int element=list.get(2);
        System.out.println(element);

        //add elemnt in between
        list.add(1, 3);//index,elemnt
        System.out.println(list);

        //set element: replacing an existing element at index
        list.set(1, 4);
        System.out.println(list);

        //delete element
        list.remove(1);
        System.out.println(list);

        //size
        int size=list.size();
        System.out.println(size);

        //traversing in arraylst
        for(int i=0;i<list.size();i++){
            System.out.print(list.get(i));
        }

        //sorting 
        Collections.sort(list);
        System.out.println(list);

        list.removeAll(list);
        System.out.println((list) + " "+ (list.size()));








        
         
    }
}
