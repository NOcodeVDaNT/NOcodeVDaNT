import java.util.*;
public class tree {
    //construct binary tree using array and retrun the root value
    static class node{
        int data;
        node left;
        node right;

        node(int data){
            this.data=data;
            this.left = null;
           this.right = null;

        }
    }
    static class Btree{
        static int ind=-1;
        public static node btree(int[] Node){
            ind++;
            if(Node[ind]==-1){
                return null;
        }
        node newnode=new node(Node[ind]);
        newnode.left=btree(Node);
        newnode.right=btree(Node);
        return newnode;


    }
}


//traversing in preorder
public static void preorder(node root) {
    if(root == null) {
        System.out.print(-1+" ");
        return;
    }
    System.out.print(root.data+" ");
    preorder(root.left);
    preorder(root.right);
}
//inorder
public static void inorder(node root) {
    if(root == null) {
        System.out.print(-1+" ");
        return;
    }
    inorder(root.left);
    System.out.print(root.data+" ");
    inorder(root.right);
}
//postorder

public static void postorder(node root) {
    if(root == null) {
        System.out.print(-1+" ");
        return;
    }
    postorder(root.left);
    postorder(root.right);
    System.out.print(root.data+" ");
}



//level order traversing == DFS algoritham
public static void levelOrder(node root) {
    if(root == null) {
        return;
    }
    Queue<node> q = new LinkedList<>();
    q.add(root);
    q.add(null);
    while(!q.isEmpty()) {
        node curr = q.remove();
        if(curr == null) {
            System.out.println();
            //queue empty
            if(q.isEmpty()) {
                break;
            } else {
                q.add(null);
            }
        } else {
            System.out.print(curr.data+" ");
            if(curr.left != null) {
                q.add(curr.left);
            }
            if(curr.right != null) {
                q.add(curr.right);
            }
        }
    }
}


//hiegth of tree
public static int height(node root) {
    if(root == null) {
        return 0;
    }


    int leftHeight = height(root.left);
    int rightHeight = height(root.right);
    return Math.max(leftHeight, rightHeight) + 1;
}


//number of node

public static int countOfNodes(node root) {
    if(root == null) {
        return 0;
    }

    return countOfNodes(root.left)+countOfNodes(root.right)+1;
    
}

//sum of nodes
public static int sumOfNodes(node root) {
    if(root == null) {
        return 0;
    }


    int leftSum = sumOfNodes(root.left);
    int rightSum = sumOfNodes(root.right);
    return leftSum + rightSum + root.data;
}

public static int diameter(node root) {
    if(root == null) {
        return 0;
    }


    int diam1 = height(root.left) + height(root.right) + 1;
    int diam2 = diameter(root.left);
    int diam3 = diameter(root.right);


    return Math.max(diam1, Math.max(diam2, diam3));
}






    public static void main(String[] args) {

        //create  tree
        int nodes[] = {1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1};
        Btree tree = new Btree();
        node root = tree.btree(nodes);
        System.out.println(root.data);

        //traversing
        preorder(root);
        System.out.println();
        System.out.print("postoder:::");
        postorder(root);
        System.out.println();
        System.out.print("inorder:::");
        inorder(root);






    }
}
