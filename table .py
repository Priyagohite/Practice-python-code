#Printing table of user defined integer

#1
n=int(input("Enter value for"))
m=n*10
for i in range(n,m+1,n):
    print(i)
    
#2
n=int(input("Enter value for"))
m=n*10
x=0
for i in range(n,m+1,n):
    x=x+1
    print(n,"*",x,"=",i)

#3
n=int(input("Enter value for"))
m=n*10
count=1
for i in range(n,m+1,n):
    print("{}*{}={}".format(n,count,i))
    count=count+1

