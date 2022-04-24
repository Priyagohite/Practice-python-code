print("This script is introduced to swap the value of two data variable using a third temporaray variable")

#1st method of swapping using third variable

a=input("Enter the first interger:")
b=input("Enter the second interger:")

print("values before swapping")

print("a=",a)
print("b=",b)

temp=a;
a=b;
b=temp;

print("values after swapping")

print("a=",a)
print("b=",b)

#2.a,b=b,a
a=input("Enter the first interger:")
b=input("Enter the second interger:")

print("values before swapping")

print("a="+a)
print("b="+b)

a,b=b,a

print("values after swapping")

print("a=",a)
print("b=",b)




