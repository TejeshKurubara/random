from abc import ABC, abstractmethod


class GradeCalculator(ABC):

    @abstractmethod
    def calculate_grade(self):
        pass


class Student(GradeCalculator):

    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.__marks = []

    def add_marks(self):

        for i in range(5):
            mark = int(input("Enter Mark: "))
            self.__marks.append(mark)

    def calculate_grade(self):

        total = sum(self.__marks)
        avg = total / len(self.__marks)

        print("Average =", avg)

        if avg >= 90:
            print("Grade : A+")

        elif avg >= 80:
            print("Grade : A")

        elif avg >= 70:
            print("Grade : B")

        elif avg >= 60:
            print("Grade : C")

        else:
            print("Grade : Fail")

    def display(self):

        print("\nRoll Number :", self.roll)
        print("Name :", self.name)
        print("Marks :", self.__marks)

        self.calculate_grade()


students = []

while True:

    print("\n===== STUDENT GRADE MANAGEMENT =====")
    print("1.Add Student")
    print("2.Display Students")
    print("3.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")

        s = Student(roll, name)
        s.add_marks()

        students.append(s)

        print("Student Added Successfully")

    elif ch == 2:

        if len(students) == 0:
            print("No Student Records")

        else:

            for s in students:
                s.display()

    elif ch == 3:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
