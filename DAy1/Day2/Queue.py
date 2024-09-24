class Queue:
    def __init__(self):
        self.queue=[]
    
    def isempty(self):
        return self.queue==[]
    
    def peak(self):
        if(self.isempty()):
            return "No elements found in queue"
        else:
            return self.queue[-1]
        
    def display(self):
        if(self.isempty()):
            return "No elements found in queue to display"
        else:
            return self.queue
    
    def enqueue(self,item):
        if(len(self.queue)>=size):
            return "Overflow"
        elif(len(self.queue)==0):
            self.queue.append(item)
            print(self.queue)
            return "{} is enqueued to the queue".format(item)

        else:
            self.queue.append(0)
            for  i in range(len(self.queue)-2,-1,-1):
                self.queue[i+1]=self.queue[i]
            self.queue[0]=item
            return "{} is enqueued to the queue".format(item)

    def dequeue(self):
        if(len(self.queue)==0):
            return "Underflow"
        else:
            del_item=self.queue[-1]
            self.queue.pop(-1)
            return del_item
        



if __name__==f"__main__":
    q=Queue()
    size=int(input("Enter length of the queue=="))
    while(True):
        option=int(input("Select the operation that you want to perform : \n 1.Enqueue  \n 2.Dequeue \n 3.Display \n 4.Peak \n 5.Isempty \n 6.Exit ="))
        if(option==1):
            ele=int(input("Enter element to push into the queue==="))
            res=q.enqueue(ele)
            print(res)
        elif(option==2):
            res=q.dequeue()
            print(res)
        elif(option==3):
            res=q.display()
            print(res)
        elif(option==4):

            res=q.peak()
            print(res)
        elif(option==5):
            res=q.isempty()
            print(res)
        else:
            break
    

    