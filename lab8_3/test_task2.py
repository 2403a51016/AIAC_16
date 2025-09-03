import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_assign_grade_A(self):
        self.assertEqual(assign_grade(95), 'A')
        self.assertEqual(assign_grade(90), 'A')

    def test_assign_grade_B(self):
        self.assertEqual(assign_grade(89.9), 'B')
        self.assertEqual(assign_grade(80), 'B')

    def test_assign_grade_C(self):
        self.assertEqual(assign_grade(79.9), 'C')
        self.assertEqual(assign_grade(70), 'C')

    def test_assign_grade_D(self):
        self.assertEqual(assign_grade(69.9), 'D')
        self.assertEqual(assign_grade(60), 'D')

    def test_assign_grade_F(self):
        self.assertEqual(assign_grade(59.9), 'F')
        self.assertEqual(assign_grade(0), 'F')

    def test_assign_grade_invalid_type(self):
        with self.assertRaises(TypeError):
            assign_grade("90")
        with self.assertRaises(TypeError):
            assign_grade([90])

    def test_assign_grade_out_of_range(self):
        with self.assertRaises(ValueError):
            assign_grade(-1)
        with self.assertRaises(ValueError):
            assign_grade(101)

if __name__ == '__main__':
    unittest.main()