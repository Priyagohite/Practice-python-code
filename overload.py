#method of overloading
class student():
   '''' def __init__(self):
        self.a=a
        self.b=b
        self.c=c'''
   def avg(self,a=None,b=None,c=None):
      average=0
      if(a!=None and b!=None and c!=None):
        average=(a+b+c)/3
      elif(a!=None and b!=None and c==None):
        average=(a+b)/2
      elif(a!=None and b==None and c==None):
        average=a
      else:
        average="no values provided"
      return average
   
s1=student()
avg2=s1.avg(2,4)
avg3=s1.avg(6)
avg4=s1.avg()

print(avg2)
print(avg3)
print(avg4)

