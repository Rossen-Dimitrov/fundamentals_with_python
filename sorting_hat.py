def sorting_hat(name):
    if len(name) < 5:
        return "Gryffindor"
    elif len(name) == 5:
        return "Slytherin"
    elif len(name) == 6:
        return "Ravenclaw"
    elif len(name) > 6:
        return "Hufflepuff"


while True:
    student_name = str(input())
    if student_name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif student_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    else:
        print(f"{student_name} goes to {sorting_hat(student_name)}.")
