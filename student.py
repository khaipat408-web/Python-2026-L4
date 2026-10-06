import math
import numpy as np
from .person import Person

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)
        self._marks = {}
        self._gpa = 0.0

    def set_mark(self, course_id, mark):
        self._marks[course_id] = math.floor(mark * 10) / 10

    def get_marks(self):
        return self._marks

    def get_gpa(self):
        return self._gpa

    def calculate_gpa(self, courses_dict):
        student_marks = []
        credits_list = []

        for course_id, mark in self._marks.items():
            if course_id in courses_dict:
                student_marks.append(mark)
                credits_list.append(courses_dict[course_id].get_credits())

        if not credits_list or sum(credits_list) == 0:
            self._gpa = 0.0
            return 0.0

        marks_arr = np.array(student_marks)
        credits_arr = np.array(credits_list)

        self._gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
        self._gpa = math.floor(self._gpa * 100) / 100
        return self._gpa