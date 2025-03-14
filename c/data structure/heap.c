#include<stdio.h>
int insertMIN(int arr[], int size, int x) {
    arr[size] = x; // Insert at the end
    int i = size;
    size++; // Increase the size

    // Heapify-up (Percolate-up)
    while (i > 0 && arr[(i - 1) / 2] > arr[i]) {
        int temp = arr[i];
        arr[i] = arr[(i - 1) / 2];
        arr[(i - 1) / 2] = temp;
        
        i = (i - 1) / 2; // Move to the parent index
    }

    return size; // Return updated size
}

int deleteMAXheap(int a[], int n) {
    if (n <= 0) {
        printf("Heap is empty.\n");
        return -1; 
    }

    
    int maxElement = a[0];

    // Replace the root with the last element in the heap
    a[0] = a[n - 1];
    n--; // Reduce the size of the heap

    
    int i = 0;
    while (1) {
        int largest = i;        // Assume current node is largest
        int left = 2 * i + 1;   // Left child index
        int right = 2 * i + 2;  // Right child index

        // Check if left child exists and is larger than current
        if (left < n && a[left] > a[largest]) {
            largest = left;
        }

        // Check if right child exists and is larger than current largest
        if (right < n && a[right] > a[largest]) {
            largest = right;
        }

        // If the largest is still the current node, the heap is valid
        if (largest == i) {
            break;
        }

        // Swap the current node with the largest child
        int temp = a[i];
        a[i] = a[largest];
        a[largest] = temp;

        // Move to the largest child
        i = largest;
    }

    return maxElement;
}

void heapifyMAXadjust(int a[],int size,int index)
{
    int largest = index;
    int left = 2 * index +1 ;
    int right = 2 * index + 2;

    if(left<=size && a[left]>a[largest]){
        largest = left;
    }

    if(right<=size && a[right]>a[largest]){
        largest = right;
    }

    if(largest!=index){
        int temp=a[index];
        a[index]=a[largest];
        a[largest]=temp;
        heapifyMAXadjust(a,size,largest);
    }

}

void printHeap(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int insertMAX(int arr[], int size, int x) {
    arr[size] = x; // Insert at the end
    int i = size;
    size++; // Increase the size

    // Heapify-up (Percolate-up)
    while (i > 0 && arr[(i - 1) / 2] < arr[i]) { // Change condition to '>'
        int temp = arr[i];
        arr[i] = arr[(i - 1) / 2];
        arr[(i - 1) / 2] = temp;
        
        i = (i - 1) / 2; // Move to the parent index
    }

    return size; // Return updated size
}


int main(){

 int arr[]={2,3,1,5,8,4};
 int size=sizeof(arr)/sizeof(arr[0]);
 heapSort(arr,size);
 for (int i = 0; i < size; i++){
        printf("%d ", arr[i]);
 }
    printf("\n");


}
