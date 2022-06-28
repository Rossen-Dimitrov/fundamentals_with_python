name = str(input())
year_counter = 0
average = 0
bad_grade = 0
condition = True
while year_counter < 12:
    grade = float(input())
    if grade < 4:
        bad_grade += 1
        if bad_grade > 1:
            condition = False
            year_counter += 1
            break
    else:
        year_counter += 1
        average += grade
average /= year_counter
if condition:
    print(f"{name} graduated. Average grade: {average:.2f}")
else:
    print(f"{name} has been excluded at {year_counter} grade")