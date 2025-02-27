#include <stdio.h>
#include <stdlib.h>

// Structure for a Huffman tree node
struct HuffmanNode {
    char data;  // Character
    int freq;   // Frequency of character
    struct HuffmanNode *left, *right;  // Left and right child
};

// Structure for the priority queue (min-heap)
struct MinHeap {
    int size;  // Number of nodes in heap
    struct HuffmanNode **array;  // Array of node pointers
};

// Function to create a new node
struct HuffmanNode* createNode(char data, int freq) {
    struct HuffmanNode* node = (struct HuffmanNode*)malloc(sizeof(struct HuffmanNode));
    node->data = data;
    node->freq = freq;
    node->left = node->right = NULL;
    return node;
}

// Function to swap two nodes in the heap
void swapNodes(struct HuffmanNode** a, struct HuffmanNode** b) {
    struct HuffmanNode* temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify function to maintain min-heap property
void minHeapify(struct MinHeap* heap, int index) {
    int smallest = index;
    int left = 2 * index + 1;
    int right = 2 * index + 2;

    if (left < heap->size && heap->array[left]->freq < heap->array[smallest]->freq)
        smallest = left;
    
    if (right < heap->size && heap->array[right]->freq < heap->array[smallest]->freq)
        smallest = right;
    
    if (smallest != index) {
        swapNodes(&heap->array[index], &heap->array[smallest]);
        minHeapify(heap, smallest);
    }
}

// Function to extract the minimum node from the heap
struct HuffmanNode* extractMin(struct MinHeap* heap) {
    struct HuffmanNode* temp = heap->array[0];  // The root node (minimum frequency)
    heap->array[0] = heap->array[heap->size - 1];  // Move last node to root
    heap->size--;  // Reduce heap size
    minHeapify(heap, 0);  // Restore min-heap property
    return temp;
}

// Function to insert a new node into the heap
void insertHeap(struct MinHeap* heap, struct HuffmanNode* node) {
    heap->size++;
    int i = heap->size - 1;

    // Place node at the correct position in min-heap
    while (i > 0 && node->freq < heap->array[(i - 1) / 2]->freq) {
        heap->array[i] = heap->array[(i - 1) / 2];
        i = (i - 1) / 2;
    }
    heap->array[i] = node;
}

// Function to build a Huffman tree from given characters and frequencies
struct HuffmanNode* buildHuffmanTree(char data[], int freq[], int size) {
    struct MinHeap* heap = (struct MinHeap*)malloc(sizeof(struct MinHeap));
    heap->size = 0;
    heap->array = (struct HuffmanNode**)malloc(size * sizeof(struct HuffmanNode*));

    // Insert all characters into the heap
    for (int i = 0; i < size; i++)
        insertHeap(heap, createNode(data[i], freq[i]));

    // Build the Huffman Tree
    while (heap->size > 1) {
        struct HuffmanNode *left = extractMin(heap);
        struct HuffmanNode *right = extractMin(heap);

        // Create an internal node with combined frequency
        struct HuffmanNode* newNode = createNode('$', left->freq + right->freq);
        newNode->left = left;
        newNode->right = right;

        insertHeap(heap, newNode);  // Insert the new node back into the heap
    }
    return extractMin(heap);  // The last remaining node is the root of the Huffman Tree
}

// Function to print Huffman codes from the tree
void printHuffmanCodes(struct HuffmanNode* root, int arr[], int top) {
    // If left child exists, add '0' to path and recurse
    if (root->left) {
        arr[top] = 0;
        printHuffmanCodes(root->left, arr, top + 1);
    }

    // If right child exists, add '1' to path and recurse
    if (root->right) {
        arr[top] = 1;
        printHuffmanCodes(root->right, arr, top + 1);
    }

    // If leaf node is reached, print the character and its code
    if (!root->left && !root->right) {
        printf("%c: ", root->data);
        for (int i = 0; i < top; i++)
            printf("%d", arr[i]);
        printf("\n");
    }
}

// Main function to demonstrate Huffman Encoding
int main() {
    char data[] = {'A', 'B', 'C', 'D', 'E', 'F'};
    int freq[] = {5, 9, 12, 13, 16, 45};  // Example frequency
    int size = sizeof(data) / sizeof(data[0]);

    // Build Huffman Tree
    struct HuffmanNode* root = buildHuffmanTree(data, freq, size);

    // Print Huffman codes
    int arr[100], top = 0;
    printf("Huffman Codes:\n");
    printHuffmanCodes(root, arr, top);

    return 0;
}
