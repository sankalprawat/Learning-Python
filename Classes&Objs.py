class Student:
    def __init__(self, name, roll_no, test_marks, activity_marks, sport_marks):
        self.name = name
        self.roll_no = roll_no
        self.test_marks = test_marks
        self.activity_marks = activity_marks
        self.sport_marks = sport_marks

    def display_details(self):
        print("Name : ", self.name)
        print("Roll Number : ", self.roll_no)
        print("Test Marks : ", self.test_marks)
        print("Activity marks : ", self.activity_marks)
        print("Sports marks : ", self.sport_marks)


class Result:
    @staticmethod
    def final_result(test_marks, activity_marks, sport_marks):
        total_marks = sum(test_marks) + activity_marks + sport_marks
        avg_marks = total_marks / (len(test_marks) + 2)

        print("Total marks of student is : ", total_marks)
        print("Average marks of student is :", avg_marks)

        if avg_marks <= 33:
            return "Fail"
        else:
            return "Pass"


name = "Sankalp"
roll_num = '0153'
test_marks = [90, 92, 89, 95]
activity = 88
sports = 60

student1 = Student(name, roll_num, test_marks, activity, sports)
student1.display_details()
final_result = Result.final_result(test_marks, activity, sports)
print("The result of the student is : ", final_result)
