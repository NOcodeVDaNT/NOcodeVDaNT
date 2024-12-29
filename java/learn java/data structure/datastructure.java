import java.util.ArrayList;// using arraylist data structure
import java.util.Collections;//for useinf collections framework

public class datastructure {
    public static void main(String[] args) {
        System.out.println("-------------------ARRAY LIST-----------------------------------------");
        ArrayList<Integer> list=new ArrayList<>();
        //ADD  elemnt in llist
        list.add(0);
        list.add(1);
        list.add(3);
        list.add(3);
        list.add(4);
       

        System.out.println(list);

        //add elemnt berween the list
        list.add(2, 2);
        System.out.println(list);

        //get elemt with index
        for(int i=0;i<list.size();i++){                                //list.size(); retunr number of elemnt
            System.out.println(list.get(i));
        }

        

        //set elemnt
        list.set(3, -1);
        System.out.println(list);

        //delete element
        list.remove(4);//index is given
        System.out.println(list);

        //sorting am arraylist
        Collections.sort(list);
        System.out.println(list);
        

        // collection framework:- 
        


        

        






    }    
 
    

}
