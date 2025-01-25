""" class Student:
    '''this is a docstring and can be used to provide discription about the class'''
    def __init__(self,x,y,z):
        self.name = x
        self.age= y         # here name, age and marks are instance variables. x,y and z are the parameters passed.
        self.marks = z
    
    def display(self):      # self is the first parameter that should be passed to a instance method
        print("Student Name: {}  age is: {}  Marks is: {}".format(self.name,self.age,self.marks))

s1 = Student('Shivam',25,90)        #reference variables are created for the objects
s2 = Student('Abhishek',26,95)

s1.display()            # using referecne variables, we can access the instance variables and instance methods
s2.display() """


class Employee:
    def __init__(self, eno, ename, esal, eadd):
        self.eno = eno 
        self.ename = ename 
        self.esal = esal
        self.eadd = eadd

    def details(self):
        print("Employee num: ", self.eno)
        print("Employee name: ",self.ename)
        print("Employee salary: ",self.esal)
        print("Employee address: ",self.eadd)

e1 = Employee(101,'Shivam',25000,'BLR')
e1.details()

print()

e2 = Employee(102,'Abhishek',40000,'KOL')
e2.details()