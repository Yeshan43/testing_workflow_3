
import unittest

from student_service import StudentService


class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.service = StudentService()

    def test_add_student(self):
        student = self.service.add_student(
            1, "Kamal", [80, 75, 90]
        )

        self.assertEqual(student.name, "Kamal")
        self.assertEqual(student.student_id, 1)

    def test_get_student(self):
        self.service.add_student(1, "Kamal", [80, 90])

        student = self.service.get_student(1)

        self.assertEqual(student.name, "Kamal")

    def test_calculate_average(self):
        self.service.add_student(1, "Kamal", [80, 90])

        average = self.service.calculate_average(1)

        self.assertEqual(average, 85)

    def test_reject_duplicate_student_id(self):
        self.service.add_student(1, "Kamal", [80])

        with self.assertRaises(ValueError):
            self.service.add_student(1, "Nimal", [90])

    def test_reject_empty_name(self):
        with self.assertRaises(ValueError):
            self.service.add_student(1, "  ", [80])

    def test_reject_invalid_marks(self):
        with self.assertRaises(ValueError):
            self.service.add_student(1, "Kamal", [120])


if __name__ == "__main__":
    unittest.main()
