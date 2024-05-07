# Fungsi untuk menampilkan data nilai ujian dalam bentuk tabel
def display_grades(grades, students, subjects):
    print("Data Nilai Ujian:")
    # Header kolom
    print("{:<10}".format("Mahasiswa"), end="")
    for subject in subjects:
        print("{:<10}".format(subject), end="")
    print()

    # Menampilkan nilai ujian
    for i in range(len(grades)):
        print("{:<10}".format(students[i]), end="")
        for j in range(len(grades[i])):
            print("{:<10}".format(grades[i][j]), end="")
        print()

# Fungsi untuk menghitung rata-rata nilai ujian dari setiap mahasiswa
def average_grades(grades, students):
    print("Rata-rata Nilai Ujian:")
    for i in range(len(grades)):
        total = sum(grades[i])
        average = total / len(grades[i])
        print("Rata-rata nilai ujian untuk Mahasiswa", students[i], ":", "{:.2f}".format(average))

# Fungsi untuk menentukan nilai tertinggi dan terendah dari setiap mata kuliah
def min_max_grades(grades, students, subjects):
    print("Nilai Tertinggi dan Terendah dari Setiap Mata Kuliah:")
    for i in range(len(grades[0])):
        max_grade = grades[0][i]
        min_grade = grades[0][i]
        max_student = students[0]
        min_student = students[0]

        for j in range(1, len(grades)):
            if grades[j][i] > max_grade:
                max_grade = grades[j][i]
                max_student = students[j]
            if grades[j][i] < min_grade:
                min_grade = grades[j][i]
                min_student = students[j]
        print("Mata Kuliah", subjects[i])
        print("Nilai tertinggi:", max_grade, "oleh Mahasiswa", max_student)
        print("Nilai terendah:", min_grade, "oleh Mahasiswa", min_student)

if __name__ == "__main__":
    # Input data nilai ujian, nama mahasiswa, dan nama mata kuliah
    grades = []
    students = []
    subjects = []

    num_students = int(input("Masukkan jumlah mahasiswa: "))
    num_subjects = int(input("Masukkan jumlah mata kuliah: "))

    # Input nama mahasiswa
    for i in range(num_students):
        name = input("Masukkan nama mahasiswa ke-{}: ".format(i+1))
        students.append(name)

    # Input nama mata kuliah
    for i in range(num_subjects):
        subject = input("Masukkan nama mata kuliah ke-{}: ".format(i+1))
        subjects.append(subject)

    # Input nilai ujian
    print("Masukkan nilai ujian:")
    for i in range(num_students):
        print("Masukkan nilai ujian untuk mahasiswa", students[i], ":")
        student_grades = []
        for j in range(num_subjects):
            grade = int(input("Nilai ujian {}: ".format(subjects[j])))
            student_grades.append(grade)
        grades.append(student_grades)

    # 1. Menampilkan data nilai ujian dalam bentuk tabel
    display_grades(grades, students, subjects)
    print()

    # 2. Menghitung rata-rata nilai ujian dari setiap mahasiswa
    average_grades(grades, students)
    print()

    # 3. Menentukan nilai tertinggi dan terendah dari setiap mata kuliah
    min_max_grades(grades, students, subjects)



