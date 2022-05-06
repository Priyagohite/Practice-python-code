'''def div(x,y):
    return x/y
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=div(a,b)

print("a=",a)
print("b=",b)
print("c=",c)

def div(x,y):
    return x/y
from support import*
def smart_div(func):
    def inner(m,n):#no of parameter should be same no alg ho skte h
        if m<n:
            m,n=n,m
            return m,n
        return(funct)
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=div(a,b)
d=smart_div(div)

print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
'''

from support import *
'''def div(x,y):
    return x/y
'''
def smart_div(func):
    def inner(m,n):#no of parameter should be same no alg ho skte h
        if m<n:
            m,n=n,m
        return func(m,n)
    return inner
    
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=div(a,b)
div1=smart_div(div)
d=div1(a,b)

print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)


'''method class k andr hoti h
method are of three type
instance
class
static'''

