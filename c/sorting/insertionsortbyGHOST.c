#include<stdio.h>
int main(){
    int n[5]={7,8,3,1,2};

    int length = sizeof(n) / sizeof(n[0]);
    

    for (int i = 1; i < length; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (n[i]<n[j]){
                int temp = n[i];
                n[i]=n[j];
                n[j]=temp;

            }
        }
        
    }
     for (int k= 0; k < 5; k++)
    {
        printf("%d",n[k]);

    }
    
}

