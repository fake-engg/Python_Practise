class Student:
    def __init__(self, student_id=None,marks=None,age=None, course_id=None,fee=0):
        self.__student_id=None
        self.__marks = None
        self.__age =None
        self.__course_id = None
        self.__fees = None

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_id(self, student_id):
        self.__student_id = student_id

    def get_id(self):
        return self.__student_id
    
    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_course_id(self,course_id):
        self.__course_id = course_id
    
    def get_course_id(self):
        return self.__course_id
    
    def set_fees(self,fees):
        self.__fees = fees
    
    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if self.get_marks() >=0 and self.get_marks()<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.get_age()>20:
            return True
        else:
            return False
       
    def check_qualification(self):
        if self.validate_marks() ==True:
            if int(self.get_marks()) >= 65:
                return True
            else:
                return False
        else:
            return False
        
    def choose_course(self,course_id):
        if course_id == 1001 or course_id == 1002:
            self.set_course_id(course_id)
            if self.get_marks() > 85:
                if self.get_course_id() == 1001:
                    self.set_fees(25575.0 - 0.25 * 25575.0)
                elif self.get_course_id == 1002:
                    self.set_fees(15500.0 - 0.25 * 15500.0)
            else:
                if self.get_course_id() == 1001:
                    self.set_fees(25575.0) 
                elif self.get_course_id == 1002:
                    self.set_fees(15500.0)            
        else:
            return False


        
s1 = Student()
print("Student 1")
s1.set_id(101)
s1.set_marks(87)
s1.set_age(27)
s1.set_course_id(1002)
s1.get_fees()
print(s1.check_qualification())

print()
print("Student 2")

s2 = Student()
s2.set_id(102)
s2.set_marks(61)
s2.set_age(25)
print(s2.check_qualification())