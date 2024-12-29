public class blocksynch {
    public static void main(String[] args) {
        msg m=new msg();
        ourthread t1=new ourthread(m, "tony");
        ourthread t2=new ourthread(m, "bruce");

        t1.start();
        t2.start();
        
    }
}
class ourthread extends Thread{
    msg m=new msg();
    String name;
    ourthread(msg m,String name){
        this.m=m;
        this.name=name;
        
    }
    public void run(){
        m.show(name);

    }


}
class msg{
    void show(String name){
        //100 line of code
       synchronized (this) { 
        for (int i = 0; i < 3; i++) {
            System.out.println("hello"+name);
        }
       }
        //100 line of code
    }
}
