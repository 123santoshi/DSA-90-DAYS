class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DLL:
    
    def __init__(self):
        self.head =None
        
    def insert_at_begin(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        print("{} is inserted first  successfully(else)".format(data))
    
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            print("{} is inserted first successfully(if)".format(data))
        else:
            temp=self.head
            while temp.next is not None:
            
                temp=temp.next
            new_node.prev=temp
            temp.next=new_node
            
    def delete_front(self):
        if self.head is None:
            print("No elements found to delete")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            temp.next.prev = None
            self.head=temp.next
            print("deleted ")
        
    def delete_end(self):
        if self.head is None:
            print("No elements found to delete")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head 
            while temp.next :
                temp=temp.next
            temp.prev.next=None
            
                
        
    def display(self):
        if self.head is None:
            print("No elements found in the DLL to display")
        else:
            temp = self.head
            while temp.next:
                print(temp.data, "==>", end=" ")
                temp=temp.next
            print(temp.data)
    
    def length(self):
        count=0
        if self.head is None:
            print(count)
        else:
            temp = self.head
            count=1
            while temp.next is not None:
                count+=1
                print("size of DLL is {}".format(count))
                temp=temp.next
    
    def insert_at_pos(self,data,pos):
        if(pos==0 or self.head is None):
            self.insert_at_begin(data)
        elif(pos==1 or self.next.next is None):
            self.insert_at_end(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
            new_node.prev=temp.prev
            new_node.next=temp
            temp.prev.next=new_node
            temp.prev=new_node
    
    def search (self,item):
        found=0
        if self.head is None:
            print("No item found to search ")
        elif(self.head.next is None):
            if self.head.data==item:
                found=1
                print("Element found")
        else:
            temp=self.head
            while temp.next:
                if temp.data==item:
                    found=1
                    print("Element found")
                    break
                else:
                    temp=temp.next
            if(found==0):
                print("ELement not found")
            
            
            

if __name__=="__main__":
    s=DLL()
    while(True):
        option=int(input(" \n 1.insert first  \n 2.insert End \n 3.Display \n 4.Delete first \n 5.Delete End \n 6.Length \n 7.Insert position \n \n 8. Search 9.Exit \n Select the operation that you want to perform == "))
        if(option==1):
            ele=int(input("Enter element to insert into the linked list ==="))
            s.insert_at_begin(ele)
        elif(option==2):
            ele=int(input("Enter element to insert into the linked list ==="))
            s.insert_at_end(ele)
        elif(option==3):
            res=s.display()
        elif(option==4):
            s.delete_front()
        elif(option==5):
            res=s.delete_end()
        elif(option==6):
            s.length()
        elif(option==7):
            ele=int(input("Enter element to insert into the linked list ==="))
            pos=int(input("Enter in which position you want to insert the element"))
            s.insert_at_pos(ele,pos)
        elif(option==8):
            ele=int(input("Enter element to search ==="))
            s.search(ele)
        else:
            break
            
        
            

            