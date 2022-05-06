#program with function

'''#using iteration method

import time

def fact(n):
    fact_n=1
    for i in range(1,n+1):
         fact_n=fact_n*i
    return(fact_n)

#print("factorial of", n ,"=", fact_n)
x=int(input("Enter a number to calculate a factorial:"))

start=time.time()

factorial=fact(x)
print("factorial of {} is: {}".format(x,factorial))

end=time.time()
print("Execution time:",end-start)
'''

#y=int(input("Enter the value:"))
#y=fact(s)
#fact(x)
#fact(y)



#using iteration method

import time

#start=time.time()

print("to find the factorial of a user defined number\n")
n=int(input())
start=time.time()
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("factorial of {} is: {}".format(n,fact))

end=time.time()
print("Execution time :",end-start)


#using recursion method

import time

def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        y=x*fact(x-1)
        return y
n=int(input("Enter the number to calculate factorial:"))
start=time.time()
factorial=fact(n)
print("factorial of {} is {}".format(n,factorial))

end=time.time()
print("Execution time :",end-start)


'''
#using function method
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    else:
        for i in range(x,0,-1):
            y=y*i
        return y
funct_val=fact(5)
print("factorial of {} is {}".format(5,funct_val))'''

