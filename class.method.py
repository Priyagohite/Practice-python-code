#ese method 
#instance method

class student():
    institution="IIPS"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
         print("--------------------------")
         print("Marks in pyhton=",self.a)
         print("Marks in pyhton lab=",self.b)
         print("---------------------------")
         
    @classmethod
    def info(self):
       print("class belongs to",self.institution)#class belong kr rha h
    @staticmethod
    def about():
        print("this class hold the data of marks obtained by student")
s1=student(12,10)
s2=student(13,11)
s3=student(14,9)
s1.show()
s2.show()
s3.show()

student.info()
student.about()
print(student.institution)
