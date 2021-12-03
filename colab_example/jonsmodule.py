class Student:

    def __init__(self,name,email,grades={}):
        self.name=name
        self.email=email
        self.grades=grades

    def add_grade(self,course,grade):
        self.grades[course]=grade

    def get_grades(self):
        return self.grades
