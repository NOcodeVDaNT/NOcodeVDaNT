#include <stdio.h>
#include <string.h>

// Recursive function to find LCS length
int lcs(char *X, char *Y, int m, int n) {
    // Base Case: If either string is empty, LCS length is 0
    if (m == 0 || n == 0)
        return 0;

    // If last characters match, move diagonally left-up
    if (X[m-1] == Y[n-1])
        return 1 + lcs(X, Y, m-1, n-1);

    // If last characters don't match, take the max of two cases
    return (lcs(X, Y, m-1, n) > lcs(X, Y, m, n-1)) ? lcs(X, Y, m-1, n) : lcs(X, Y, m, n-1);
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
