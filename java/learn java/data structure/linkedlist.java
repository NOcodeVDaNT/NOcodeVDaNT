import java.util.LinkedList;
import java.util.Collections;

public class linkedlist {
    Node head; //initiated by null
    //create a node
    class Node{
        Node next;
        String data;

        Node(String data){
            this.data=data;
            this.next=null;

        }

    }
    //add begin
    public void addbegin(String data){
        Node newnode=new Node(data);
        if(head==null){
            head=newnode;
            return;
        }
        newnode.next=head;
        head=newnode;

    }

    //add end
    public void addend(String data){
        Node newnode=new Node(data);
        if (head==null) {
            head=newnode;
            return;
        }
        Node curNode = head;
        while (curNode.next!=null) {
            curNode=curNode.next;
        }
        curNode.next=newnode;
        
    }

    //delete begin
    public void delbegin(){
        if (head==null) {
            System.out.println("nothing to delete");
            return;
        }
        head=head.next;
    }

    //printing the list
    public void print(){
        if (head==null) {
            System.out.println("list is empty");
            return;
        }
        Node curNode=head;
        while (curNode!=null) {
            System.out.print(curNode.data+"->");
            curNode=curNode.next;
        }
        System.out.println("NULL");
    }


    //reverse the list
    public Node reverse(Node head){

        if (head==null||head.next==null)  {
            return head;
            
        }

        Node prevNode=head;
        Node curNode=head.next;
        while (curNode!=null) {
            Node nextNode=curNode.next;
            curNode.next=prevNode;
            //updating
            prevNode=curNode;
            curNode=nextNode;
            
        }
        head.next=null;
        head=prevNode;
        return head;
    }

    //size of list
    public int size(Node head){
        int size=0;
        Node currNode=head;
        while(currNode!=null){
            size++;
            currNode=currNode.next;
        }
        return size;

    }


    public Node RemoveNthNodeFromEnd(Node head,int n) {


        
        if (head == null || head.next==null)
            return null;

        int size= size(head);
        int NodeFromEnd=size-n+1;

        Node currNode=head;
        int i=1;

        if(n==size)
        return head.next;
        



        while( i<NodeFromEnd){
            currNode=currNode.next;
            i++;

        }
        currNode.next=currNode.next.next;

        return head;






    }

    //middle elemnt in list

    public Node middleNode(Node head){
        Node hare=head;
        Node turtle=head;

        while(hare.next.next!=null ||hare.next!=null){
            turtle=turtle.next;
            hare=hare.next.next;

        }
        return turtle;

    }


    //is linkedlist a palindrome
    public boolean ispalindrome(Node head){
        if(head==null ||head.next==null){
            return true;

        }
        Node middle=middleNode(head);
        Node SecondHalfStart = reverse(middle.next);
        Node FirstHalfStart =head;

        while(SecondHalfStart!=null){
            if(FirstHalfStart != SecondHalfStart){
                return false;

            }
            FirstHalfStart=FirstHalfStart.next;
            SecondHalfStart=SecondHalfStart.next;


        }
        return true;


    }





    public static void main(String[] args) {
        linkedlist list=new linkedlist();
        list.addbegin("a");
        list.addbegin("is");
        list.addend("op");
        list.print();
        list.delbegin();
        list.print();

        
    }
}
