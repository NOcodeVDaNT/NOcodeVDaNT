 class A extends Thread{
    @Override
    public void run(){
        try {
            for(int i=0;i<=5;i++){
                System.out.println("threading is running");
                Thread.sleep(1000);
            }
        } catch (Exception e) {
            System.out.println("Exception in thread");
        }
    }

 }
 //sleep method  give interrupted exception thats we use throws keyword to handle it in main method


public class extend {
    public static void main(String[] args) throws InterruptedException{
        A a = new A();
        a.start();
        for (int i = 0; i < 5; i++) {
            System.out.println("vedant");
            Thread.sleep(1000);
        }
        
    }
}
