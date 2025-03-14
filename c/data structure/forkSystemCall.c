#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid;

    // Create a child process
    pid = fork();

    if (pid < 0) {
        // If fork fails
        perror("Fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process: Executes this block
        printf("I am the child process. My task is to calculate 2 + 3.\n");
        printf("Result: 2 + 3 = %d\n", 2 + 3);
    } else {
        // Parent process: Executes this block
        printf("I am the parent process. My task is to print a message.\n");
        printf("Hello from the parent process!\n");
    }

    return 0;
}

output:I am the parent process. My task is to print a message.
Hello from the parent process!
I am the child process. My task is to calculate 2 + 3.
Result: 2 + 3 = 5


explanation:

In the parent-child process example I gave earlier, the reason both blocks appear to be executed is that both the parent and the child processes are running independently after the fork() system call.

Understanding Why Both Blocks Run
When fork() is called:

The parent process and child process both run concurrently. Each one has its own copy of the program's execution.
The return value of fork() is different for the parent and the child:
In the child process, fork() returns 0.
In the parent process, fork() returns the PID (Process ID) of the child.
Since both processes execute their own flow of the program, both the parent and child processes will run their respective code blocks. This is not due to an issue with if-else, but because you have two processes running at the same time.

Correct Explanation for Your Code:
In the parent process, fork() returns a non-zero value (the child's PID), so it will execute the else block.
In the child process, fork() returns 0, so it will execute the if block.
So, both the parent and child processes are running independently, which means both blocks can execute in their respective processes.