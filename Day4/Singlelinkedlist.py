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
        new_node=Node(self.data)
        if self.head is None:
            self.head=new_node
            return "{} inserted into the list".format(self.data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    
    def display(self):
        if self.head is None:
            return "Empty linked list .No data to display "
        cur=self.head
        while cur.next is not None:
            print(cur.data , "--->")
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


s=SLL()
ans=s.insert_at_begin(5)
print(ans)
s1=s.display()
print(s1)
        



    



