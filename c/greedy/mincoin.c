#include <stdio.h>

void minCoins(int coins[], int n, int amount) {
    printf("Coins used: ");
    for (int i = 0; i < n; i++) {
        while (amount >= coins[i]) {
            amount -= coins[i];
            printf("%d ", coins[i]);
        }
    }
    printf("\n");
}

int main() {
    int coins[] = {1000, 500, 100, 50, 20, 10, 5, 2, 1};
    int n = sizeof(coins) / sizeof(coins[0]);
    int amount = 93;

    minCoins(coins, n, amount);
    return 0;
}

