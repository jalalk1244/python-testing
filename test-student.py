import unittest
from datetime import timedelta
from student import Student
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    def setUp(self):
        self.student = Student('John', 'Doe')

    # def tearDown(self):
    #     print('tearDown')

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_apply_extension(self):
        before_end_date = self.student.end_date
        self.student.apply_extension(10)

        # My solution to the challenge
        # self.assertGreater(self.student.end_date, before_end_date)
        # Video's solution to the challenge
        self.assertEqual(
            before_end_date + timedelta(days=10), self.student.end_date)

    def test_course_schedule_success(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Success')

    def test_course_schedule_failed(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Somthing went wrong with the request!')


if __name__ == '__main__':
    unittest.main()
