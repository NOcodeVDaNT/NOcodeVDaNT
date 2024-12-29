
import java.util.*;


public class graph {
    static class edge{
        int src;
        int dest;
        int weight;
        //contructor
        public edge(int a,int b,int c)
        {
            this.src=a;
            this.dest=b;
            this.weight=c;
        }
    }
    static  int vertice=4;

    //create grph using adjecncy list
    public static void creategraph(ArrayList<edge> graph[]){


        //here now each index of array of  arraylist is null and we cannot store any value on it first we have to make it empty arraylist on each index of array of arraylist

        // in java  when you create an array of objects, the array itself is allocated memory, but the objects that the array is meant to hold are not automatically created. By default:
        //Arrays of primitive types (e.g., int[], double[]) are initialized with default values for those types (0, 0.0, false, etc.).
        //Arrays of reference types (e.g., String[], ArrayList[], or edge[]) are initialized with null because they hold references, not actual objects.


        for(int i=0;i<vertice;i++){
            //vreate empty arraylist on each index of array of arraylist
            graph[i]=new ArrayList<edge>();

        }
        //adding edges
        graph[0].add(new edge(0,2,2));
        
        graph[1].add(new edge(1,2,10));
        graph[1].add(new edge(1,3,0));

        graph[2].add(new edge(2,0,2));
        graph[2].add(new edge(2,1,10));
        graph[2].add(new edge(2,3,-1));

        graph[3].add(new edge(3,1,0));
        graph[3].add(new edge(3,2,-1));



    }

    public static void printingraph(ArrayList<edge> graph[]){
        //printing graph
        for(int i=0;i<vertice;i++){
            System.out.println("Adjacency list of vertex "+i);
            System.out.print("Vertex "+i+" is connected to: ");
            for(int j=0;j<graph[i].size();j++){
                System.out.println();
                System.out.print("connected to:"+graph[i].get(j).dest +"  weight:"+graph[i].get(j).weight);
                System.out.println();
                }
                System.out.println();
                System.out.println();
                }
    }


    public static void bfs(ArrayList<edge> graph[], int V) {
        boolean visited[] = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        q.add(0); //Source = 0
        while(!q.isEmpty()) {
        int curr = q.remove();
        if(!visited[curr]) {
        System.out.print(curr+" ");
        visited[curr] = true;
        for(int i=0; i<graph[curr].size(); i++) {
        edge e = graph[curr].get(i);
        q.add(e.dest);
        }
        }
        }
        System.out.println();
        }

    public static void main(String[] args) {
     


        ArrayList<edge> graph[]=new ArrayList[vertice];//it means you are creating an array of size vertices of ArrayLists that contain edge type data
        creategraph(graph);
        printingraph(graph);

       
        



    }

}

