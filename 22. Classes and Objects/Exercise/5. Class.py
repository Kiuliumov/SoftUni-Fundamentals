class Class:
    __student_count = 22
    def __init__(self,name):
        self.name = name
        self.students = []
        self.grades = []
    def add_student(self,name,grade):
        if len(self.students) and len(self.grades) < Class.__student_count:
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
    def __repr__(self):
        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {Class.get_average_grade()}.'