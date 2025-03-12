#include<stdio.h>

void conquere(int a[],int si,int mid,int ei);


void divide(int a[],int si,int ei){
    if (si>=ei)
    {
        return;
    }
    int mid=(si+ei)/2;
    divide(a,si,mid);
    divide(a,mid+1,ei);
    conquere(a,si,mid,ei);
    
}

//principle of merging
void conquere(int a[],int si,int mid,int ei){
    int merged[ei-si+1];
    int indx1=si;
    int indx2=mid+1;
    int x=0;

    while(indx1<=mid && indx2<=ei){
        if (a[indx1]<=a[indx2]){
            merged[x]=a[indx1];
            indx1++;
            x++;

    }
    else{
        merged[x]=a[indx2];
        indx2++;
        x++;

    }
    }


    while(indx1<=mid){
        merged[x]=a[indx1];
        indx1++;
        x++;
    }
    
    while(indx2<=ei){
        merged[x]=a[indx2];
        indx2++;
        x++;
    }
    for(int i=si,j=0;i<=ei;i++,j++){
        a[i]=merged[j];


}


}
int main(){

    int arr[]={3,5,2,1,7,0};
    int n=sizeof(arr)/sizeof(arr[0]);
    divide(arr,0,n);
    for (int i=0;i<n;i++){
        printf("%d  ",arr[i]);
    }



}