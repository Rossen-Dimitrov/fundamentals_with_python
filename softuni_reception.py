employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
num_students = int(input())
answer_capacity = employee_1 + employee_2 + employee_3
hour = 0

while num_students > 0:
    num_students -= answer_capacity
    hour += 1
    if hour % 4 == 0:
        hour += 1

print(f'Time needed: {hour}h.')