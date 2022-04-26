n=int(input("Enter the no:"))
count=0
for i in range(2,n-1):
       if(n%i==0):
           count=1
if(count==0):
     print("prime no")
else:
    print("Not a prime no")
        
