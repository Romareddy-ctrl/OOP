#VARIABLES IN OOP
#Instance Variable
#CLASS(STATIC) VARIABLE
class Student:
    school = "ABC school"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


s1=Student(34,35,36)
s2=Student(43,44,45)
s1.m1=8
Student.school="SSC school"

print(s1.m1,s1.m2,s1.m3)
print(s2.m1,s2.m2,s2.m3)


