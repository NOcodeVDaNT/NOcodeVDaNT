#include<stdio.h>

#include<stdlib.h>
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Function to create a new node
Node* getNode(int x) {
    Node* p = (Node*)malloc(sizeof(Node));
    p->data = x;
    p->next = NULL;
    return p;
}

// Function to build a linked list with 3 nodes (1 -> 2 -> 3)


void display(Node* p) {
    while (p != NULL) {
        printf("%d\n", p->data);
        p = p->next;
    }
}

// Function to add a node at the end of the list
Node* addend(Node* s, int x) {
    Node* p = getNode(x);
    if (s == NULL) {
        return p; // If the list is empty, the new node is the start
    }
    Node* temp = s;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = p;
    return s; // Return the head of the list
}

Node* addbegin(Node *s, int x) {
    Node *p = getNode(x);
    p->next = s;
    return p;
}
void delend(Node *s){

    if (s==NULL)
    {
        printf("empty list");
        return;
    }

    if (s->next==NULL)
    {
        free(s);
        s=NULL;
        printf("now the list is empty");
        return;
    }
    
    

    Node *r,*temp=s;
    while(temp->next!=NULL){
        r=temp;
        temp=temp->next;
    }
    r->next=NULL;
    free(temp);
}
int count(Node *s){
    int count = 0;
    while (s != NULL) {
        count++;
        s = s->next;
        }
        return count;

}

void indertNodeAfterNode(Node* after,Node *start ,int x){
    Node *newnode = getNode(x);
    Node*temp=start;
    while(temp!=after){
        temp=temp->next;
        
    }
    Node*temp2=temp->next;
    temp->next=newnode;
    newnode->next=temp2;
    

    
}

Node* searchByNode(Node *s,int x){
    Node*temp=s;
    while(temp->data!=x && temp!=NULL){
        temp=temp->next;

    }
    if (temp==NULL)
    {
       printf("elemnt not found");
       return s;
    }
    
    return temp;
}


int main() {
    Node* start;

    start = addend(NULL,1);
    display(start);

    start = addbegin(start, 4);
    addend(start, 5);

    display(start);

    return 0;
}
