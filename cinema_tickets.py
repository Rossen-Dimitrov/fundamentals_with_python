total_ticket = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
command = str(input())
while command != "Finish":
    movie_name = command
    free_places = int(input())
    places = free_places
    current_total_tickets = 0
    while free_places > 0:
        ticket_type = str(input())
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        current_total_tickets += 1
        total_ticket += 1
        free_places -= 1
    print(f"{movie_name} - {current_total_tickets / places * 100:.2f}% full.")
    command = str(input())
print(f"Total tickets: {total_ticket}")
print(f"{student_tickets / total_ticket * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_ticket * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_ticket * 100:.2f}% kids tickets.")
