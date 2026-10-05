import math
import numpy as np
import curses

class Person:
    def __init__(self, person_id, name, dob):
        self._id = person_id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob


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


class Course:
    def __init__(self, course_id, name, credits_num):
        self._id = course_id
        self._name = name
        self._credits = credits_num

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits


class StudentManagementApp:
    def __init__(self):
        self._students = []
        self._courses = {}  # {course_id: Course}

    def input_string(self, stdscr, prompt):
        stdscr.clear()
        stdscr.addstr(1, 2, prompt)
        stdscr.refresh()
        curses.echo()
        val = stdscr.getstr(2, 2).decode('utf-8')
        curses.noecho()
        return val

    def input_number_students(self, stdscr):
        count = int(self.input_string(stdscr, "Nhập số lượng sinh viên trong lớp: "))
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(1, 2, f"--- Nhập thông tin sinh viên thứ {i + 1} ---")
            stdscr.addstr(3, 2, "ID sinh viên: ")
            curses.echo()
            s_id = stdscr.getstr(3, 16).decode('utf-8')
            stdscr.addstr(4, 2, "Họ và tên: ")
            s_name = stdscr.getstr(4, 13).decode('utf-8')
            stdscr.addstr(5, 2, "Ngày sinh (DD/MM/YYYY): ")
            s_dob = stdscr.getstr(5, 25).decode('utf-8')
            curses.noecho()

            self._students.append(Student(s_id, s_name, s_dob))

    def input_number_courses(self, stdscr):
        count = int(self.input_string(stdscr, "Nhập số lượng môn học: "))
        for i in range(count):
            stdscr.clear()
            stdscr.addstr(1, 2, f"--- Nhập thông tin môn học thứ {i + 1} ---")
            stdscr.addstr(3, 2, "ID môn học: ")
            curses.echo()
            c_id = stdscr.getstr(3, 14).decode('utf-8')
            stdscr.addstr(4, 2, "Tên môn học: ")
            c_name = stdscr.getstr(4, 15).decode('utf-8')
            stdscr.addstr(5, 2, "Số tín chỉ: ")
            c_credits = float(stdscr.getstr(5, 14).decode('utf-8'))
            curses.noecho()

            self._courses[c_id] = Course(c_id, c_name, c_credits)

    def input_marks(self, stdscr):
        if not self._courses or not self._students:
            stdscr.clear()
            stdscr.addstr(2, 2, "Cần nhập thông tin sinh viên và môn học trước!")
            stdscr.addstr(4, 2, "Nhấn phím bất kỳ để quay lại...")
            stdscr.getch()
            return

        c_id = self.input_string(stdscr, "Nhập ID môn học cần nhập điểm: ")
        if c_id not in self._courses:
            stdscr.clear()
            stdscr.addstr(2, 2, "Môn học không tồn tại!")
            stdscr.addstr(4, 2, "Nhấn phím bất kỳ để quay lại...")
            stdscr.getch()
            return

        stdscr.clear()
        stdscr.addstr(1, 2, f"--- Nhập điểm cho môn: {self._courses[c_id].get_name()} ---")
        line = 3
        curses.echo()
        for student in self._students:
            stdscr.addstr(line, 2, f"Điểm cho {student.get_name()} ({student.get_id()}): ")
            mark = float(stdscr.getstr(line, 45).decode('utf-8'))
            student.set_mark(c_id, mark)
            line += 1
        curses.noecho()

    def update_gpa_and_sort(self):
        for student in self._students:
            student.calculate_gpa(self._courses)
        
        # Sắp xếp danh sách sinh viên theo GPA giảm dần bằng NumPy argsort
        if self._students:
            gpa_list = [s.get_gpa() for s in self._students]
            gpa_arr = np.array(gpa_list)
            sorted_indices = np.argsort(-gpa_arr)  # Dấu trừ để sắp xếp giảm dần
            self._students = [self._students[i] for i in sorted_indices]

    def display_students(self, stdscr):
        self.update_gpa_and_sort()
        stdscr.clear()
        stdscr.addstr(1, 2, "================ DANH SÁCH SINH VIÊN (SẮP XẾP THEO GPA GIẢM DẦN) ================")
        stdscr.addstr(3, 2, f"{'ID':<10} | {'Họ tên':<20} | {'Ngày sinh':<12} | {'GPA':<5}")
        stdscr.addstr(4, 2, "-" * 60)

        line = 5
        for s in self._students:
            stdscr.addstr(line, 2, f"{s.get_id():<10} | {s.get_name():<20} | {s.get_dob():<12} | {s.get_gpa():<5.2f}")
            line += 1

        stdscr.addstr(line + 1, 2, "Nhấn phím bất kỳ để tiếp tục...")
        stdscr.getch()

    def display_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(1, 2, "================ DANH SÁCH MÔN HỌC ================")
        stdscr.addstr(3, 2, f"{'ID':<10} | {'Tên môn':<25} | {'Số tín chỉ':<10}")
        stdscr.addstr(4, 2, "-" * 50)

        line = 5
        for c_id, c in self._courses.items():
            stdscr.addstr(line, 2, f"{c.get_id():<10} | {c.get_name():<25} | {c.get_credits():<10}")
            line += 1

        stdscr.addstr(line + 1, 2, "Nhấn phím bất kỳ để tiếp tục...")
        stdscr.getch()

    def run(self, stdscr):
        curses.curs_set(0)
        
        # Khởi tạo dữ liệu ban đầu
        self.input_number_students(stdscr)
        self.input_number_courses(stdscr)

        # Curses Menu Loop
        menu_items = [
            "1. Nhập điểm môn học",
            "2. Xem danh sách môn học",
            "3. Xem danh sách sinh viên & GPA (Đã sắp xếp)",
            "0. Thoát"
        ]
        
        current_row = 0

        while True:
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            stdscr.addstr(1, 2, "================ QUẢN LÝ SINH VIÊN & ĐIỂM (CURSES UI) ================")

            for idx, item in enumerate(menu_items):
                x = 4
                y = 3 + idx
                if idx == current_row:
                    stdscr.attron(curses.A_REVERSE)
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.A_REVERSE)
                else:
                    stdscr.addstr(y, x, item)

            stdscr.refresh()
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
                current_row += 1
            elif key in [curses.KEY_ENTER, 10, 13]:
                if current_row == 0:
                    self.input_marks(stdscr)
                elif current_row == 1:
                    self.display_courses(stdscr)
                elif current_row == 2:
                    self.display_students(stdscr)
                elif current_row == 3:
                    break


def main(stdscr):
    app = StudentManagementApp()
    app.run(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)