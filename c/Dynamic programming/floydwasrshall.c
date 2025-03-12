#include <stdio.h>

#define INF 99999 
#define V 4       


void printSolution(int dist[V][V]) {
    printf("Shortest distances between every pair of vertices:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF)
                printf("%4s ", "INF");
            else
                printf("%4d ", dist[i][j]);
        }
        printf("\n");
    }
}


void floydWarshall(int graph[V][V]) {
    int dist[V][V];

    // Initialize distance matrix with graph values
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            dist[i][j] = graph[i][j];

    // Algorithm to update shortest paths
    for (int k = 0; k < V; k++) { // Consider each vertex as an intermediate
        for (int i = 0; i < V; i++) { // Source vertex
            for (int j = 0; j < V; j++) { // Destination vertex
                // Check if vertex k improves the shortest path from i to j
                if (dist[i][k] != INF && dist[k][j] != INF && 
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
                
            }
        }
    }

    
    printSolution(dist);
}


int main() {
    
    int graph[V][V] = {
        {0, 4, 2, 6},
        {2, 0, INF, 4},
        {INF, 1, 0, INF},
        {INF, INF, 2, 0}
    };

    
    floydWarshall(graph);

    return 0;
}
