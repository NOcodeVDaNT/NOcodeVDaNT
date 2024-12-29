public class synchrinization {
   static class Bus implements Runnable{
        int available=1,passenger;
        Bus(){
            this.passenger=1;
        }
        public synchronized void run(){
            String name=Thread.currentThread().getName();
            if(available>=passenger){
                System.out.println(name+"reserves seat");
                available=available-passenger;

            }
            else{
                System.out.println("seat not available");
            }
        }
    }
    public static void main(String[] args) {
        Bus r=new Bus();
        Thread t1=new Thread(r);
        Thread t2=new Thread(r);
        Thread t3=new Thread(r);

        t1.setName("ram");
        t2.setName("lakshman");
        t3.setName("sita");

        t1.start();
        t2.start();
        t3.start();

      
    }
}
