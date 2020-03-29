class Person:
    def __init__(self,fName,lName):
        print("Person class init called")
        self.fName = fName
        self.lName = lName

    def printName(self):
        print(self.fName,self.lName)

class Student(Person):
    def __init__(self, fname, lname,year):
        print("sub class calling Parent class")
        super().__init__(fname, lname)
        self.graduationYear = year
    def welcome(self):
        print("Welcome ",self.fName,self.lName," to the class of ",self.graduationYear)



x = Student("Mayur","Chandra",2005)
x.printName()
x.welcome();