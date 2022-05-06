print("Welcome to my calculator: ")
#function multiply two values

def mul(x,y):
   return x*y

#function divides two values

def div(x,y):
    return x/y

#function add two values

def add(x,y):
    return x+y

#function modulo two values

def mod(x,y):
     return x%y
#function pow two values

def sqr(x):
     return x*x

def cube(x):
    return x*x*x

def pow(x):
    n=int(input("enter power u want"))
    return x**n
def sqroot(x):
    return x**(0.5)

def cbroot(x):
   return x**1/3

print("select operation:")
print("1.Addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")
print("5.modulo")
print("6.sqr")
print("7.cube")
print("8.sqroot")

user=str.lower(input("which type of operation to be perform(unary,binary): "))
if(user=='unary'):
    x=int(input("Enter the number:"))
elif(user=='binary'):
  a=str.lower(input("Enter which type of value(int,float) you want to enter: "))
  if(a=='int'):
       x=int(input("Enter the first no:"))
       y=int(input("Enter the second no:"))
  elif(a=='float'):
       x=float(input("Enter the first no:"))
       y=float(input("Enter the second no:"))
  else:
      print("either int or float")
else:
    print("either unary or binary: ")

#choice=input("Enter choice(1,2,3,4,5)")
choice=input("enter operator which operation is perform: ")
if(choice=='+'):
    i=add(x,y)
    print(x,"+",y,"=",i)
elif(choice=='-'):
    i=sub(x,y)
    print(x,"-",y,"=",i)
elif(choice=='*'):
    i=mul(x,y)
    print(x,"*",y,"=",i)
elif(choice=='/'):
    i=div(x,y)
    print(x,"/",y,"=",i)
elif(choice=='%'):
    i=mod(x,y)
    print(x,"%",y,"=",i)
elif(choice=='sqr'):
    i=sqr(x)
    print(x,"sqr","=",i)
elif(choice=='cube'):
    i=cube(x)
    print(x,"cube","=",i)
elif(choice=='pow'):
    i=pow(x)
    print(x,"pow","=",i)
elif(choice=='sqroot'):
    i=sqroot(x)
    print(x,"sqroot","=",i)
elif(choice=='cbroot'):
    i=cbroot(x)
    print(x,"cbroot","=",i)
else:
   print("wrong choice")



