class Person:
    def __init__(self,fName,lName):
        print("Person class init called")
        self.fName = fName
        self.lName = lName

    def printName(self):
        print(self.fName,self.lName)

class Student(Person):
    def __init__(self, fname, lname):
        print("sub class calling Parent class")
        super().__init__(fname, lname)



x = Student("Mayur","Chandra")
x.printName()