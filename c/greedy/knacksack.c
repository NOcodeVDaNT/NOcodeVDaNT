#include <stdio.h>
#include <stdlib.h>


float *vw;
int size;
int *w;
int *v;
int wt;
float *final_allotment;

struct item {
    int weight;
    int value;
    float vw;
};

struct item *item;

// Function to adjust the structure array
void adjust(struct item item[], float vw[], int v[], int w[], int size) {
    for (int i = 0; i < size; i++) {
        item[i].weight = w[i];
        item[i].value = v[i];
        item[i].vw = vw[i]; // Store value-to-weight ratio
    }
    printItems(item, size);
}

// Function to print items
void printItems(struct item item[], int size) {
    printf("\nAdjusted Items:\n");
    for (int i = 0; i < size; i++) {
        printf("Item %d - Weight: %d, Value: %d, Value/Weight Ratio: %.2f\n",
               i + 1, item[i].weight, item[i].value, item[i].vw);
    }
}

// Function to calculate total weight
void total_weight(int w[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += w[i];
    }
    wt = sum;
}

// Function to find value-to-weight ratio
void findvw(int w[], int v[], int n) {
    for (int i = 0; i < n; i++) {
        vw[i] = (float)v[i] / w[i]; // Ensure floating-point division
    }
    insertionSortDescending(vw, n);
}

// Function to take input
void take_input() {
    int n;
    printf("Enter the number of items: \n");
    scanf("%d", &n);

    // Dynamic memory allocation
    vw = (float *)malloc(n * sizeof(float));
    final_allotment = (float *)malloc(n * sizeof(float));
    item = (struct item *)malloc(n * sizeof(struct item));
    v = (int *)malloc(n * sizeof(int));
    w = (int *)malloc(n * sizeof(int));

    size = n;

    printf("Enter the weights of the items: \n");
    for (int i = 0; i < n; i++) {
        printf("Enter %d item weight: ", i + 1);
        scanf("%d", &w[i]);
    }

    printf("Enter the values of the items: \n");
    for (int i = 0; i < n; i++) {
        printf("Enter %d item value: ", i + 1);
        scanf("%d", &v[i]);
    }

    findvw(w, v, n);
}

// Function to print an array
void printArray(float arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%.2f ", arr[i]);
    }
    printf("\n");
}

// Function to sort array in descending order
void insertionSortDescending(float arr[], int n) {
    for (int i = 1; i < n; i++) {
        float key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] < key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Main function
int main() {
    take_input();

    printf("What is the capacity of the sack? ");
    int capacity;
    scanf("%d", &capacity);

    total_weight(w, size);

    printf("Value-to-Weight Ratios:\n");
    for (int i = 0; i < size; i++) {
        printf("%.2f ", vw[i]);
    }
    printf("\n");
    

    return 0;
}
