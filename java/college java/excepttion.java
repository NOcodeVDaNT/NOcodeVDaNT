public class excepttion {
    public static void main(String[] args) {
        try{
            System.out.println("dividing of computation");
            int b=23/0;
            System.out.println("divided by zero");
        }
        catch(Exception e){

            System.out.println(e);

        }
        finally{
            System.out.println("we are in final block");

        }
    }
}
