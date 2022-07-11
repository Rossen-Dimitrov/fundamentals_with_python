data_input = input()
company_employees = {}

while not data_input == "End":
    data_input = data_input.split(" -> ")
    company = data_input[0]
    id_comp = data_input[1]
    if company not in company_employees:
        company_employees[company] = []
    if id_comp not in company_employees[company]:
        company_employees[company].append(id_comp)

    data_input = input()

for company, employee in company_employees.items():
    print(company)
    for name in employee:
        print(f"-- {name}")
