import curses
from domain.student import Student
from domain.course import Course

def input_string(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(1, 2, prompt)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(2, 2).decode('utf-8')
    curses.noecho()
    return val

def input_students(stdscr, students_list):
    count = int(input_string(stdscr, "Nhập số lượng sinh viên trong lớp: "))
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

        students_list.append(Student(s_id, s_name, s_dob))

def input_courses(stdscr, courses_dict):
    count = int(input_string(stdscr, "Nhập số lượng môn học: "))
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

        courses_dict[c_id] = Course(c_id, c_name, c_credits)

def input_marks(stdscr, students_list, courses_dict):
    if not courses_dict or not students_list:
        stdscr.clear()
        stdscr.addstr(2, 2, "Cần nhập thông tin sinh viên và môn học trước!")
        stdscr.addstr(4, 2, "Nhấn phím bất kỳ để quay lại...")
        stdscr.getch()
        return

    c_id = input_string(stdscr, "Nhập ID môn học cần nhập điểm: ")
    if c_id not in courses_dict:
        stdscr.clear()
        stdscr.addstr(2, 2, "Môn học không tồn tại!")
        stdscr.addstr(4, 2, "Nhấn phím bất kỳ để quay lại...")
        stdscr.getch()
        return

    stdscr.clear()
    stdscr.addstr(1, 2, f"--- Nhập điểm cho môn: {courses_dict[c_id].get_name()} ---")
    line = 3
    curses.echo()
    for student in students_list:
        stdscr.addstr(line, 2, f"Điểm cho {student.get_name()} ({student.get_id()}): ")
        mark = float(stdscr.getstr(line, 45).decode('utf-8'))
        student.set_mark(c_id, mark)
        line += 1
    curses.noecho()