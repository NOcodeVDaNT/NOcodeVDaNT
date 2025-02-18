#ifndef VEDXLIST_H
#define VEDXLIST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* getNode(int x);
Node* build123();
void display(Node* p);
Node* addend(Node* s, int x);
Node* addbegin(Node *s, int x);

#endif
