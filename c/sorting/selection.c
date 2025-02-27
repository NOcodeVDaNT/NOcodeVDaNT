
//game of smallest index

#include<stdio.h>

int main(){
    int n[5]={7,8,3,1,2};
    int length = sizeof(n) / sizeof(n[0]);

    for (int i = 0; i < length; i++)
    {
        int smallest= i;
        for (int j = i+1; j <length ; j++)
        {
            if (n[smallest]>n[j])
            {
                smallest=j;
                

            }
            
        }
        int temp = n[i];
        n[i] = n[smallest];
        n[smallest] = temp;


        
    }

     for (int k= 0; k < 5; k++)
    {
        printf("%d",n[k]);

    }
    

    }