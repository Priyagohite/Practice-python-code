'''class(object):
    def __intit_(self,arg):
        super(,self)__init__()
        self.arg=arg
'''
#overriding
        
class school():
    def __init__(self):
        self.name=input("Enter school name:")
        self.address=input("Enter school address:")
    def show(self):
        print("{} is situated at {}".format(self.name,self.address))
item1=school()
item1.show()
