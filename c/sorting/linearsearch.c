#include<stdio.h>

int Linearsearch(int arr[],int size,int key){
    int i;
    for(i=0;i<size;i++){
        if(arr[i]==key)
        return i;
        }
        return -1;

}
int main(){
    int a[5]={
        1,2,3,4,5
    };
    printf("%d",Linearsearch(a,5,4));  //3 

}