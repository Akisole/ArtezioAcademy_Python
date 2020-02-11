"""Module of Student"""


class Student:
    """Class of Student"""

    def __init__(self, name: str, course: dict):
        self.name = name
        self.exam_max = course.get('exam_max')
        self.lab_max = course.get('lab_max')
        self.lab_num = course.get('lab_num')
        self.k = course.get('k')

        self.marks = {}
        self.attempts = {}
        self.max_points = self.exam_max
        for i in range(self.lab_num):
            self.marks.setdefault(i, 0)
            self.attempts.setdefault(i, 3)
            self.max_points += self.lab_max
        self.marks.setdefault('exam', 0)

    def make_lab(self, mark, num):
        """Accept laboratory work"""
        if self.attempts[num] > 0:
            self.attempts[num] -= 1

            tmp_m = mark
            if mark > self.lab_max:
                tmp_m = self.lab_max

            self.marks[num] = tmp_m

        return self

    def make_exam(self, mark):
        """Accept exam"""

        tmp_m = mark
        if mark > self.exam_max:
            tmp_m = self.exam_max

        self.marks['exam'] = tmp_m

        return self

    def is_certified(self):
        """Certification of student"""

        points = self.marks['exam']
        for i in range(self.lab_num):
            points += self.marks[i]

        certified = False
        if points >= self.max_points*self.k:
            certified = True

        result = (points, certified)

        return result
