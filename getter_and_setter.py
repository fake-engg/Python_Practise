class Student:
    def setName(self,name):
        self.name= name
    
    def getName(self,name):
        return self.name
    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self,marks):
        return self.marks
    
n = int(input("Enter the number of Students: "))

for i in range(n):
    s = Student()
    name = input('Enter the name: ')
    s.setName(name)
    marks = int(input('Enter the marks: '))
    s.setMarks(marks)

    print(f"Hi {s.getName(name)}, your marks are: {s.getMarks(marks)}")
    
    