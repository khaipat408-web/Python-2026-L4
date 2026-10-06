import os
import zipfile

DATA_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def compress_files():
    with zipfile.ZipFile(DATA_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in TXT_FILES:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Đã nén file: {file}")

def load_data_on_startup():
    if os.path.exists(DATA_FILE):
        with zipfile.ZipFile(DATA_FILE, "r") as zipf:
            zipf.extractall()
        print("Đã giải nén dữ liệu từ students.dat!")
    else:
        print("Chưa có students.dat, tạo dữ liệu mới.")

def input_students():
    students = []
    n = int(input("Nhập số lượng sinh viên: "))
    
    with open("students.txt", "w", encoding="utf-8") as f:
        for _ in range(n):
            student_id = input("ID sinh viên: ")
            name = input("Tên sinh viên: ")
            dob = input("Ngày sinh (DD/MM/YYYY): ")
            f.write(f"{student_id},{name},{dob}\n")
            students.append({'id': student_id, 'name': name, 'dob': dob})
    print("-> Đã tạo students.txt")
    return students

def input_courses():
    courses = []
    n = int(input("Nhập số lượng khóa học: "))
    
    with open("courses.txt", "w", encoding="utf-8") as f:
        for _ in range(n):
            course_id = input("ID khóa học: ")
            title = input("Tên khóa học: ")
            f.write(f"{course_id},{title}\n")
            courses.append({'id': course_id, 'title': title})
    print("-> Đã tạo courses.txt")
    return courses

def input_marks(students, courses):
    if not students or not courses:
        return
        
    course_id = input("Nhập ID khóa học cần nhập điểm: ")
    
    with open("marks.txt", "a", encoding="utf-8") as f:
        for student in students:
            mark = float(input(f"Nhập điểm cho sinh viên {student['name']} ({student['id']}): "))
            f.write(f"{student['id']},{course_id},{mark}\n")
    print("-> Đã tạo marks.txt")

def main():
    load_data_on_startup()

    students = input_students()
    courses = input_courses()
    input_marks(students, courses)

    compress_files()

if __name__ == "__main__":
    main()