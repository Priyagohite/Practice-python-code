a=input('Enter the first number:')
b=input('Enter the second number:')
c=input('Enter the third number:')
a=int(a)
b=int(b)
c=int(c)
if(a>b and a>c):
  print(a, 'is greater', b, 'and', c)
elif(b>a and b>c):
  print(b, 'is greater', a, 'and', c)  
else:
  print(c, 'is greater', a, 'and', c)
