class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return root
        else:
            if data < root.val:  # Go to the left subtree if data is smaller
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insert(root.left, data)
            elif data > root.val:  # Go to the right subtree if data is larger
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insert(root.right, data)
        return root

    def preorder(self, root):
        if root is not None:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def bfs(self,root,l):
        l1=[]
        if root is None:
            return l
        l1.append(root)
        while len(l1):
            cur=l1[0]
            print(cur.val,end=" ")
            if cur.left:
                l1.append(cur.left)
            if cur.right:
                l1.append(cur.right)
            l1.pop(0)
    
    
    def minnode(self,root):
        
        if root is None:
            return 
        while root.left is not None:
            root=root.left
        print(root.val)
        
    
    def maxnode(self,root):
        
        if root is None:
            return 
        while root.right is not None:
            root=root.right
        print(root.val)
        
    def leafnodes(self,root):
        l1=[]
        ans=[]
        if root is None:
            return 1
        l1.append(root)
        c=0
        while len(l1):
            cur=l1[0]
            if cur.left:
               l1.append(cur.left)
                
            if cur.right:
               l1.append(cur.right)
            
            if cur.left is None and cur.right is None:
                ans.append(cur.val)
                c+=1
            l1.pop(0)
        return c,ans
    
    def nonleafnodes(self,root):
        l1=[]
        ans=[]
        if root is None:
            return 1
        l1.append(root)
        c=0
        while len(l1):
            cur=l1[0]
            if cur.left:
               l1.append(cur.left)
                
            if cur.right:
               l1.append(cur.right)
            
            if cur.left is not None or cur.right is not None:
                ans.append(cur.val)
                c+=1
            l1.pop(0)
        return c,ans
            
            
        
            
        


if __name__ == "__main__":
    b = BST()

    while True:
        print("1. Insert a value")
        print("2. Preorder traversal")
        print("0. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            b.root = b.insert(b.root, value)
        elif choice == 2:
            print("Preorder Traversal of the BST: ", end="")
            b.preorder(b.root)
            print()
        elif choice == 3:
            print("BFSr Traversal of the BST: ", end="")
            b.bfs(b.root,[])
            print()
        elif choice == 4:
            print("Min node of the BST: ", end="")
            b.minnode(b.root)
            print()
        elif choice == 5:
            print("Max node of the BST: ", end="")
            b.maxnode(b.root)
            print()
        elif choice == 6:
            c=b.leafnodes(b.root)
            print("Leaf nodes of the BST: ", c[1],end="\n")
            print("Total no of Leaf nodes of the BST: ", c[0],end="\n")
        elif choice == 7:
            c=b.nonleafnodes(b.root)
            print("Non Leaf nodes of the BST: ", c[1],end="\n")
            print("Total no of Non Leaf nodes of the BST: ", c[0],end="\n")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")
