class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class CDLL:

    def __init__(self):
        self.head=None
        

    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.prev=new_node
            new_node.next=new_node
            self.head=new_node
        else:
            temp=self.head
            while temp.next !=self.head:
                temp=temp.next
            new_node.prev=temp.next
            new_node.next=self.head
            temp.next=new_node
            self.head.prev=new_node
            self.head=new_node
        s.display()
        


    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.prev=new_node
            new_node.next=new_node
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            new_node.prev=temp
            new_node.next=self.head
            temp.next=new_node
            self.head.prev=new_node
        s.display()



    def display(self):
        if self.head is None:
            print('No elements found to display')
        else:
            temp=self.head
            while temp.next!=self.head:
                print(temp.data,"===>" ,end="")
                temp=temp.next
            print(temp.data,"===>",end=" ")



    
    def delete_front(self):
        if self.head is None:
            print("No elements found to delete in CDLL")
        elif self.head.next == self.head:
            self.head=None
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=self.head.next
            self.head=self.head.next
            self.head.prev=temp
        s.display()


        
    def delete_end(self):
        if self.head is None:
            print("No elements found to delete in CDLL")
        elif self.head.next == self.head:
            self.head=None
        else:
            prev=self.head
            cur=self.head.next
            while cur.next!=self.head:
                cur=cur.next
                prev=prev.next
            prev.next=cur.next
            self.head.prev=prev
            cur.next=None
        s.display()
            
            
    
    def length(self):
        count=0
        if self.head is None:
            print('length is =={0}'.format(count))
        else:
            temp=self.head
            count=1
            while temp.next!=self.head:
                count+=1
                temp=temp.next
            print('length is =={0}'.format(count))
            
            
    def search(self,ele):
        found=0
        if self.head is None:
            print("CDLL IS empty to search ")
        else:
            temp=self.head
            while temp.next!=self.head:
                if temp.data==ele:
                    found=1
                    break
                else:
                    temp=temp.next
            if(temp.data==ele):
                found=1
        if(found==1):
            print("Element found")
        else:
            print("Element not found")


    
    def duplicate_search(self):
        d={}
        duplicates_list=[]
        if self.head is None:
            print("No eleements found to search ")
        else:
            temp=self.head
            while temp.next!=self.head:
                if temp.data not in d:
                    d[temp.data]=1
                else:
                    d[temp.data]+=1
                temp=temp.next
            if temp.data not in d:
                d[temp.data]=1
            else:
                d[temp.data]+=1
            
        for i in d:
            if  d[i]>1:
                duplicates_list.append(i)
        
        if(len(duplicates_list)==0):
            print("No duplicate elemnts found")
        else:
            print("duplicate elemetns are =={0}".format(duplicates_list))
            
    


    def unique_elements(self):
        d={}
        unique_list=[]
        if self.head is None:
            print("No eleements found to search ")
        else:
            temp=self.head
            while temp.next!=self.head:
                if temp.data not in d:
                    d[temp.data]=1
                else:
                    d[temp.data]+=1
                temp=temp.next
            if temp.data not in d:
                d[temp.data]=1
            else:
                d[temp.data]+=1
        for i in d:
            if  d[i]==1:
                unique_list.append(i)
        
        if(len(unique_list)==0):
            print("No unique elemnts found")
        else:
            print("Unique  elemetns are =={0}".format(unique_list))


    def sort_elements(self):
        if self.head is None:
            print("No eleements found to sort ")
        else:
            temp = self.head
            while True:
                min_node = temp
                next_node = temp.next
                while next_node != self.head:
                    if next_node.data < min_node.data:
                        min_node = next_node
                    next_node = next_node.next
                temp.data, min_node.data = min_node.data, temp.data
                temp = temp.next
                if temp == self.head:
                    break
            
        s.display()

                
        
            
if __name__=="__main__":
    s=CDLL()
    while(True):
        option=int(input(" \n 1.insert first  \n 2.insert End \n 3.Display \n 4.Delete first \n 5.Delete End \n 6.Length \n 7.Search\n 8. Duplicate Elements \n 9.Unique Elements \n 10.Sort Elements \n 11.Exit \n Select the operation that you want to perform == "))
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
        elif(option==8):
            s.duplicate_search()
        elif(option==9):
            s.unique_elements()
        elif(option==10):
            s.sort_elements()
        else:
            break
        



    



