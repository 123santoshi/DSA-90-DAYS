def reverse_string(s):
    l=[]
    for i in s:
        l.append(i)
    print("Original string==",l)
    r=[]
    for i in range(len(l)):
        ele=l.pop()
        r.append(ele)
    print("After reverse==",r)
    
    
    
s=input("Enter string to reverse using stack==")
reverse_string(s)  