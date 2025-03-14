#include<stdio.h>

int fibonaci(int n){
    if(n==0)
    return 0;

    else if(n==1)
    return 1;

    else
    return fibonaci(n-1)+fibonaci(n-2);


    
}

void func(int n){
    int a=0,b=1,next;
    for(int i=0;i<n;i++){
        print("%d",a);
        next=a+b;
        a=b;
        b=next;
        
    
    


}
}

int main(){
    int n=10;
    for(int i=0;i<n;i++){
        printf("%d ",fibonaci(i));

    }
}