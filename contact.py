class contact:
    def __init__(self,f_name,l_name,contact_no):
        self.f_name=f_name
        self.l_name=l_name
        self.contact_no=contact_no
    def putdata(self):
        f=open("contactlist.txt","w")
        #f=open("contact.txt","w")
        f.write(self.f_name)
        f.write(self.l_name)
        f.write(self.contact_no)
       # f.write(f_name,l_name,contact_no)
        f.close()
        
    def getdata(self):
       # f=open("contact list")
        f=open("contactlist.txt","r")
        f_name=f.read()
        l_name=f.read()
        contact_no=f.read()
        print(f_name," ",l_name," ",contact_no)
        f.close()
c1=contact("priya","gohite","9575951652")
c1.putdata()
print("\n")
c1.getdata()
print("\n")

   
    
        
