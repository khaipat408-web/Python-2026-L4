import curses
import numpy as np

def update_gpa_and_sort(students_list, courses_dict):
    for student in students_list:
        student.calculate_gpa(courses_dict)
    
    if students_list:
        gpa_list = [s.get_gpa() for s in students_list]
        gpa_arr = np.array(gpa_list)
        sorted_indices = np.argsort(-gpa_arr)
        return [students_list[i] for i in sorted_indices]
    return students_list

def display_students(stdscr, students_list, courses_dict):
    sorted_students = update_gpa_and_sort(students_list, courses_dict)
    stdscr.clear()
    stdscr.addstr(1, 2, "================ DANH SÁCH SINH VIÊN (SẮP XẾP THEO GPA GIẢM DẦN) ================")
    stdscr.addstr(3, 2, f"{'ID':<10} | {'Họ tên':<20} | {'Ngày sinh':<12} | {'GPA':<5}")
    stdscr.addstr(4, 2, "-" * 60)

    line = 5
    for s in sorted_students:
        stdscr.addstr(line, 2, f"{s.get_id():<10} | {s.get_name():<20} | {s.get_dob():<12} | {s.get_gpa():<5.2f}")
        line += 1

    stdscr.addstr(line + 1, 2, "Nhấn phím bất kỳ để tiếp tục...")
    stdscr.getch()

def display_courses(stdscr, courses_dict):
    stdscr.clear()
    stdscr.addstr(1, 2, "================ DANH SÁCH MÔN HỌC ================")
    stdscr.addstr(3, 2, f"{'ID':<10} | {'Tên môn':<25} | {'Số tín chỉ':<10}")
    stdscr.addstr(4, 2, "-" * 50)

    line = 5
    for c_id, c in courses_dict.items():
        stdscr.addstr(line, 2, f"{c.get_id():<10} | {c.get_name():<25} | {c.get_credits():<10}")
        line += 1

    stdscr.addstr(line + 1, 2, "Nhấn phím bất kỳ để tiếp tục...")
    stdscr.getch()