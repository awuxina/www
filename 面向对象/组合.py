class Teacher:
    def __init__(self,name,sex,course):
        self.name=name
        self.sex=sex
        self.course=course

class Student:
    def __init__(self,name,sex,course):
        self.name = name
        self.sex = sex
        self.course = course

class Course:
    def __init__(self,name,price,peroid):
        self.name=name
        self.price=price
        self.peroid=peroid

t=Teacher('egon','男',Course('python',15800,'7m'))
print(t.course.name)
s=Student('小名','男',Course('python',15800,'7m'))