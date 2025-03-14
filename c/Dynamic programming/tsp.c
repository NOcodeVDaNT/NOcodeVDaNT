#include <stdio.h>
#include <limits.h>

#define N 4  // Number of cities
#define INF INT_MAX

int tsp(int dist[N][N]) {
    int dp[1 << N][N];

    // Initialize DP table
    for (int mask = 0; mask < (1 << N); mask++)
        for (int i = 0; i < N; i++)
            dp[mask][i] = INF;

    // Base case: Start from city 0
    dp[1][0] = 0;

    // Iterate over all subsets of visited cities
    for (int mask = 1; mask < (1 << N); mask++) {
        for (int u = 0; u < N; u++) {
            if (mask & (1 << u)) { // If u is in subset
                for (int v = 0; v < N; v++) {
                    if (!(mask & (1 << v)) && dist[u][v] != INF) { // If v is not in subset
                        int newMask = mask | (1 << v);
                        dp[newMask][v] = (dp[newMask][v] < dp[mask][u] + dist[u][v]) ? dp[newMask][v] : (dp[mask][u] + dist[u][v]);
                    }
                }
            }
        }
    }

    // Find the minimum cost to return to the starting city
    int minCost = INF;
    for (int i = 1; i < N; i++) {
        if (dist[i][0] != INF) {
            minCost = (minCost < dp[(1 << N) - 1][i] + dist[i][0]) ? minCost : (dp[(1 << N) - 1][i] + dist[i][0]);
        }
    }
    return minCost;
}

int main() {
    int dist[N][N] = {
        {INF, 10, 15, 20},
        {10, INF, 35, 25},
        {15, 35, INF, 30},
        {20, 25, 30, INF}
    };
    printf("Minimum TSP cost (Bottom-Up): %d\n", tsp(dist));
    return 0;
}
