public class join {
    public static void main(String[] args) {
       
        A t1=new A();
        A t2=new A();
        A t3=new A();

    t1.setName("thread 1");
    t2.setName("thread 2");
    t3.setName("thread 3");


    t2.start();
    try {
        t2.join(); //.join method when called on a thread causes the calling thread to wait until the thread it is called on is executed full and it can give interrupted exception
        
    } catch (InterruptedException e) {
        System.out.println("Thread 2 is interrupted");
    }

    t1.start();
    t3.start();
    

    }
}
class A extends Thread{
    public void run() {
        String n=Thread.currentThread().getName();
        for (int i = 0; i < 3; i++) {
            System.out.println(n);
        }
    }
}
