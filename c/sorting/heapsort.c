#include <stdio.h>

// Function to heapify a subtree rooted at index i in a Min-Heap
void heapify(int arr[], int n, int i) {
    int smallest = i;  
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] < arr[smallest])
        smallest = left;

    if (right < n && arr[right] < arr[smallest])
        smallest = right;

    if (smallest != i) {
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;

        heapify(arr, n, smallest);
    }
}

// Function to build a Min-Heap from an array
void buildMinHeap(int arr[], int n) {
    for (int i = (n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

// Function to perform Min-Heap Sort
void heapSort(int arr[], int n) {
    buildMinHeap(arr, n);

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[0]);  // Print the smallest element (root)
        arr[0] = arr[n - 1 - i]; // Replace root with last element
        heapify(arr, n - 1 - i, 0);  // Restore Min-Heap property
    }
}

int main() {
    int arr[] = {5, 3, 8, 4, 2, 7, 1, 9};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Sorted array (Heap Sort using Min-Heap): ");
    heapSort(arr, n);

    return 0;
}
