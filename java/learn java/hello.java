import java.util.*;// use to import scanner class


public class hello{
    public static void main(String[] args) {
        System.out.println("hello world");//ln use for next line || "\n" also use for next line same as c language
        System.out.print("hello world");// next print will be done in same line
        

        //VARIABLES
        String name = "vedant dahake";
        int age = 18;
        System.out.println(  age+"\n"+name);

        int a=18;
        int b=12;
        int sum=a+b;
        System.out.println(sum);

        //INPUT
        Scanner sc =new Scanner(System.in); // boiler plate for input  || system.in is used for input
        System.out.println("enter the authorized name");
        String nam = sc.next(); // next is use for input of only one word(1 token)

        
        System.out.println(nam); // printing inputed name


        System.out.println("enter full name");      
        String man = sc.nextLine(); //nextline is used to take a sentence as input or to take a word after previous inputed string word
        System.out.println(man);

        System.out.println("enter two number");
        int c=sc.nextInt();
        int d=sc.nextInt();
        System.out.println(c+d);

        //IF ELSE
        System.out.println("enter your age");
        int AGE=sc.nextInt();
        if (AGE<18) {
            System.out.println("not elgible for prnhub");
            
        }
        else if (AGE==18) {
            
            System.out.println("baad main batata hoon");
        }
        else{
            System.out.println("eligible");
        }


        //SWITCH STATEMENT
        System.out.println("enter button number 1,2,3");
        int button=sc.nextInt();

        switch (button) {
            case 1:System.out.println("namaste");
                
                break;
            case 2:System.out.println("hello");
                
                break;
            case 3:System.out.println("kya re bedu");
                
                break;
        
            default:System.out.println("dabaya gaya button abhi uplabh nahi hai");
                break;
        }


        //LOOPS

        //FOR LOOP
        for(int e=1;e<=3;e++){
          System.out.println(e+")i am GHOST");
        }


        //WHILE LOOP
        int e=0;
        while (e<5) {
            System.out.println("hello ghost dont kill me");
            e++;

            
        }

        //DO WHILE LOOP
        int f=0;
        do{
            System.out.println(f);
            f++;
        }while(f<5);

        //PRINTNG THE SUM OF FIRST G NUMBER
        int summation=0;
        System.out.println("enter the number");
        int g=sc.nextInt();
        for(int h=0;h<=g;h++){
            summation=summation+h;

        }
        System.out.println("THE SUM TILL given number  IS="+summation);

        // ALSO PRINT THE TABLE OF THAT NUMBER
        System.out.println("THE TABLE OF NUMBER "+g+"is\n");
        for(int h=0;h<=10;h++){
            System.out.println(g*h);
        }


        System.out.println("--------------------------------------------------------------------------------------------------------");




        //PATTERN PRINTING QUESTIONS

        //RECTANGLE PATTERN
        for(int h=0;h<4;h++){
            for(int i=0;i<4;i++){
                System.out.print("@");
            
            }
            System.out.print("\n");
        }


        System.out.println("--------------------------------------------------------------------------------------------------------");

        // HOLLOW RECTANGLE
        for(int h=0;h<4;h++){
            for(int i=0;i<4;i++){
                if (i==0||i==3||h==0||h==3) {
                    System.out.print("@");
                }
                else{
                    System.out.print(" ");
                }
                
            
            }
            System.out.print("\n");
        }

        System.out.println("--------------------------------------------------------------------------------------------------------");



        //RIGHT ANGLE TRAINGLE
        for(int i=1;i<=5;i++){
            for(int h=1;h<=i;h++){
                System.out.print("*");
            
            }
            System.out.println(" ");
        }


        System.out.println("--------------------------------------------------------------------------------------------------------");
     

        int j=5;
        for(int i=1;i<=j;i++){                                                                  //           ----*
                                                                                                //           ---**
            for(int h=1;h<=j-i;h++){                                                            //           --***
                System.err.print(" ");                                                        //           -****
            }                                                                                   //           *****
            for(int k=1;k<=i;k++){
                System.out.print("*");
            }
            System.out.println();

        }

        System.out.println("--------------------------------------------------------------------------------------------------------");

        
        int numb=1;

        for(int h=1;h<=j;h++){
            for(int i=1;i<=h;i++){
                System.out.print(numb);
                 numb++;

             }
             System.out.println();

        }


        System.out.println("--------------------------------------------------------------------------------------------------------");



        for(int h=1;h<=j;h++){
            for(int i=1;i<=h;i++){
                int summ=h+i;
            

                if (summ%2==0) {
                    System.out.print("1 ");
                    
                }
                else{
                    System.out.print("0 ");
                }
            }
            System.out.println();
        }


        System.out.println("--------------------------------------------------------------------------------------------------------");



        //buttterfly pattern

        for(int h=1;h<=j;h++){
           
                for(int i=1;i<=h;i++){

                System.out.print("*");
                }
                int space=2*(j-h);
                for(int k=1;k<=space;k++){
                    System.out.print(" ");
                }
                for(int l=1;l<=h;l++){
                    System.out.print("*");
                }

                System.out.println();
  
            
        }

        
        for(int h=j;h>=1;h--){
           
            for(int i=1;i<=h;i++){

            System.out.print("*");
            }
            int space=2*(j-h);
            for(int k=1;k<=space;k++){
                System.out.print(" ");
            }
            for(int l=1;l<=h;l++){
                System.out.print("*");
            }

            System.out.println();

        
    }


    System.out.println("--------------------------------------------------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------------------------------------------------");
    System.out.println("--------------------------------------------------------------------------------------------------------");

    //using a function


    System.out.println("enter your name :");
    String yourname=sc.next();
    printMyName(yourname);// calling a function


    System.out.println("ENTER TWO NUMBER");
    int k=sc.nextInt();
    int l=sc.nextInt();

    System.out.println("THE ADDITION OF GIVEN NUMBER IS  :  "+add(k, l));

    System.out.println("the factorial og given number are : "+factorial(k)+"and "+factorial(l));



    // ARRAYS

    int[] arrayname=new int[3];  //int arrayname[]=new int[];                       * this is also valid syntax *
    arrayname[0]=18;
    arrayname[1]=98;                   //int arrayname[]={18,98,25}
    arrayname[2]=25;
    System.out.println(arrayname[0]+"  "+arrayname[1]+"  "+arrayname[2]+"  ");


    for(int i=0;i<3;i++){
        System.out.println(arrayname[i]);
    }

    System.out.println("------------------------------------------------");
    System.out.println("------------------------------------------------");
    
    for (int i : arrayname) {
        System.out.println(i);
    }

    //INPUT ARRAY

    System.out.println("ENTER THE SIZE OF ARRAY");

    int size=sc.nextInt();
    int array[]=new int[size];

    for(int i=0;i<size;i++){

        array[i]=sc.nextInt();

    }

    System.out.println("PRINTING ARRAY..........");

    for(int i=0;i<size;i++){

        System.out.println(array[i]);
      
    }


    //2D ARRAY

   //int arr[][]=new int[2][3];         * 2x3 MATRIX *

    System.out.println("enter no of rows and column");
    int rows=sc.nextInt();
    int column=sc.nextInt();


    int arr[][]=new int[rows][column];

    for(int i=0;i<rows;i++){

        for (int m=0;m<column;m++){

            System.out.println("enter the element "+ i+" "+m+" : ");
            
            arr[i][m]=sc.nextInt();

        }
    }



    
    for(int i=0;i<rows;i++){

        for (int m=0;m<column;m++){

            System.out.println("enter the element  "+ i+" "+m+"  :  "+arr[i][m]);

        }
    }



    //STRINGS:-stringss.java



    //BIT OPERTAOR AND BIT MANUPULATION

    //GETTING A BIT AT PARTICULAR POSITION i :- position was calculated from right and right most is at zeroth index.

    int n=5;
    int pos=2;
    int bitmask=1<<pos;
    if ((bitmask & n)==0) {
        System.out.println("bit was zero");
        
    }
    else{
        System.out.println("bit was non zero");
    }



    //SETTING BIT OF NUMBER N:- SETTING BIT TO 1 AT PARTICULAR POSITION i.

    int newnumber= bitmask|n;
    System.out.println(newnumber);

    //CLEAR BIT AT PARTICULAR POSITION:- SETTING BIT TO 0 AT PARTICULAR POSITION i.

    int notbitmask=~(bitmask);
    int newnumb=notbitmask & n;
    System.out.println(newnumb);


    //UPDATE BIT AT ANY POSITION TO 0 OR 1.

    //CASE 1:- TO 1 => USE SET OPERATION
    //CASE 2:- TO 0 => USE CLEAR OPERATION

   


    //SORTING TECHNIQUE

    int arrays[]={7,8,3,1,2};

    //BUBBLE SORTING=>timecomplexity=O(n^2)

    for(int i=0;i<arrays.length-1;i++){
        for(int o=0;o<arrays.length-i-1;o++){
            if (arrays[o]>arrays[o+1]) {
                int temp=arrays[o];
                arrays[o]=arrays[o+1];
                arrays[o+1]=temp;

            }

        
        }

    }
    printarray(arrays);
   


    //SELECTION SORT => TIMECOMPLEXITY = o(n^2)
   


    for(int i=0;i<arrays.length-1;i++){
        int smallest=i;
    
        for(int o=i+1;o<arrays.length;o++){
            if (arrays[smallest]>arrays[o]) {
                 smallest=o;

                
            }
            


        
        }
        int temp=arrays[smallest];
        arrays[smallest]=arrays[i];
        arrays[i]=temp;

        
    }
    printarray(arrays);


    //INSERTION SORTING => TIME COMPLEXITY = o()

    for(int i=1;i<arrays.length;i++){
        int current= arrays[i];
        int o=i-1;

        while (o>=0 && current < arrays[o]) {
            arrays[o+1]=arrays[o];
            o--;

        }
        arrays[o+1]=current;

        
    }
    printarray(arrays);





    

























    



    
   

 






    








    


   
    

    



    
        


    }




    //FUNCTIONS:- always written outside main function

    public static int printMyName(String yourname){
        System.out.println(yourname);
        return 1;
    }

    public static int add(int a, int b){
        return a+b;

    }

    public static float factorial (int a){
        float fact=1;
        for(int i=1;i<=a;i++){
            fact*=i;

        }

        return fact;
    }

     //function to print sorted array
     public static void printarray(int arr[]){
        for(int i=0;i<=arr.length-1;i++){
            System.out.print(arr[i]+"  ");
        }
     }


}