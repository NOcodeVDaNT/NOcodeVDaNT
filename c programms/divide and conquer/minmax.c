#include <stdio.h>
#include <limits.h>

// Structure to store min and max values
struct MinMax {
    int min;
    int max;
};

// Function to find min and max using divide and conquer
struct MinMax findMinMax(int arr[], int low, int high) {
    struct MinMax result, left, right;
    
    // If there's only one element
    if (low == high) {
        result.min = result.max = arr[low];
        return result;
    }

    // If there are only two elements
    if (high == low + 1) {
        if (arr[low] > arr[high]) {
            result.max = arr[low];
            result.min = arr[high];
        } else {
            result.max = arr[high];
            result.min = arr[low];
        }
        return result;
    }

    // Divide the array into two halves
    int mid = (low + high) / 2;
    left = findMinMax(arr, low, mid);
    right = findMinMax(arr, mid + 1, high);

    // Merge results
    result.min = (left.min < right.min) ? left.min : right.min;
    result.max = (left.max > right.max) ? left.max : right.max;

    return result;
}

// Driver code
int main() {
    int arr[] = {7, 2, 10, 3, 8, 1, 15, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    struct MinMax result = findMinMax(arr, 0, n - 1);

    printf("Minimum value: %d\n", result.min);
    printf("Maximum value: %d\n", result.max);

    return 0;
}
