class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
    
class CLL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=new_node
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            self.head=new_node
        
        self.display()


    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=new_node
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
        
        self.display()
    
    def display(self):
        if self.head is None:
            print("NO ELEMENTS FOUND IN THE CLL")
        else:
            temp = self.head
            while True:
                print(temp.data, "===>", end=" ")
                temp = temp.next
                if temp == self.head:
                    break
                

    def delete_front(self):
        if self.head is None:
            print("No elements found to delete ")
        elif self.head.next == self.head:
            self.head =None
        else:
            temp=self.head
            while temp.next !=self.head:
                temp=temp.next
            
            temp.next=self.head.next
            self.head= temp.next
            
        self.display()
            
    def delete_end(self):
        if self.head is None:
            print("No elements found to delete ")
        elif self.head.next == self.head:
            self.head =None
        else:
            prev=self.head
            cur=self.head.next
            while cur.next!=self.head:
                cur=cur.next
                prev=prev.next
                
            prev.next=cur.next
            cur.next=None
            
        self.display()

    
    
    def length(self):
        count=0
        if self.head is None:
            print("lenght is == {0}".format(count))
        else:
            temp=self.head
            count=1
            while temp.next!=self.head:
                count+=1
                temp=temp.next
            print("lenght of cll=={0}".format(count))
            
    
    def search(self,ele):
        found=0
        if self.head is None:
            print("No elements found to search the element")
        else:
            temp=self.head
            while temp.next!=self.head:
                if(temp.data==ele):
                    found=1
                    break
                else:
                    temp=temp.next
        if(found==1):
            print("Element found in CLL ")
        else:
            print("Element not found in CLL")
        
            
if __name__=="__main__":
    s=CLL()
    while(True):
        option=int(input(" \n 1.insert first  \n 2.insert End \n 3.Display \n 4.Delete first \n 5.Delete End \n 6.Length \n 7.Search Element \n 8.Exit \n Select the operation that you want to perform == "))
        if(option==1):
            ele=int(input("Enter element to insert into the linked list ==="))
            s.insert_at_begin(ele)
        elif(option==2):
            ele=int(input("Enter element to insert into the linked list ==="))
            s.insert_at_end(ele)
        elif(option==3):
            s.display()
        elif(option==4):
            s.delete_front()
        elif(option==5):
            s.delete_end()
        elif(option==6):
            s.length()
        elif(option==7):
            ele=int(input("Enter element to insert into the linked list ==="))
            s.search(ele)
        else:
            break
        