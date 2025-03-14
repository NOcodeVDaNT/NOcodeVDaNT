#include<stdio.h>
#define size 10
int stack[size];
int top=-1;

void push(char value) {
    if (top==size-1) {
        printf("Stack Overflow! Cannot push %d\n", value);
        return ;
    } else {
        top++;
        stack[top] = value;
        return;
    }
}
char pop(){
    if (top==-1)

    {
        printf("stack is empty");
        return -1;
    }
    char value = stack[top];
    top--;
    return value;
}
int main(){

    char a[5]="5+6*7";
    

}
