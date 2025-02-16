//games of biggest player

#include<stdio.h>
#include<math.h>


 int main(){
    int n[5]={7,8,3,1,2};

    int length = sizeof(n) / sizeof(n[0]);
    int flag = 0; //to check if the array is already sorted or not

    for (int i = 0; i < length-1; i++)
    {
        for (int j = 0; j < length-i-1; j++)
        {
            if (n[j]>n[j+1])
            {    //swapping
                int temp=n[j];
                n[j]=n[j+1];
                n[j+1]=temp;
                flag=1; //if the array is not sorted

            }
            
        }
        if(flag==0){
            break;
        }
        
    }


    for (int k= 0; k < 5; k++)
    {
        printf("%d",n[k]);

    }
    
    
    
 }

 