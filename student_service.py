
from student import Student


class StudentService:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, marks):
        if student_id in self.students:
            raise ValueError("Student ID already exists")

        if not name.strip():
            raise ValueError("Student name cannot be empty")

        if not marks:
            raise ValueError("Marks cannot be empty")

        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks must be between 0 and 100")

        student = Student(student_id, name, marks)
        self.students[student_id] = student

        return student

    def get_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Student not found")

        return self.students[student_id]

    def calculate_average(self, student_id):
        student = self.get_student(student_id)

        return sum(student.marks) / len(student.marks)
