import fact2
x=int(input("Enter the total items:"))
y=int(input("Enter the no of item to be arrange:"))
fx=fact2.fact(x)
fy=fact2.fact(x-y)
p=fx/fy
print("p=",p)
