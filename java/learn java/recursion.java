import java.util.*;
public class recursion {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //printing number n to 1
        System.out.println("enter the numbers");

        int n=sc.nextInt();
        
        printnum(n);

        System.out.println();

        printnumb(1, n);

        System.out.println();

        sum(1, n, 0);

        System.out.println();

        System.out.println(factorial(n));


        //fibonacci
        System.out.print("0");
        System.out.print("1");
        fibonacci(0, 1, n-2);

        System.out.println();
        System.out.println(power(n, n));


        //TOWER OF HANOI
        hanoi(n, "S", "H", "D");


        System.out.println();

        
        //reverse the string
        String s="vedantdahake";
        int i=s.length()-1;
        reverse(s, i);

        System.out.println();

        //occurences of elemnt
        String str="abaacdaefaah";
        occurences(str, 'a', 0);  //character elemtn passes between ' '


        //sorted array
        int array[]={1,2,3,7,5,6};
        sorted(array, 0);



        System.out.println();


        //shift all x at end of the string
        String stri="axbcxxd";
        shift(stri, 0, 0, "");


        System.out.println();


        //remove repeat characters in word
        String string="vveeddaanntt";
        repeat(string, "", 0);


        System.out.println();


        //all subsequences of a string

        String strin="abc";
        subsequences(strin, 0, "");

        System.out.println();


        //keypad combination
        String sstring="23";
        printcomb(sstring, 0, "");

        System.out.println("--------------------------------------------------------------------------------------------------------------------");
        System.out.println("                                               BASIC-OVER                                                           ");
        System.out.println("--------------------------------------------------------------------------------------------------------------------");


        System.out.println();

        //combination of word
        String p="abc";
        combination(p, "");

        System.out.println();


        //count total path to move in maze from point 0,0 to n,m
        int r=3,q=3;
        System.out.println(path(r,q, 0, 0));
        

        //place a tile of size 1xM in a floor of size NxM
        int t=4,u=2;
        System.out.println("required"+place(t, u));


         //total number of ways in which you can invite N people to your party single or in pair
         System.out.println(party(2));

         //merge sort
         int newarray[]={5,6,7,3,1,2};
         int w=newarray.length;
         divide(newarray, 0, w-1);
         for(int v=0;v<w;v++){
            System.out.println(newarray[v]+" ");

         }

        System.out.println("---------------------------------------------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------------------------------------------");
        System.out.println("---------------------------------------------------------------------------------------------------------------");


