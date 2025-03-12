#include <stdio.h>
#include <limits.h>

// Function to compute the minimum cost of matrix multiplication
int matrixChainMultiplication(int arr[], int n) {
    int dp[n][n];

    // Initializing the diagonal with 0, as multiplying a single matrix needs no operations
    for (int i = 1; i < n; i++)
        dp[i][i] = 0;

    // Length of matrix chain (subproblem size)
    for (int len = 2; len < n; len++) {   
        for (int i = 1; i < n - len + 1; i++) {   //when l=2 then i=1 to n-1, when l=3 then i=1 to n-2 and so on
            int j = i + len - 1; // j is the ending index of the subsequence when i=1 and l=2 then j=2, when i=2 and l=2  then j=3 and so on
            dp[i][j] = INT_MAX;

            // Try different positions for splitting the product
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j];
                if (cost < dp[i][j])
                    dp[i][j] = cost;
            }
        }
    }
    return dp[1][n-1];  // Final result
}

// Driver code
int main() {
    int arr[] = {40, 20, 30, 10, 30};  // Example matrix dimensions
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Minimum number of multiplications is %d\n", matrixChainMultiplication(arr, n));
    return 0;
}
