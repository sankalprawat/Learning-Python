class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Toppers(Student):
    def __init__(self, students):
        sorted_students = sorted(students, key=lambda s: s.marks, reverse=True)
        self.top_students = sorted_students[:3]

    def print_toppers(self):
        print("Top 3 Students:")
        for i, student in enumerate(self.top_students):
            total_marks = student.marks
            print(f"{i+1}. {student.name} - Total Marks: {total_marks} ")


students = [
    Student("Tanmay", 89),
    Student("Sheffali", 90),
    Student("Simran", 71),
    Student("Sankalp", 92),
    Student("Hardik", 55),
]

toppers = Toppers(students)
toppers.print_toppers()
