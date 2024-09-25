class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return "{} inserted into the list".format(data)
        else:
            new_node.next=self.head
            self.head=new_node
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        
    def insert_at_pos(self,data,pos):
        if(pos==0 or self.head is None):
            self.insert_at_begin(data)
        else:
            new_node=Node(data)
            prev=self.head
            cur=prev.next
            for i in range(pos-1):
                prev=prev.next
                cur=cur.next
            new_node.next=cur
            prev.next=new_node
    
            
    def length(self):
        count=0
        if self.head is None:
            return "Length of linked list is = {}".format(count)
        else:
            temp=self.head
            while temp:
                c+=1
                temp=temp.next
        return c
        
    def display(self):
        if self.head is None:
            return "Empty linked list .No data to display "
        cur=self.head
        while cur:
            print(cur.data , "--->" ,end="")
            cur=cur.next


    def delete_front(self):
        if self.head is None:
            return "Empty Linked list .No items found to delete"
        else:
            temp=self.head
            self.head=temp.next
            return "deleted the front elemenet"
    
    
    def delete_end(self):
        if self.head is None:
            return "Empty Linked list .No items found to delete"
        else:
            prev=self.head
            cur=prev.next
            while cur.next:
                cur=cur.next
                prev=prev.next
            prev.next=None
            return "Deleted the last element "


if __name__=="__main__":
    s=SLL()
    while(True):
        option=int(input(" \n 1.insert first  \n 2.insert End \n 3.Display \n 4.Delete first \n 5.Delete End \n 6.Length \n 7.Insert position \n 8.Exit \n Select the operation that you want to perform == "))
        if(option==1):
            ele=int(input("Enter element to insert into the linked list ==="))
            res=s.insert_at_begin(ele)
        elif(option==2):
            ele=int(input("Enter element to insert into the linked list ==="))
            res=s.insert_at_end(ele)
        elif(option==3):
            res=s.display()
        elif(option==4):
            res=s.delete_front()
        elif(option==5):
            res=s.delete_end()
        elif(option==6):
            res=s.length()
        elif(option==7):
            ele=int(input("Enter element to insert into the linked list ==="))
            pos=int(input("Enter in which position you want to insert the element"))
            res=s.insert_at_pos(ele,pos)
        else:
            break
        



    



