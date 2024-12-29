//games of biggest player

#include<stdio.h>
#include<math.h>


 int main(){
    int n[5]={7,8,3,1,2};

    int length = sizeof(n) / sizeof(n[0]);

    for (int i = 0; i < length-1; i++)
    {
        for (int j = 0; j < length-i-1; j++)
        {
            if (n[j]>n[j+1])
            {    //swapping
                int temp=n[j];
                n[j]=n[j+1];
                n[j+1]=temp;

            }
            
        }
        
    }

    for (int k= 0; k < 5; k++)
    {
        printf("%d",n[k]);

    }
    
    
    
 }

 