#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Maximum size of the queue

int queue[MAX];
int front = -1;
int rear = -1;

// Function to check if the queue is full
int isFull() {
    if ((front == 0 && rear == MAX - 1) || (rear == (front - 1) % (MAX - 1))) {
        return 1;
    }
    return 0;
}

// Function to check if the queue is empty
int isEmpty() {
    if (front == -1) {
        return 1;
    }
    return 0;
}

// Function to add an element to the queue
void enqueue(int value) {
    if (isFull()) {
        printf("Queue Overflow! Cannot enqueue %d\n", value);
        return;
    }

    if (front == -1) {  // First element to be inserted
        front = 0;
        rear = 0;
    } else if (rear == MAX - 1 && front != 0) {  // Circular increment
        rear = 0;
    } else {
        rear++;
    }
    queue[rear] = value;
    printf("Enqueued %d\n", value);
}

// Function to delete an element from the queue
int dequeue() {
    if (isEmpty()) {
        printf("Queue Underflow! Cannot dequeue\n");
        return -1;
    }

    int value = queue[front];
    if (front == rear) {  // Only one element was in the queue
        front = -1;
        rear = -1;
    } else if (front == MAX - 1) {
        front = 0;  // Circular increment
    } else {
        front++;
    }
    return value;
}

// Function to display the elements in the queue
void display() {
    if (isEmpty()) {
        printf("Queue is empty\n");
        return;
    }

    printf("Queue elements are: ");
    if (rear >= front) {
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
    } else {  // For circular queue
        for (int i = front; i < MAX; i++) {
            printf("%d ", queue[i]);
        }
        for (int i = 0; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
    }
    printf("\n");
}

int main() {
    int choice, value;

    while (1) {
        printf("\nQueue Operations:\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to enqueue: ");
                scanf("%d", &value);
                enqueue(value);
                break;
            case 2:
                value = dequeue();
                if (value != -1) {
                    printf("Dequeued value is: %d\n", value);
                }
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
