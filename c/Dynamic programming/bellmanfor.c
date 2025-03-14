#include <stdio.h>
#include <limits.h>

// Structure to store an edge (u -> v with weight w)
struct Edge {
    int src, dest, weight;
};

// Function to run the Bellman-Ford algorithm
void bellmanFord(int V, int E, struct Edge edges[], int source) {
    int distance[V];

    // Step 1: Initialize distances from source to all vertices as INFINITY
    for (int i = 0; i < V; i++)
        distance[i] = INT_MAX;
    distance[source] = 0; // Distance to itself is 0

    // Step 2: Relax all edges (V-1) times
    for (int i = 0; i < V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].src;
            int v = edges[j].dest;
            int w = edges[j].weight;

            // If the source vertex distance is not infinity and the new distance is shorter
            if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
                distance[v] = distance[u] + w;
            }
        }
    }

    // Step 3: Check for negative weight cycles
    for (int j = 0; j < E; j++) {
        int u = edges[j].src;
        int v = edges[j].dest;
        int w = edges[j].weight;

        if (distance[u] != INT_MAX && distance[u] + w < distance[v]) {
            printf("Graph contains a negative weight cycle!\n");
            return;
        }
    }

    // Print the shortest distances
    printf("Vertex   Distance from Source (%d)\n", source);
    for (int i = 0; i < V; i++)
        printf("%d \t\t %d\n", i, distance[i]);
}

// Main function
int main() {
    int V = 5; // Number of vertices
    int E = 8; // Number of edges

    struct Edge edges[] = {
        {0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2}, {1, 4, 2},
        {3, 2, 5}, {3, 1, 1}, {4, 3, -3}
    };

    int source = 0; // Start from vertex 0
    bellmanFord(V, E, edges, source);

    return 0;
}
