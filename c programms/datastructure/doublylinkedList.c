#include<stdio.h>
#include<string.h>
#include<stdlib.h>


typedef struct node{
    int data;
    struct node *next;
    struct node *prev;
}Node;


Node* getNode(int x) {
    Node* p = (Node*)malloc(sizeof(Node));
    p->data = x;
    p->next = NULL;
    p->prev = NULL;

    return p;
}

Node* insertend (Node* head, int x) {
    Node* p = getNode(x);
    Node *temp=head;
    if (head==NULL){
        head = p;
        return p;
    }
    {
          while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = p;
    p->prev=temp;
    return head;

    }

}
 Node* indertAfterNode(Node *head,Node* p,int x){
    Node* t = getNode(x);
    Node *temp=head;
    if (p == NULL) {
        printf("list is empty no such node found");
        return head;
 }
 while(temp!=p){
    temp=temp->next;
 }
 Node* temp2=p->next;
 temp->next=t;
 t->prev=temp;
 t->next=temp2;

 return head;

 }



 Node* deleteNode(Node* head, Node* p) {
 Node*temp=head;
 if (p==NULL) {
    printf("list is empty no such node found");

 }
 while (temp != p) {
    temp = temp->next;

 }
 temp->prev->next = temp->next;
 return head;

}


int main(){






}