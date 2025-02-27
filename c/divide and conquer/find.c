// Find First and Last Position of Element in Sorted Array

#include <stdio.h>

int findFirst(int arr[], int n, int target) {
    int left = 0, right = n - 1, first = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            first = mid;  // Update first occurrence
            right = mid - 1;  // Search in left half
        } else if (arr[mid] < target) {
            left = mid + 1;  // Search right half
        } else {
            right = mid - 1; // Search left half
        }
    }
    return first;
}

int findLast(int arr[], int n, int target) {
    int left = 0, right = n - 1, last = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            last = mid;  // Update last occurrence
            left = mid + 1;  // Search in right half
        } else if (arr[mid] < target) {
            left = mid + 1;  // Search right half
        } else {
            right = mid - 1; // Search left half
        }
    }
    return last;
}

int main() {
    int arr[] = {1, 2, 2, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 2;

    int first = findFirst(arr, n, target);
    int last = findLast(arr, n, target);

    printf("First occurrence: %d\n", first);
    printf("Last occurrence: %d\n", last);

    return 0;
}
