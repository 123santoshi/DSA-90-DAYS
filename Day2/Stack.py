class Stack :
    
    def __init__(self):
        self.stack=[]
    
    def isempty(self):
        if(len(self.stack)==0):
            return 1
        else:
            return 0
    
    def push (self,data):
        #print("push method ")
        if(len(self.stack)>size):
            return "Overflow"
        else:
            self.stack.append(data)
            return "{} is pushed into stack".format(data)
    
    def pop (self):
        #print("pop method ")
        if(len(self.stack)==0):
            return "Underflow"
        else:
            deleted=self.stack.pop()
            return "{} is deleted from stack".format(deleted)
    
    def display(self) :
        if(len(self.stack)==0):
            print('No elements in the stack')
        else:
            return self.stack
    def peak(self):
        #print("peak method ")

        if(len(self.stack)==0):
            return "stack is empty"
        else:
            return self.stack[-1]
if __name__=="__main__":
    s=Stack()
    size=int(input("Enter length of the stack=="))
    while(True):
        option=int(input("Select the operation that you want to perform :  1.Push  \n 2.Pop \n 3.Display \n 4.Peak \n 5.Isempty \n 6.Exit = "))
        if(option==1):
            ele=int(input("Enter element to push into the stack==="))
            res=s.push(ele)
            print(res)
        elif(option==2):
            res=s.pop()
            print(res)
        elif(option==3):
            res=s.display()
            print(res)
        elif(option==4):

            res=s.peak()
            print(res)
        elif(option==5):
            res=s.isempty()
            print(res)
        else:
            break
    