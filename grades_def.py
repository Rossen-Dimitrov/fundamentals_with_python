def grade_task():
    grade_input = float(input())
    if grade_input < 3:
        return "Fail"
    elif grade_input < 3.5:
        return "Poor"
    elif grade_input < 4.5:
        return "Good"
    elif grade_input < 5.5:
        return "Very Good"
    else:
        return "Excellent"


print(grade_task())
