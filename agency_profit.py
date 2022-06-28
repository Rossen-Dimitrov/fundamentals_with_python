aviocompany = str(input())
adult_tickets = int(input())
child_tickets = int(input())
ticket_price = float(input())
taxes = float(input())

child_ticket_price = 0.3 * ticket_price
taxes = (adult_tickets + child_tickets) * taxes
total = (adult_tickets * ticket_price + child_tickets * child_ticket_price + taxes) * 0.2


print(f"The profit of your agency from {aviocompany} tickets is {total:.2f} lv.")