        //quick sort
        quicksort(newarray, 0, w-1);
        for(int v=0;v<w;v++){
            System.out.println(newarray[v]+" ");

         }

       


       






       





















        
    }

    //FUNCTIONS 


    //printing number n to 1
    public static void printnum (int n){
        if (n>0) {
            System.out.print(n);
            printnum(n-1);          
        }
       return;
    }


    //printing number 1 to m
    public static void printnumb(int n,int m){
        if(n==0||n==m){
            System.out.println(m);
            return;

        }
        System.out.print(n);
        printnumb(n+1, m);


    }
    //sum of n natural number
    public static void sum(int n,int m,int summ){
        if (n==m) {
            summ+=n;
            System.out.println(summ);
            return;       
        }
     summ+=n;
     sum(n+1, m, summ);
     return;

    }

    //factorial
    public static int factorial(int n){
        if (n==0||n==1) {
            return 1;
        }
     int f= factorial(n-1);
     int c=n*f;
     return c;

    }



    //fibonacci series
    public static void fibonacci(int a,int b,int n){
        if(n==0){
            return;
        }
        int c=a+b;
        System.out.print(c);;
        fibonacci(b, c, n-1);     
    }


    //x^n
    public static int power(int x,int n){
        if (n==0) {
            return 1;
        }
        if (x==0) {
            return 0;
        }
        //if n is even
        if(n%2==0){
            return power(x, n/2)*power(x, n/2);
        }
        else{
            return power(x, n/2)*power(x, n/2)*x;
        }
    }



    //TOWER OF HANOI => timecompolexity is O(n^2)
    public static void hanoi(int n,String src,String helper,String dest){
        if (n==1) {
            System.out.println("transfered disk "+n+" from "+src+" to "+dest);
            return;
            
        }
        hanoi(n-1, src, dest, helper);
        System.out.println("transfered disk " +n+ " from "+src+" to "+dest);
        hanoi(n-1, helper, src, dest);

    }


    //REVERSE A STRING => timecomplexity is 0(s.lenght)
    public static void reverse(String s,int i){
        if (i==0) {
            System.out.print(s.charAt(0));
            return;
        }
        System.out.print(s.charAt(i));
        reverse(s, i-1); 
        
    }


    //first and last occurence of an elemnt in string

    public static int first=-1; //static variables
    public static int last=-1;  //static variables

    public static void occurences(String str,char element,int indx){
        if (indx==str.length()) {
            System.out.println(first);
            System.out.println(last);
            return;
            
        }
        char cuurentcharacter=str.charAt(indx);
        if(cuurentcharacter == element){
            if (first==-1) {
                first=indx;
            }
            else{
                last=indx;
            }
        }
        occurences(str, element, indx+1);
    }


    //checking sorted array(strickly increasing )
    public static void sorted(int a[],int indx){
        if (indx==a.length-1) {
            System.out.println("sorted");
            return;
            
        }
        if (a[indx]>a[indx+1]) {
            System.out.println("not sorted");
            return;
            
            
        }
        sorted(a, indx+1);
        
    }

    //shift all x at end of the string
    public static void shift(String s,int indx,int count,String newString){
        if (indx==s.length()) {
            for(int n=0;n<count;n++){
                newString+='x';
            }
            System.out.print(newString);
            return;

        }
        if(s.charAt(indx)=='x'){
            count++;
            shift(s, indx+1, count, newString);
        }
        else{
            newString+=s.charAt(indx);
            shift(s, indx+1, count, newString);
        }

    }


    //remove repeat characters in word
    public static boolean[] map=new boolean[26];

    public static void repeat(String str, String newstr, int indx){
        if (indx==str.length()) {
            System.out.println(newstr);
            return;

        }
        char currchar=str.charAt(indx);
        if (map[currchar-'a']==true) {
            repeat(str, newstr, indx+1);
        }
        else{
            newstr+=currchar;
            map[currchar-'a']=true;
            repeat(str, newstr, indx+1);
        }

    }



    //all subsequences of a string
    public static void subsequences(String str,int indx,String newsString){

        if (indx==str.length()) {
            System.out.println(newsString);
            return;
        }
        char currchar=str.charAt(indx);
        //to be part
        subsequences(str, indx+1, newsString+currchar);

        //not to be part of string
        subsequences(str, indx+1, newsString);
     }


    //keypad combination
    public static String[] keypad ={".","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"};

    public static void printcomb(String str,int indx, String combination){

        if (indx==str.length()) {
            System.out.println(combination);
            return;
        }
        char currchar=str.charAt(indx);
        String mapping=keypad[currchar-'0'];
        for(int i=0;i<mapping.length();i++){
            printcomb(str, indx+1, combination+mapping.charAt(i));
        }
     }


    // combination of word  => timecomplexity = O(n!)
    public static void combination(String s,String comb){
        if (s.length()==0) {
            System.out.println(comb);
            return;
        }
        for(int i=0;i<s.length();i++){
            char currchar=s.charAt(i);
            String newString=s.substring(0, i)+s.substring(i+1);
            combination(newString, comb+currchar);
        }
     }


     //count total path to move in maze from point 0,0 to n,m
     public static int path (int n,int m,int i,int j)

     { 
        if (i==n||j==m) {
            return 0;
        }
        if (i==n-1 && j==m-1) {
        return 1;
        
        }
        int downpath=path(n, m, i+1, j);
        int rightpath=path(n, m, i, j+1);
        return downpath+rightpath;


     }




    //place a tile of size 1xM in a floor of size NxM
    public static int place(int n, int m){

        if (n<m) {
            return 1;
        }
        if (n==m) {
            return 2;
        }
        int vertical=place(n-m, m);
        int horizontal=place(n-1, m);
        return vertical+horizontal;


    }


    //total number of ways in which you can invite N people to your party single or in pair
    public static int party(int n){
        if (n==2) {
            return 2;
        }
        if(n<=1){
            return 1;
        }
        int single=party(n-1);
        int pair=(n-1)*party(n-2);
        return single+pair;
    }

    //merge sorting => timecomllexity is O(nlogn)

    public static void conquer(int array[],int si,int mid,int ei){
        int merged[]=new int[ei-si+1];
        int indx1=si;
        int indx2=mid+1;
        int x=0;
        while(indx1<=mid && indx2<=ei) {
            if (array[indx1]<array[indx2]) {
                merged[x++]=array[indx1++];
            }
            else{
                merged[x++]=array[indx2++];
            }
            
        }
        while (indx1<=mid) {
            merged[x++]=array[indx1++];
            
        }
        while (indx2<=ei) {

              merged[x++]=array[indx2++];
        }
        for(int i=0,j=si;i<merged.length;i++,j++){
            array[j]=merged[i];
        }
    }
    public static void divide (int array[],int si,int ei){
        if (si>=ei) {
            return;
            
        }
        int mid=si+(ei-si)/2;
        divide(array, si, mid);
        divide(array,mid+1, ei);
        conquer( array, si, mid, ei);
    }

    //quick sort
    public static int getindex(int array[],int low,int high){
        int pivot=array[high];
        int i= low-1;
        for(int j=low;j<high;j++){
            if (array[j]<pivot) {
                i++;
                //swap
                int temp=array[i];
                array[i]=array[j];
                array[j]=temp;

            }

        }
        i++;
        int temp= array[i];
        array[i]=pivot;
        array[high]=temp;
        return i;

    }
    public static void  quicksort(int array[],int low,int high){
        if (low<high) {
            int pivotindex=getindex(array,low,high);

            quicksort(array, low, pivotindex-1);
            quicksort(array, pivotindex+1, high);
        }
         
    }










     }









    

