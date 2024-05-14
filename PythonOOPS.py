class Result:
    def __init__(self, name, roll_number, test_marks):
        self.name = name
        self.roll_number = roll_number
        self.test_marks = test_marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Test Marks:", self.test_marks)

class Student(Result):
    def display_details(self):
        super().display_details()
        print("Activity Marks:", self.activity_marks)
        print("Sports Marks:", self.sports_marks)

    def __init__(self, name, roll_number, test_marks, activity_marks, sports_marks):
        super().__init__(name, roll_number, test_marks)
        self.activity_marks = activity_marks
        self.sports_marks = sports_marks

    def calculate_result(self):
        total_marks = sum(self.test_marks) + self.activity_marks + self.sports_marks
        average_marks = total_marks / (len(self.test_marks) + 2)
        if average_marks >= 50:
            return "Pass"
        else:
            return "Fail"

# Example usage
name = "John Doe"
roll_number = "123456"
test_marks = [85, 78, 92]
activity_marks = 15
sports_marks = 10

student = Student(name, roll_number, test_marks, activity_marks, sports_marks)
student.display_details()
print("Final Result:", student.calculate_result())
