from unittest import TestCase, main
from project.student_report_card import StudentReportCard
# from area_test.project.student_report_card import StudentReportCard
# ------------------------ score 83 ---------------------------------

class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Mimi", 2)

    def test_successful_year(self):
        self.student.school_year = 1
        self.assertEqual(1, self.student.school_year)

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.student.student_name)
        self.assertEqual(2, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_name_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_correct(self):
        expected = [2]
        self.student.add_grade("Math", 2)
        self.assertEqual(expected, self.student.grades_by_subject["Math"])

    def test_average_grade_by_subject_correct(self):
        self.student.add_grade("Math", 6.00)
        self.student.add_grade("Bio", 6.00)
        self.student.add_grade("Gym", 6.00)
        self.assertEqual([6.00], self.student.grades_by_subject["Math"])
        self.assertEqual([6.00], self.student.grades_by_subject["Bio"])
        self.assertEqual([6.00], self.student.grades_by_subject["Gym"])
        self.assertEqual(1, len(self.student.grades_by_subject["Math"]))
        self.assertEqual("Math: 6.00\n"
                         "Bio: 6.00\n"
                         "Gym: 6.00", self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade("Math", 6.00)
        self.student.add_grade("Bio", 6.00)
        actual = self.student.average_grade_for_all_subjects()
        expected = "Average Grade: 6.00"
        self.assertEqual(expected, actual)
        self.assertEqual([6.00], self.student.grades_by_subject["Math"])
        self.assertEqual([6.00], self.student.grades_by_subject["Bio"])
        self.assertEqual(1, len(self.student.grades_by_subject["Math"]))

    def test_repr_correct(self):
        self.student.grades_by_subject = {"math": [2, 4, 6]}
        expected = "Name: Mimi\n" \
                   "Year: 2\n" \
                   "----------\n" \
                   "math: 4.00\n" \
                   "----------\n" \
                   "Average Grade: 4.00"
        self.assertEqual(expected, self.student.__repr__())


if __name__ == "__main__":
    main()
