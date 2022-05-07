#open file

f=open("Myfirstfile.txt","w")
x="PRIYA GOHITE"
f.write(x)
y="RANI PAWAR"
f.write("\n"+y)
#f.write(y)
f.close()

#read file

f=open("Myfirstfile.txt","r")
x=f.read()
print(x)
f.close()
