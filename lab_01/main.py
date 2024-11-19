#Kutuphaneler
from sub_classes import Teacher
from sub_classes import Student

if __name__ == "__main__":
    person_1 = Student(234210024,"Enes","Dagci@")
    person_2 = Teacher("Harun","kıran@gmail.com","Computer Eng.")
    
    print(person_1.introduce())
    print(person_2.introduce())




