employees = []
num = int(input("How many employees: "))

for i in range(num):
    name = input(f"Enter employee name {i+1}: ")
    company = input(f"Enter company name {i+1}: ")
    salary = int(input(f"Enter salary {i+1}: "))
    employee = {
        "name": name,
        "company": company,
        "salary": salary
    }
    employees.append(employee)
print(employees)
print(max(employees, key=lambda x: x["salary"]))
print(sum(employee["salary"] for employee in employees) / len(employees))