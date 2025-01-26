#include<stdio.h>
#include<stdlib.h>

int main(){
    int n;
    printf("entter noumber of processesssssss: ");
    scanf("%d", &n);

    int bt[n], wt[n], tat[n],ct[n];

    printf("Enter the burst times for each process:\n");

    for(int i = 0; i < n; i++){
        printf("P[%d]: ", i);
        scanf("%d", &bt[i]);
    }
    printf("enter arrival time for each process:\n");
    int at[n];
    for(int i = 0; i < n; i++){
        printf("P[%d]: ", i);
        scanf("%d", &at[i]);
    }

    if(at[0]!=0){
        printf("Invalid input");
        exit(0);
    }

    wt[0]=0;
    tat[0]=bt[0];
    ct[0]=at[0]+bt[0]-1;

    for(int i=1;i<n;i++){
        wt[i]=ct[i-1]-at[i];
        ct[i]=ct[i-1]+bt[i];
        tat[i]=ct[i]-at[i];

        
    }

    printf("Process\tarrival time\tBurst Time\tWaiting Time\tTurnaround Time\tCompletion Time\n");
    for(int i = 0; i < n; i++){
        printf("P[%d]\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n", i,at[i], bt[i], wt[i], tat[i],ct[i]);
    }

    for(int i=0;i<n;i++){
        if (at[i+1]>ct[i])
        {
            printf("idle time between process %d and %d is %d\n",i,i+1,at[i+1]-ct[i]);
        }
        


    }

    
}