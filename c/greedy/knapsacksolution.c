#include <stdio.h>
#include <stdlib.h>

// Structure for an item with weight, value, and value/weight ratio
struct Item {
    int weight;
    int value;
    double ratio;
};

// Comparison function to sort items by value/weight ratio in descending order
int compare(const void *a, const void *b) {
    struct Item *item1 = (struct Item *)a;
    struct Item *item2 = (struct Item *)b;
    return (item2->ratio  > item1->ratio) - (item2->ratio < item1->ratio);
    // Compare based on value/weight ratio in descending order
    // If item2's ratio is greater, return 1 (swap needed)
    // If item1's ratio is greater, return -1 (no swap)
    // If equal, return 0 (keep order the same)



// Sorting items using qsort
// Parameters: 
//  - items: Array of items
//  - n: Number of items
//  - sizeof(struct Item): Size of each item in bytes
//  - compare: Function used for sorting

}

// Function to solve the fractional knapsack problem
double fractionalKnapsack(int capacity, struct Item items[], int n) {
    // Sort items based on value/weight ratio
    qsort(items, n, sizeof(struct Item), compare);

    double totalValue = 0.0;
    for (int i = 0; i < n; i++) {
        if (capacity >= items[i].weight) {
            // Take the full item
            totalValue += items[i].value;
            capacity -= items[i].weight;
        } else {
            // Take the fractional part
            totalValue += items[i].ratio * capacity;
            break;
        }
    }
    return totalValue;
}

int main() {
    int n, capacity;
    printf("Enter the number of items: ");
    scanf("%d", &n);

    struct Item items[n];
    printf("Enter weight and value for each item:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &items[i].weight, &items[i].value);
        items[i].ratio = (double)items[i].value / items[i].weight;
    }

    printf("Enter knapsack capacity: ");
    scanf("%d", &capacity);

    double maxValue = fractionalKnapsack(capacity, items, n);
    printf("Maximum value in knapsack: %.2lf\n", maxValue);

    return 0;
}
