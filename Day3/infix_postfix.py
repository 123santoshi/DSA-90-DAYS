def precedence(p):
    if p=='+' or p=='-':
        return 1
    elif p=='*' or p=='/':
        return 2
    elif p=='^':
        return 3
    else:
        return 0

def infix_postfix(s):
    operators=[]
    operands=[]



s="A+B*(C^D-E)^(F+G*H)-I"
infix_postfix(s)