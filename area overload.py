class area():
    def a(self,r=None,l=None):
        if(r!=None and l!=None):
            ar=l*r
            return ar
        elif(r!=None and l==None):
            ac=22/7*r*r
            return ac
        else:
           print("No value provided")
    
a1=area()
rect=a1.a(2,3)
circle=a1.a(2)
q=a1.a()

print("Area of rectangle:",rect)
print("Area of circle:",circle)
