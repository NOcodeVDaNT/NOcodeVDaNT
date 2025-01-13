public class operatingSystem {

 
        // Shared variables
        // 'flag' array indicates the intent of each process to enter the critical section.
        // 'flag[0]' is for Process 0, and 'flag[1]' is for Process 1.
        private static volatile boolean[] flag = new boolean[2]; 
    
        // 'turn' determines whose turn it is to enter the critical section.
        // It helps to resolve conflicts when both processes want to enter at the same time.
        private static volatile int turn;
    
        // Shared resource that both processes will modify in the critical section.
        private static int sharedCounter = 0;                    
    
        // Class representing Process 0
        private static class Process0 extends Thread {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) { // Execute the critical section 5 times
                    // Entry section: Indicate intent to enter critical section
                    flag[0] = true; // Process 0 signals its intent
                    turn = 1;       // Give priority to Process 1 if it also wants to enter
    
                    // Busy wait until it's safe to enter critical section
                    // Wait until Process 1 is not interested or it's Process 0's turn
                    while (flag[1] && turn == 1);
    
                    // Critical section: Safely modify the shared resource
                    System.out.println("Process 0: Entering critical section.");
                    sharedCounter++; // Increment shared counter
                    System.out.println("Process 0: Shared counter = " + sharedCounter);
                    try {
                        Thread.sleep(1000); // Simulate work in the critical section
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt(); // Handle interruption
                    }
                    System.out.println("Process 0: Leaving critical section.");
    
                    // Exit section: Indicate that Process 0 has left the critical section
                    flag[0] = false;
    
                    // Remainder section: Perform other non-critical tasks
                    try {
                        Thread.sleep(1000); // Simulate non-critical work
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            }
        }
    
        // Class representing Process 1
        private static class Process1 extends Thread {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) { // Execute the critical section 5 times
                    // Entry section: Indicate intent to enter critical section
                    flag[1] = true; // Process 1 signals its intent
                    turn = 0;       // Give priority to Process 0 if it also wants to enter
    
                    // Busy wait until it's safe to enter critical section
                    // Wait until Process 0 is not interested or it's Process 1's turn
                    while (flag[0] && turn == 0);
    
                    // Critical section: Safely modify the shared resource
                    System.out.println("Process 1: Entering critical section.");
                    sharedCounter++; // Increment shared counter
                    System.out.println("Process 1: Shared counter = " + sharedCounter);
                    try {
                        Thread.sleep(1000); // Simulate work in the critical section
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt(); // Handle interruption
                    }
                    System.out.println("Process 1: Leaving critical section.");
    
                    // Exit section: Indicate that Process 1 has left the critical section
                    flag[1] = false;
    
                    // Remainder section: Perform other non-critical tasks
                    try {
                        Thread.sleep(1000); // Simulate non-critical work
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            }
        }
    
        public static void main(String[] args) {
            // Initialize flags for both processes
            flag[0] = false;
            flag[1] = false;
    
            // Create and start threads representing the two processes
            Thread t0 = new Process0();
            Thread t1 = new Process1();
    
            t0.start(); // Start Process 0
            t1.start(); // Start Process 1
    
            // Wait for both threads to finish
            try {
                t0.join(); // Wait for Process 0 to finish
                t1.join(); // Wait for Process 1 to finish
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt(); // Handle interruption
            }
    
            // Print the final value of the shared counter after both processes finish
            System.out.println("Final value of shared counter = " + sharedCounter);
        }
    
    




    
}
