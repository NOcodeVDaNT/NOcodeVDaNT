#include<stdio.h>

int BinarySearchRecursive(int a[], int low, int high, int x) {
    if (low > high) {
        return -1; // Base case: element not found
    }

    int mid = low + (high - low) / 2; // Calculate mid point

    if (a[mid] == x) {
        return mid; // Base case: element found
    }

    if (a[mid] < x) {
        return BinarySearchRecursive(a, mid + 1, high, x); // Search in the right half
    } else {
        return BinarySearchRecursive(a, low, mid - 1, x); // Search in the left half
    }
}


int BinarySearch(int a[], int n, int x) {
    int low = 0, high = n - 1; // Define search bounds
    while (low <= high) {  //jab tak karo jabtak low chota hai high se ,jab low bada ho jayenga tak element hi nahi milega
        int mid = low + (high - low) / 2; // Calculate mid point
        if (a[mid] == x) {
            return mid; // Element found, return index
        }
        if (a[mid] < x) {
            low = mid + 1; // Narrow down to the right half
        } else {
            high = mid - 1; // Narrow down to the left half
        }
    }
    return -1; // Element not found
}


int main() {
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = 10;
    int x = 4;

    int result = BinarySearchRecursive(a, 0, n - 1, x); // Initial call with full bounds

    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }

    return 0;
}
