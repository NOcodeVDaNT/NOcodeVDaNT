#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 100

// Graph structure using an adjacency list
typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

typedef struct Graph {
    int vertices;
    Node* adjList[MAX_NODES];  // Array of adjacency lists
    int visited[MAX_NODES];    // Visited array
} Graph;

// Create a new node
Node* createNode(int v) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

// Initialize graph
void initGraph(Graph* g, int vertices) {
    g->vertices = vertices;
    for (int i = 0; i < vertices; i++) {
        g->adjList[i] = NULL;
        g->visited[i] = 0;
    }
}

// Add an edge (undirected)
void addEdge(Graph* g, int src, int dest) {
    // Add edge from src to dest
    Node* newNode = createNode(dest);
    newNode->next = g->adjList[src];
    g->adjList[src] = newNode;

    // Add edge from dest to src (for undirected graph)
    newNode = createNode(src);
    newNode->next = g->adjList[dest];
    g->adjList[dest] = newNode;
}

// DFS traversal
void dfs(Graph* g, int vertex) {
    printf("%d ", vertex);
    g->visited[vertex] = 1; // Mark as visited

    Node* temp = g->adjList[vertex];
    while (temp) {
        int adjVertex = temp->vertex;
        if (!g->visited[adjVertex]) {
            dfs(g, adjVertex);
        }
        temp = temp->next;
    }
}

// Main function
int main() {
    Graph g;
    int vertices = 6;
    initGraph(&g, vertices);

    addEdge(&g, 0, 1);
    addEdge(&g, 0, 2);
    addEdge(&g, 1, 3);
    addEdge(&g, 1, 4);
    addEdge(&g, 2, 4);
    addEdge(&g, 3, 5);
    addEdge(&g, 4, 5);

    printf("DFS Traversal: ");
    dfs(&g, 0); // Start DFS from node 0
    printf("\n");

    return 0;
}
