#permitation

x=int(input("Enter the total items:"))
y=int(input("Enter the no of item to be arrange:"))
def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
        return(fact_n)
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("p=",p)
 
