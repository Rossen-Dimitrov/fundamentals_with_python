class Party:
    def __init__(self):
        self.people = []


my_party = Party()
people_input = input()
while not people_input == "End":
    my_party.people.append(people_input)
    people_input = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
