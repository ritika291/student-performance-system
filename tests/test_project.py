import unittest
from marks import calculate_grade, calculate_percentage, get_result


class TestStudentPerformanceSystem(unittest.TestCase):

    def test_grade_A_plus(self):
        self.assertEqual(calculate_grade(95), "A+")

    def test_grade_A(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(40), "F")

    def test_percentage(self):
        self.assertEqual(calculate_percentage(80, 100), 80)

    def test_pass_result(self):
        self.assertEqual(get_result(75), "Pass")

    def test_fail_result(self):
        self.assertEqual(get_result(30), "Fail")


if __name__ == "__main__":
    unittest.main()
