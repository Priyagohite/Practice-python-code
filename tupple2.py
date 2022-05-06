t1=[1,2,3,4]
t2=[9,8,7,6]
print(t1)
print(id(t1))
t1+=t2
print(t1)
print(id(t1))
#t1.append(26)
#tupple k case m memory location badal jati hai operation perform karne k baad isliye unki id change ho jati h

t1=(1,2,3,4)
t2=(9,8,7,6)
#t1=t2
print(t1)
print(id(t1))

#usi tupple ko agr list me convert kar denge to memory location nahi badlegi koi bhi operation perform karne k baad isliye uski id bhi sam rhegi;
