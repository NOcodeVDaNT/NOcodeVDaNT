#include <stdio.h>
#include <string.h>

// Function to find LCS length
int lcs(char *X, char *Y, int m, int n) {
    int dp[m+1][n+1]; // DP table

    // Build the table bottom-up
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                dp[i][j] = 0; // Base case
            else if (X[i-1] == Y[j-1])
                dp[i][j] = 1 + dp[i-1][j-1]; // Characters match
            else
                dp[i][j] = (dp[i-1][j] > dp[i][j-1]) ? dp[i-1][j] : dp[i][j-1]; // Take max
        }
    }

    return dp[m][n]; // LCS length
}

// Driver Code
int main() {
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";
    int m = strlen(X);
    int n = strlen(Y);

    printf("Length of LCS: %d\n", lcs(X, Y, m, n));
    return 0;
}
