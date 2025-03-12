#include <stdio.h>
#include <stdlib.h>

typedef struct Job {
    char id;      // Job ID (e.g., 'A', 'B', 'C', etc.)
    int deadline; // Deadline of the job
    int profit;   // Profit if the job is completed within its deadline
} Job;

// Function to compare two jobs based on profit (for sorting in descending order)
int compareJobs(const void *a, const void *b) {
    return ((Job *)b)->profit - ((Job *)a)->profit;
}

// Function to find the maximum deadline among jobs
int findMaxDeadline(Job jobs[], int n) {
    int max = 0;
    for (int i = 0; i < n; i++) {
        if (jobs[i].deadline > max)
            max = jobs[i].deadline;
    }
    return max;
}

// Function to schedule jobs and maximize profit
void jobSequencing(Job jobs[], int n) {
    // Step 1: Sort jobs by profit in descending order
    qsort(jobs, n, sizeof(Job), compareJobs);

    // Step 2: Find the maximum deadline
    int maxDeadline = findMaxDeadline(jobs, n);

    // Step 3: Create an array to track occupied slots
    char schedule[maxDeadline]; // Job IDs assigned to each slot
    int slot[maxDeadline];      // Mark slot availability (1 = occupied, 0 = free)

    for (int i = 0; i < maxDeadline; i++) {
        slot[i] = 0; // Initialize all slots as free
        schedule[i] = '-'; // No job assigned initially
    }

    int totalProfit = 0;

    // Step 4: Assign jobs to the latest available slot before their deadline
    for (int i = 0; i < n; i++) {
        for (int j = jobs[i].deadline - 1; j >= 0; j--) {
            if (slot[j] == 0) { // If slot is free
                schedule[j] = jobs[i].id; // Assign job
                slot[j] = 1; // Mark slot as occupied
                totalProfit += jobs[i].profit; // Add profit
                break; // Move to the next job
            }
        }
    }

    // Step 5: Print the scheduled jobs and total profit
    printf("Scheduled Jobs: ");
    for (int i = 0; i < maxDeadline; i++) {
        if (schedule[i] != '-')
            printf("%c ", schedule[i]);
    }
    printf("\n\n------------------------\n\n\nMaximum Profit: %d\n", totalProfit);
}

// Main function to test the job sequencing algorithm
int main() {
    int n;
    printf("Enter the number of jobs: ");
    scanf("%d", &n);

    Job jobs[n]; // Array to store jobs

    printf("Enter Job ID, Deadline, and Profit for each job:\n");
    for (int i = 0; i < n; i++) {
        printf("Job %d: ", i + 1);
        scanf(" %c %d %d", &jobs[i].id, &jobs[i].deadline, &jobs[i].profit);
    }

    // Call job sequencing function
    jobSequencing(jobs, n);

    return 0;
}
