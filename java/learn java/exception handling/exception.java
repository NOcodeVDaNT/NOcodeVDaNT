


public class exception {

    public static void main(String[] args) {
       int a=10,b=0;
       //try catch
       try {
           System.out.println(a/b);
       } catch (ArithmeticException e) {
        System.out.println(e);
       }

       //number format exception
       String name="ghost";
       try{
        int num=Integer.parseInt(name);
       }
       catch(NumberFormatException e){
        System.out.println(e);
       }
       

       //finally
       String str=null;
       try {
        System.out.println(str.toUpperCase());
       }
       catch(NullPointerException e){
        System.out.println(e);
       }
       finally{
        System.out.println("alway work code block");
       }


       //multiple try catch
       int[] array = new int[5];

       try {
        System.out.println(array[2]);
        System.out.println(array[5]);
           
       } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println(e);
       }
       String nam="ghost";
       try {
        System.out.println(nam.length());
        System.out.println(nam.charAt(5));
           
       } catch (StringIndexOutOfBoundsException e) {
        System.out.println(e);
       }



       //multiple catch block
       try{
            System.out.println(a/b);    //arthmetaic exception
            System.out.println(array[5]); //arrayout of bound exception
            System.out.println(nam.charAt(5)); //string index out of bound exception

       }
       catch(ArithmeticException e){
        System.out.println("inside muliple catch");
       }
       catch(ArrayIndexOutOfBoundsException e){
        System.out.println("inside muliple catch");
       }
       catch(StringIndexOutOfBoundsException e){
        System.out.println("inside muliple catch");
       }


       //nested try block
       try {
           //statment 1
           try {
               //statement 2
           } catch (Exception e) {
            System.out.println("nested catch");  //handled when statement 2 fails

           }
       } catch (Exception e) {
         System.out.println("outer catch"); //handled when statement 1 fails
       }



       //nested finally
       try {
        
       } catch (Exception e) {
        
       }
       finally{
        //when finally block also has some risky code
             try {
                System.out.println("finally block");
             } catch (Exception e) {
                 
             }
             finally{
                //most imported set of code that has to be run
                 System.out.println("inner finally");
             }
       }
       //throw and throws
       int age= 18;
       try {
        voteChecker(16); // This will throw an exception
    } catch (IllegalArgumentException e) {
        System.out.println(e.getMessage()); // Output: Not eligible for voting.
    }

     

      
    }

    public static  void voteChecker(int age) throws IllegalArgumentException {
        if (age < 18) {
            throw new IllegalArgumentException("Not eligible for voting.");
        } else {
            System.out.println("You are eligible to vote.");
        }
    }
    
}
