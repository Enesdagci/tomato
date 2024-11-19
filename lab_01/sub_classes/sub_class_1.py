from base_classes.base_class import Person

class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name,email)
        self.__subject = subject

    def introduce(self):
        super().introduce()
        return "Name : {}, Email : {}, Lecture : {}".format(self.__name,self.__email,self.__subject)

class Student(Person):
    def __init__(self,name,student_id,email):
        super().__init__(name,email)
        self.__studentId = student_id

    def introduce(self):
        super().introduce()
        return "Student Id : {} Name : {}, Email : {}".format(self.__studentId,self.__name,self.__email)

class TA(Teacher,Student):
    def __init__(self,name,student_id,email,subject):
        super().__init__(name,email,student_id,subject)

    def introduce(self):
        super().introduce()
        return "Student Id : {} Name : {}, Email : {}".format(self.__studentId,self.__name,self.__email)

personel = TA("Enes",2342,"dAg")
print(TA.introduce)
print(TA.mro())
