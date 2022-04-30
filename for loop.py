#for loop

a=input("Enter your name:")
print(type(a))
print(a)
for p in a:
   print(p)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7+3)

a=100
for i in range(a):
    print(i)

n=5
for i in range (n):
    print(i)


n=10
for i in range (1,n+1):
    print(i)

n=10
for i in range (2,21,2):
    print(i)
'''#print table while using for loop...
n=int(input("Enter value:"))
m=n*10
x=0
for i in range(n,m+1,n):
    x=x+1
    print(n,"*",x,"=",i)

n=int(input("Enter value:"))
m=n*10
count=1
for i in range(n,m+1,n):
    print("{}*{}={}" .format(n,count,i))
    count=count+1
'''


