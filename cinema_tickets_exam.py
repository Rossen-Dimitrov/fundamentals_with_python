student_counters = 0
standard_counters = 0
kid_counters = 0
while True:
    user_input = input()
    if user_input == "Finish":
        break
    capacity = int(input())
    sold_tickets = 0
    while sold_tickets < capacity:
        ticket_type = input()
        if ticket_type == "End":
            break
        sold_tickets += 1
        if ticket_type == "student":
            student_counters += 1
        elif ticket_type == "standard":
            standard_counters +=1
        elif ticket_type == "kid":
            kid_counters += 1
    print(f"{user_input} - {(sold_tickets / capacity) * 100:.2f}% full.")
total_tickets = student_counters + standard_counters + kid_counters
print(f"Total tickets: {total_tickets}")
print(f"{(student_counters / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_counters / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_counters / total_tickets) * 100:.2f}% kids tickets.")
