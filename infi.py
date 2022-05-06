print("Python program to evaluate postfix expression")

def postfix_evaluate(ev,a):
    flag=0
    for i in ev:
        if(i.isdigit()):
            stk.append(i)
        else:
            
            if(a=='int' and flag==0):
                op2=int(stk.pop())
                op1=int(stk.pop())
            else:
                op2=float(stk.pop())
                op1=float(stk.pop())
            if(i== '+'):
                stk.append(op1+op2)
            elif(i== '-'):
                stk.append(op1-op2)
            elif(i== '*'):
                stk.append(op1*op2)  
            elif(i== '/'):
                if(op1%op2!=0):
                    flag=1
                stk.append(op1/op2)
            elif(i== '^'):
                stk.append(pow(op1,op2))
    return stk.pop()


stk=[]
postfix=["5","7","3","/","+"]

a=input("int or float: ")
ans=postfix_evaluate(postfix,a)
print(ans)


operator = ["+","-","/","*","%","(",")"]
numeral = ["0","1","2","3","4","5","6","7","8","9","."]
expression = []
input_exp = input("Enter the expression : ")
print("Input =", input_exp)
operand = ""
top=-1
flag=0
for i in input_exp :
    if i in numeral :
        operand = operand+i
        flag=1
    elif i in operator :
        if(flag==1):
            expression.append(operand)
            operand = ""
            flag=0
            expression.append(i)
        else:
            expression.append(i)
    else :
        print("Invalid Character")
        break
if(flag==1):
    expression.append(operand)
print("Input (in list) = ", expression )
stk=[]
postfix=convert(expression)
print(postfix)
