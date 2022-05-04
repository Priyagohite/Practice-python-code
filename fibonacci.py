n=int(input("How many values"))

#first two terms

n1=0
n2=1
sum=0
count=1
print("fibonacci series:",end="\n")
while(count<=n):
    print(sum,end="")
    count+=1
    n1=n2
    n2=sum
    sum=n1+n2

