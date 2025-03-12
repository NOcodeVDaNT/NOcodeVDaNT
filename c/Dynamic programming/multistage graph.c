#include <stdio.h>
#include <limits.h>

#define MAX_NODES 100  // Maximum number of nodes in the graph

int memo[MAX_NODES];  // Memoization table
int n;  // Number of nodes

// Function to find the shortest path using recursion with memoization
int shortest_path(int graph[MAX_NODES][MAX_NODES], int node) {
    if (node == n - 1)  // If it's the destination node, return 0
        return 0;

    if (memo[node] != -1)  // Return memoized result if available
        return memo[node];

    int min_cost = INT_MAX;

    for (int next = 0; next < n; next++) {
        if (graph[node][next] != 0) {  // If an edge exists
            int cost = graph[node][next] + shortest_path(graph, next);
            if (cost < min_cost)
                min_cost = cost;
        }
    }

    memo[node] = min_cost;  // Store result in memo table
    return min_cost;
}

// Wrapper function to initialize memoization table
int multi_stage_graph(int graph[MAX_NODES][MAX_NODES], int total_nodes) {
    n = total_nodes;

    // Initialize memoization table with -1 (indicating uncomputed values)
    for (int i = 0; i < n; i++) {
        memo[i] = -1;
    }

    return shortest_path(graph, 0);  // Start from source node (0)
}

int main() {
    int graph[MAX_NODES][MAX_NODES] = {0};
    int total_nodes, edges;

    printf("Enter the number of nodes: ");
    scanf("%d", &total_nodes);

    printf("Enter the number of edges: ");
    scanf("%d", &edges);

    printf("Enter edges (source destination weight):\n");
    for (int i = 0; i < edges; i++) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        graph[u][v] = w;  // Directed weighted edge
    }

    int shortest_cost = multi_stage_graph(graph, total_nodes);
    printf("The shortest path cost from source to destination is: %d\n", shortest_cost);

    return 0;
}
