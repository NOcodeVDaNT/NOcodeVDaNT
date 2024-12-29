
class A implements Runnable{
    public void run() {
        for(int i=0;i<=5;i++){
            System.out.println("threading is running");
            
        }
    }
}
public class implement {
    public static void main(String[] args) {
        A a=new A();
        Thread t=new Thread(a);//since runnable interface dont have start mehtod it only have run mehtod so to
        //start the tread we need to create a thread object then we can pass A in it to execute the run method written in A

        t.start();
        for(int i=0;i<=5;i++){
            System.out.println(" MAIN threading is running");
            
        }
        
    }
    
}
