#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 100

// Queue structure for BFS
typedef struct {
    int items[MAX_NODES];
    int front, rear;
} Queue;

// Initialize queue
void initQueue(Queue* q) {
    q->front = -1;
    q->rear = -1;
}

// Check if queue is empty
int isEmpty(Queue* q) {
    return q->front == -1;
}

// Enqueue operation
void enqueue(Queue* q, int value) {
    if (q->rear == MAX_NODES - 1) {
        printf("Queue is full!\n");
        return;
    }
    if (q->front == -1) q->front = 0;
    q->items[++q->rear] = value;
}

// Dequeue operation
int dequeue(Queue* q) {
    if (isEmpty(q)) return -1;
    int item = q->items[q->front++];
    if (q->front > q->rear) q->front = q->rear = -1; // Reset queue
    return item;
}

// Graph structure
typedef struct {
    int vertices;
    int adj[MAX_NODES][MAX_NODES]; // Adjacency matrix representation
} Graph;

// Initialize graph
void initGraph(Graph* g, int vertices) {
    g->vertices = vertices;
    for (int i = 0; i < vertices; i++)
        for (int j = 0; j < vertices; j++)
            g->adj[i][j] = 0;
}

// Add edge
void addEdge(Graph* g, int src, int dest) {
    g->adj[src][dest] = 1;
    g->adj[dest][src] = 1; // Undirected graph
}

// BFS traversal
void bfs(Graph* g, int start) {
    int visited[MAX_NODES] = {0};
    Queue q;
    initQueue(&q);

    printf("BFS Traversal: ");
    visited[start] = 1;
    enqueue(&q, start);

    while (!isEmpty(&q)) {
        int node = dequeue(&q);
        printf("%d ", node);

        for (int i = 0; i < g->vertices; i++) {
            if (g->adj[node][i] == 1 && !visited[i]) {
                visited[i] = 1;
                enqueue(&q, i);
            }
        }
    }
    printf("\n");
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

    bfs(&g, 0); // Start BFS from node 0

    return 0;
}
