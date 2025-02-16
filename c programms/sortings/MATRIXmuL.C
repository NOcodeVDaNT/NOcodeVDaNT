#include <stdio.h>
#include <stdlib.h>

#define MAX 10  // Maximum matrix size

// Function to add two matrices
void addMatrix(int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}

// Function to multiply matrices using divide and conquer
void multiplyMatrix(int A[MAX][MAX], int B[MAX][MAX], int C[MAX][MAX], int size) {
    if (size == 1) {
        C[0][0] = A[0][0] * B[0][0];
        return;
    }

    int newSize = size / 2;
    int A11[MAX][MAX], A12[MAX][MAX], A21[MAX][MAX], A22[MAX][MAX];
    int B11[MAX][MAX], B12[MAX][MAX], B21[MAX][MAX], B22[MAX][MAX];
    int C11[MAX][MAX], C12[MAX][MAX], C21[MAX][MAX], C22[MAX][MAX];
    int P1[MAX][MAX], P2[MAX][MAX], P3[MAX][MAX], P4[MAX][MAX], P5[MAX][MAX], P6[MAX][MAX], P7[MAX][MAX];

    // Initialize submatrices
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + newSize];
            A21[i][j] = A[i + newSize][j];
            A22[i][j] = A[i + newSize][j + newSize];

            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + newSize];
            B21[i][j] = B[i + newSize][j];
            B22[i][j] = B[i + newSize][j + newSize];
        }
    }

    // Recursive multiplications
    multiplyMatrix(A11, B11, P1, newSize);
    multiplyMatrix(A12, B21, P2, newSize);
    multiplyMatrix(A11, B12, P3, newSize);
    multiplyMatrix(A12, B22, P4, newSize);
    multiplyMatrix(A21, B11, P5, newSize);
    multiplyMatrix(A22, B21, P6, newSize);
    multiplyMatrix(A21, B12, P7, newSize);
    multiplyMatrix(A22, B22, C22, newSize);

    // Compute final submatrices
    addMatrix(P1, P2, C11, newSize);
    addMatrix(P3, P4, C12, newSize);
    addMatrix(P5, P6, C21, newSize);
    addMatrix(P7, C22, C22, newSize); // C22 = P7 + C22

    // Merge submatrices into result matrix
    for (int i = 0; i < newSize; i++) {
        for (int j = 0; j < newSize; j++) {
            C[i][j] = C11[i][j];
            C[i][j + newSize] = C12[i][j];
            C[i + newSize][j] = C21[i][j];
            C[i + newSize][j + newSize] = C22[i][j];
        }
    }
}

// Function to take matrix input
void inputMatrix(int matrix[MAX][MAX], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}

// Function to display matrix
void printMatrix(int matrix[MAX][MAX], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX] = {0};
    int size;

    printf("Enter the size of square matrices (must be power of 2): ");
    scanf("%d", &size);

    printf("Enter elements of first matrix:\n");
    inputMatrix(A, size);

    printf("Enter elements of second matrix:\n");
    inputMatrix(B, size);
    
    multiplyMatrix(A, B, C, size);

    printf("Product of the matrices:\n");
    printMatrix(C, size);

    return 0;

    

   
}