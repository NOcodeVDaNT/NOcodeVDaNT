#include <stdio.h>
#include <stdlib.h>

// Partition function (used in QuickSelect)
int partition(int arr[], int left, int right) {
    int pivot = arr[right];  // Choosing the last element as pivot
    int i = left - 1;

    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    // Swap pivot to its correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[right];
    arr[right] = temp;

    return i + 1;
}

// QuickSelect function to find Kth smallest element
int quickSelect(int arr[], int left, int right, int k) {
    if (left <= right) {
        int pivotIndex = partition(arr, left, right);

        if (pivotIndex == k - 1) {
            return arr[pivotIndex];  // Found the Kth smallest
        } else if (pivotIndex > k - 1) {
            return quickSelect(arr, left, pivotIndex - 1, k);  // Search left part
        } else {
            return quickSelect(arr, pivotIndex + 1, right, k);  // Search right part
        }
    }
    return -1;  // Should not reach here
}

int main() {
    int arr[] = {7, 10, 4, 3, 20, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    int kthSmallest = quickSelect(arr, 0, n - 1, k);
    int kthLargest = quickSelect(arr, 0, n - 1, n - k + 1);

    printf("The %dth smallest element is: %d\n", k, kthSmallest);
    printf("The %dth largest element is: %d\n", k, kthLargest);

    return 0;
}
