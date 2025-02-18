#include <stdio.h>

// Function to partition the array with first element as pivot
int partition(int arr[], int low, int high) {
    int pivot = arr[low];  // First element as pivot
    int i = low + 1, j = high;
    
    while (i <= j) {
        while (i <= high && arr[i] <= pivot) i++;
        while (j >= low && arr[j] > pivot) j--;
        
        if (i < j) {
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    // Swap pivot with arr[j] to place pivot at correct position
    int temp = arr[low];
    arr[low] = arr[j];
    arr[j] = temp;
    
    return j;  // New pivot position
}

// QuickSort function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);
        quickSort(arr, low, pivotIndex - 1);  // Sort left part
        quickSort(arr, pivotIndex + 1, high); // Sort right part
    }
}

// Function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {34, 7, 23, 32, 5, 62, 32};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, size);
    
    quickSort(arr, 0, size - 1);
    
    printf("Sorted array: ");
    printArray(arr, size);
    
    return 0;
}
