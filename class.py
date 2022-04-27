class cars:

#special function for class
    
 def __init__(self,b_name,model,types):#individual object k liye self ka use kiya hai

#specify
     self.b_name=b_name
     self.model=model
     self.types=types

      
#car1 object bnaya h
      
car1=cars("maruti","caiz","sedan")
y=car1.model
print(y)
