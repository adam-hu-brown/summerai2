class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []
    def myfunc(self):
        print("Hello my name is", self.name, "\nI am in grade", self.grade)

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
    def myfunc(self):
        print("This course is called:", self.name)

calc = Course("Calculus")
english = Course("English")
bob = Student("Bob", 11)
john = Student("John", 12)

bob.myfunc()
john.myfunc()