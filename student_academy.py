class_book = {}
n_students = int(input())
for _ in range(n_students):
    student = str(input())
    grade = float(input())
    if student not in class_book:
        class_book[student] = [0.0, 0]
    class_book[student][0] += grade
    class_book[student][1] += 1

for student, grades in class_book.items():
    if grades[0] / grades[1] >= 4.5:
        print(f"{student} -> {grades[0] / grades[1]:.2f}")
