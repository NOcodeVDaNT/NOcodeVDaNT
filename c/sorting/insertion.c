#include<stdio.h>
int main(){
    int n[5]={7,8,3,1,2};

    int length = sizeof(n) / sizeof(n[0]);
    

    for (int i = 1; i < length; i++)
    {
        int current=n[i];
        int j=i-1;
        while (j>=0 && n[j]>current){
            n[j+1]=n[j];
            j--;

        }
        n[j+1]=current;
    }
     for (int k= 0; k < 5; k++)
    {
        printf("%d",n[k]);

    }
    
}

