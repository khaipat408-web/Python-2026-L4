import curses
import input as in_mod
import output as out_mod

students = []
courses = {}

def main_app(stdscr):
    curses.curs_set(0)
    
    in_mod.input_students(stdscr, students)
    in_mod.input_courses(stdscr, courses)

    menu_items = [
        "1. Nhập điểm môn học",
        "2. Xem danh sách môn học",
        "3. Xem danh sách sinh viên & GPA (Đã sắp xếp)",
        "0. Thoát"
    ]
    
    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(1, 2, "================ QUẢN LÝ SINH VIÊN (PW4 MODULES) ================")

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
                in_mod.input_marks(stdscr, students, courses)
            elif current_row == 1:
                out_mod.display_courses(stdscr, courses)
            elif current_row == 2:
                out_mod.display_students(stdscr, students, courses)
            elif current_row == 3:
                break

if __name__ == "__main__":
    curses.wrapper(main_app)