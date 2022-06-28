judges_num = int(input())
command = str(input())
total_grade = 0
grade_counter = 0
while command != "Finish":
    presentation_name = command
    grade = 0
    for j in range(judges_num):
        grade_1 = float(input())
        grade += grade_1
        grade_counter += 1
    print(f"{presentation_name} - {grade / judges_num:.2f}.")
    total_grade += grade
    command = input()
print(f"Student's final assessment is {total_grade/grade_counter:.2f}.")

