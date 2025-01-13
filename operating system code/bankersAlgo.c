#include <stdio.h>
#include <stdbool.h>

#define MAX_PROCESSES 10      // Maximum number of processes
#define MAX_RESOURCES 10      // Maximum number of resources

// Function to check if the system is in a safe state
bool isSafe(int processes[], int available[], int max[][MAX_RESOURCES], int allocation[][MAX_RESOURCES], int need[][MAX_RESOURCES], int n, int m) {
    int work[MAX_RESOURCES];      // Work array to track available resources during the simulation
    bool finish[MAX_PROCESSES];  // Finish array to track which processes have finished
    int safeSequence[MAX_PROCESSES]; // To store the safe sequence
    int count = 0;               // Counter for the safe sequence index

    // Step 1: Initialize the work array (initially same as available resources)
    for (int i = 0; i < m; i++) {
        work[i] = available[i]; // Copy available resources to work array
    }

    // Step 2: Initialize the finish array (all processes are initially unfinished)
    for (int i = 0; i < n; i++) {
        finish[i] = false; // No process has finished initially
    }

    // Step 3: Main loop to find a safe sequence
    while (count < n) {
        bool found = false; // To check if a process can proceed

        for (int p = 0; p < n; p++) {
            if (!finish[p]) { // If process `p` has not finished
                bool canAllocate = true;

                // Step 3.1: Check if need of process `p` can be satisfied by available resources (work)
                for (int r = 0; r < m; r++) {
                    if (need[p][r] > work[r]) { // If any resource need exceeds available
                        canAllocate = false; // Process cannot proceed
                        break;
                    }
                }

                // Step 3.2: If resources can be allocated to process `p`
                if (canAllocate) {
                    for (int r = 0; r < m; r++) {
                        work[r] += allocation[p][r]; // Release allocated resources to work
                    }
                    safeSequence[count++] = p; // Add process `p` to the safe sequence
                    finish[p] = true;          // Mark process `p` as finished
                    found = true;              // Indicate a process was found
                }
            }
        }

        // If no process could proceed, the system is not in a safe state
        if (!found) {
            printf("System is not in a safe state.\n");
            return false;
        }
    }

    // Step 4: Print the safe sequence
    printf("System is in a safe state.\nSafe sequence: ");
    for (int i = 0; i < n; i++) {
        printf("P%d ", safeSequence[i]);
    }
    printf("\n");

    return true;
}

int main() {
    int n = 5; // Number of processes
    int m = 3; // Number of resource types (A, B, C)

    int processes[] = {0, 1, 2, 3, 4}; // Process IDs

    // Total resources in the system (e.g., A=10, B=5, C=7)
    int totalResources[] = {10, 5, 7}; // User asked about resource instances (here is their definition)

    // Available resources in the system (derived by subtracting allocated resources from total resources)
    int available[] = {3, 3, 2};

    // Maximum resources each process may request
    int max[][MAX_RESOURCES] = {
        {7, 5, 3}, // Max resources needed by process 0
        {3, 2, 2}, // Max resources needed by process 1
        {9, 0, 2}, // Max resources needed by process 2
        {2, 2, 2}, // Max resources needed by process 3
        {4, 3, 3}  // Max resources needed by process 4
    };

    // Resources currently allocated to each process
    int allocation[][MAX_RESOURCES] = {
        {0, 1, 0}, // Resources allocated to process 0
        {2, 0, 0}, // Resources allocated to process 1
        {3, 0, 2}, // Resources allocated to process 2
        {2, 1, 1}, // Resources allocated to process 3
        {0, 0, 2}  // Resources allocated to process 4
    };

    // Remaining resource need of each process
    int need[MAX_PROCESSES][MAX_RESOURCES];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            need[i][j] = max[i][j] - allocation[i][j]; // Need = Max - Allocation
        }
    }

    // Check if the system is in a safe state
    isSafe(processes, available, max, allocation, need, n, m);

    return 0;
}
