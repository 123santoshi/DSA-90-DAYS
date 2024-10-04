def balanced_paranthesis(s):
    l=[]
    pairs= {'{':'}' , '(':')', '[':']' }
    for i in s:
        if i=="(" or i=="{" or i=="[":
            l.append(i)
        elif(i=='}' or i==']' or i==')'):
            if len(l)==0 or pairs[l.pop()]!=i:
                return False
    if(len(l)==0):
        return True
    
    
    
    
s=input("Enter string to reverse using stack==")
ans=balanced_paranthesis(s)
if(ans):
    print("balanced")
else:
    print("Not balanced")