class Person:
    def __init__(self,fName,lName):
        self.fName = fName
        self.lName = lName

    def printName(self):
        print(self.fName,self.lName)

class Student(Person):
    pass


x = Student("Mayur","Chandra")
x.printName()