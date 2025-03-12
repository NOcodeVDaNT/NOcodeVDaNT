#include <stdio.h>
#include <stdlib.h>

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
    int n;
    print("nummber of coin");
    scanf("%d",&n);

    int coins[n];
    for (int i = 0; i < n; i++) {
        scanf("%d",&coins[i]);
    }
    
    n = sizeof(coins) / sizeof(coins[0]);
    int amount = 93;

    minCoins(coins, n, amount);
    return 0;
}

