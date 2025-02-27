#include<stdio.h>
int partition(int a[],int low,int high);



void quick(int a[],int low,int high){
    if(low<high){
        int pivotindex=partition(a,low,high);
        quick(a,low,pivotindex-1);
        quick(a,pivotindex+1,high);

    }
}

int partition(int a[],int low,int high){
    int pivot=a[high];
    int i=low-1;
    for(int j=low;j<high;j++){
        if (a[j]<pivot)
        {
            i++;
            int temp = a[i]; 
            a[i] = a[j];
            a[j] = temp;
        }
        
    }

    i++;
    int temp = a[i];
    a[i] = a[high];
    a[high] = temp;
    return i;
}

int main(){

    int arr[]={3,5,2,1,7,0};
    int n=sizeof(arr)/sizeof(arr[0]);
    quick(arr,0,n);
    for (int i=0;i<n;i++){
        printf("%d  ",arr[i]);
    }
    

}