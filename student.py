from datetime import date, timedelta
import requests


class Student:
    """ A Student class as a basis for method testing """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
        self.dot = '.'

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f'{self._first_name}.{self._last_name}@email.com'.lower()

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)

    def course_schedule(self):
        response = requests.get(f'http://company.com/course-schedule/{self._first_name}/{self._last_name}')

        if response.ok:
            return response.text
        else:
            return 'Somthing went wrong with the request!'
