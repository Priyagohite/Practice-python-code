class A:
    def random(self):
        print("I an in class A")
#a ko inherit kiya hai
#multiple value inherit krna
class c:
    def random(self):
       print("I am in class C")
class B(A):
    def random(self):
        print("I am in class B")
item1=B()
item1.random()
