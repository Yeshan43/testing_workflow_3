
from student_service import StudentService


def main():
    service = StudentService()

    student = service.add_student(
        student_id=1,
        name="Kamal",
        marks=[80, 75, 90],
    )

    average = service.calculate_average(student.student_id)

    print("Student Management System")
    print(f"Student ID: {student.student_id}")
    print(f"Student Name: {student.name}")
    print(f"Marks: {student.marks}")
    print(f"Average Marks: {average:.2f}")


if __name__ == "__main__":
    main()
