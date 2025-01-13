import java.util.concurrent.Semaphore;
import java.util.LinkedList;
import java.util.Queue;

class BoundedBuffer {
    private final Queue<Integer> buffer; // Buffer to store items
    private final int capacity;         // Maximum capacity of the buffer

    // Semaphores to manage access and synchronization
    private final Semaphore emptySlots; // Tracks empty slots in the buffer
    private final Semaphore fullSlots;  // Tracks filled slots in the buffer
    private final Semaphore mutex;      // For mutual exclusion

    public BoundedBuffer(int capacity) {
        this.capacity = capacity;
        this.buffer = new LinkedList<>();
        this.emptySlots = new Semaphore(capacity); // Start with all slots empty
        this.fullSlots = new Semaphore(0);         // Start with no items in buffer
        this.mutex = new Semaphore(1);             // For exclusive access
    }

    // Produce an item and add it to the buffer
    public void produce(int item) throws InterruptedException {
        emptySlots.acquire(); // Wait for an empty slot
        mutex.acquire();      // Lock the buffer
        buffer.add(item);     // Add the item to the buffer
        System.out.println("Producer produced: " + item);
        mutex.release();      // Unlock the buffer
        fullSlots.release();  // Signal that an item is available
    }

    // Consume an item from the buffer
    public int consume() throws InterruptedException {
        fullSlots.acquire();  // Wait for a filled slot
        mutex.acquire();      // Lock the buffer
        int item = buffer.poll(); // Remove the item from the buffer
        System.out.println("Consumer consumed: " + item);
        mutex.release();      // Unlock the buffer
        emptySlots.release(); // Signal that an empty slot is available
        return item;
    }
}

class Producer extends Thread {
    private final BoundedBuffer buffer;

    public Producer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            int item = 0; // Item to produce
            while (true) {
                buffer.produce(item++); // Produce an item
                Thread.sleep(1000);     // Simulate production time
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class Consumer extends Thread {
    private final BoundedBuffer buffer;

    public Consumer(BoundedBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            while (true) {
                buffer.consume();      // Consume an item
                Thread.sleep(1500);    // Simulate consumption time
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class BoundedBufferProblem {
    public static void main(String[] args) {
        int bufferCapacity = 5; // Maximum size of the buffer
        BoundedBuffer buffer = new BoundedBuffer(bufferCapacity);

        Producer producer = new Producer(buffer);
        Consumer consumer = new Consumer(buffer);

        producer.start(); // Start the producer thread
        consumer.start(); // Start the consumer thread
    }
}
