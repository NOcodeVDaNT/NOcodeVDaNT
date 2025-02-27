#include <stdio.h>
#include <stdlib.h>

// Min-Heap structure
typedef struct MinHeap {
    int *arr;
    int size;
} MinHeap;

// Swap function
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Heapify function
void heapify(MinHeap *heap, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < heap->size && heap->arr[left] < heap->arr[smallest])
        smallest = left;
    if (right < heap->size && heap->arr[right] < heap->arr[smallest])
        smallest = right;

    if (smallest != i) {
        swap(&heap->arr[i], &heap->arr[smallest]);
        heapify(heap, smallest);
    }
}

// Extract min element from heap
int extractMin(MinHeap *heap) {
    int min = heap->arr[0];
    heap->arr[0] = heap->arr[heap->size - 1];
    heap->size--;
    heapify(heap, 0);
    return min;
}

// Insert element into heap
void insertHeap(MinHeap *heap, int key) {
    int i = heap->size;
    heap->size++;
    heap->arr[i] = key;

    while (i != 0 && heap->arr[(i - 1) / 2] > heap->arr[i]) {
        swap(&heap->arr[i], &heap->arr[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

// Function to find the minimum cost of merging files
int optimalMerge(int files[], int n) {
    MinHeap heap;
    heap.arr = (int *)malloc(n * sizeof(int));
    heap.size = 0;

    // Insert all files into the heap
    for (int i = 0; i < n; i++) {
        insertHeap(&heap, files[i]);
    }

    int totalCost = 0;
    while (heap.size > 1) {
        int first = extractMin(&heap);
        int second = extractMin(&heap);
        int mergeCost = first + second;
        totalCost += mergeCost;
        insertHeap(&heap, mergeCost);
    }

    free(heap.arr);
    return totalCost;
}


// Function to maintain the Min Heap property
void minHeapify(int arr[], int size, int i) {
    int smallest = i;        // Assume current node is the smallest
    int left = 2 * i + 1;    // Left child index
    int right = 2 * i + 2;   // Right child index

    // Check if left child exists and is smaller than current smallest
    if (left < size && arr[left] < arr[smallest])
        smallest = left;

    // Check if right child exists and is smaller than current smallest
    if (right < size && arr[right] < arr[smallest])
        smallest = right;

    // If the smallest is not the current node, swap and continue heapifying
    if (smallest != i) {
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;

        minHeapify(arr, size, smallest); // Recursively heapify the affected subtree
    }
}



int main() {
    int files[] = {5, 3, 8, 6};
    int n = sizeof(files) / sizeof(files[0]);

    printf("Minimum merge cost: %d\n", optimalMerge(files, n));
    return 0;
}
