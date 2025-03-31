#include <stdio.h>
#include <stdbool.h>

#define N 8 // Change this value to solve for different board sizes

void printSolution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%c ", board[i][j] ? 'Q' : '.');
        }
        printf("\n");
    }
    printf("\n");
}

bool isSafe(int board[N][N], int row, int col) {
    // Check horizontal (left side only)
    for (int i = 0; i < col; i++) {
        if (board[row][i])
            return false;
    }
    
    // Check vertical (above only)
    for (int i = 0; i < row; i++) {
        if (board[i][col])
            return false;
    }
    
    // Check upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j])
            return false;
    }
    
    // Check upper right diagonal
    for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
        if (board[i][j])
            return false;
    }
    
    return true;
}

bool solveNQUtil(int board[N][N], int row) {
    if (row >= N) {
        printSolution(board);
        return true;
    }

    for (int i = 0; i < N; i++) {
        if (isSafe(board, row, i)) {
            board[row][i] = 1;
            if (solveNQUtil(board, row + 1))
                return true;
            board[row][i] = 0;
        }
    }
    return false;
}

void solveNQ() {
    int board[N][N] = {0};
    if (!solveNQUtil(board, 0))
        printf("No solution exists\n");
}

int main() {
    solveNQ();
    return 0;
}
