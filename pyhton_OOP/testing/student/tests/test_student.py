from unittest import TestCase, main
# from pyhton_OOP.testing.student.project.student import Student
from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Mimi", {"Math": ["2"]})
        self.student2 = Student("Meri", None)

    def test_initialization_correct(self):
        self.assertEqual("Mimi", self.student.name)
        self.assertEqual({"Math": ["2"]}, self.student.courses)
        self.assertEqual({}, self.student2.courses)

    def test_if_course_already_added(self):
        expected = "Course already added. Notes have been updated."
        actual = self.student.enroll("Math", "2")
        self.assertEqual(expected, actual)

    def test_if_course_and_notes_have_been_added(self):
        expected = "Course and course notes have been added."
        actual = self.student2.enroll("Chemistry", "1", "Y")
        self.assertEqual(expected, actual)

    def test_if_course_and_notes_have_been_added_with_no_course_notes(self):
        expected = "Course and course notes have been added."
        actual = self.student2.enroll("Chemistry", "1")
        self.assertEqual(expected, actual)

    def test_if_course_has_been_added(self):
        expected = "Course has been added."
        actual = self.student2.enroll("English", "5", "No")
        self.assertEqual(expected, actual)
        self.assertEqual([], self.student2.courses["English"])

    def test_add_notes_correct(self):
        expected = "Notes have been updated"
        actual = self.student.add_notes("Math", "some_note")
        self.assertEqual(expected, actual)

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("Math", "some_notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_removes(self):
        expected = "Course has been removed"
        actual = self.student.leave_course("Math")
        self.assertEqual(expected, actual)

    def test_leave_course_raises_an_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()