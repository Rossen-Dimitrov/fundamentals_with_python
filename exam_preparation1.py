bad_grades = int(input())
bad_grades_counter = 0
grade_counter = 0
average = 0
last_problem = ""

while True:
    task_name = str(input())
    if task_name == "Enough":
        average /= grade_counter
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {grade_counter}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    grade_counter += 1
    average += grade
    last_problem = task_name
    if grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades:
            print(f"You need a break, {bad_grades} poor grades.")
            break
