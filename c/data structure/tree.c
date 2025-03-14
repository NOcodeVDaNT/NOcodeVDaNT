#include<stdio.h>
#include <stdbool.h>
typedef struct tree
{
    int data;
    struct tree *left, *right;

}tree;



void inorder(tree *root) {
    if (root == NULL) {  
        return;
    }
    inorder(root->left);           
    printf("%d ", root->data);    
    inorder(root->right);         
}



void postorder(tree *root) {
    if (root == NULL) {  
        return;
    }
    postorder(root->left);          
     
   postorder(root->right);  
    printf("%d ", root->data);           
}


void pre(tree *root) {
    if (root == NULL) {  
        return;
    }
    printf("%d ", root->data);  
    pre(root->left);          
     
    pre(root->right);  
             
}


tree* insertBST(tree *root, int key)
{

if (root == NULL) { 
tree* t = (tree*) malloc(sizeof(tree));
t->data = key;
t->left = t->right =NULL;
return(t) ;
}

if (key < root->data)
root->left = insertBST(root->left, key);

else
root->right = insertBST(root->right, key);

return ;
}


bool searchBST(tree *root, int key){
    if (root == NULL) {
        return 0;
    }
    if (root->data == key) {
            return 1;
    }
    if (root->data>key){
        searchBST(root->left,key);
    }
    if(root->data<key){
        searchBST(root->right,key);
    }

    
        
}

//DELETE FROM BST 

tree* findMin(tree* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

tree* deleteBST(tree* root, int key) {
    if (root == NULL) {
        return root; // Node not found
    }

    // Traverse the tree to find the node to delete
    if (key < root->data) {
        root->left = deleteBST(root->left, key);
    } else if (key > root->data) {
        root->right = deleteBST(root->right, key);
    } else {
        // Node found
        // Case 1: No child
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        // Case 2: One child
        else if (root->left == NULL) {
            tree* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            tree* temp = root->left;
            free(root);
            return temp;
        }
        // Case 3: Two children
        else {
            tree* temp = findMin(root->right);
            root->data = temp->data; // Copy inorder successor's value
            root->right = deleteBST(root->right, temp->data); // Delete successor
        }
    }
    return root;
}



int main(){

}