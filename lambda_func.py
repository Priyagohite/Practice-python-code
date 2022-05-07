'''
int(input("Enter value of a : "))
int(input("Enter value of b : "))
'''
a = 4
b = 3
z = lambda x,y: x+y
print(z(2,4))

list1=[2,13,42,4,524,331,67,89,45,90]
list_even=[]
print(list1)
print(list_even)
for i in list1:
    if i%2 == 0:
        list_even.append(i)
print(list_even)

'''
def even(n):
    return n%2==0

list1=[2,13,42,4,524,331,67,89,45,90]

list_even=[]

print(list1)
print(list_even)

for i in list1:
        y==even(i)
        if y==True:
            list_even.append(i)
print(list_even)
'''



