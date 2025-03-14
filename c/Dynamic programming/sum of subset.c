#include <stdio.h>
#include <stdbool.h>

#define MAX_N 100  // Maximum array size
#define MAX_SUM 1000 // Maximum target sum

bool subsetSum(int arr[], int n, int target) {
    bool dp[n + 1][target + 1];

    // Initialize DP table
    for (int i = 0; i <= n; i++)
        dp[i][0] = true; // A sum of 0 is always possible

    for (int j = 1; j <= target; j++)
        dp[0][j] = false; // Without any element, no positive sum is possible

    // Fill the DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= target; j++) {
            if (arr[i - 1] <= j)
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
            else
                dp[i][j] = dp[i - 1][j];
        }
    }

    return dp[n][target]; // Final answer
}

int main() {
    int arr[] = {10, 7, 5, 18, 12, 20, 15};
    int target = 35;
    int n = sizeof(arr) / sizeof(arr[0]);

    if (subsetSum(arr, n, target))
        printf("Subset with the given sum exists!\n");
    else
        printf("No subset with the given sum.\n");

    return 0;
}
