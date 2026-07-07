book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 500
}
print("Title:", book["title"])
print("Author:", book["author"])

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
print("\nAll Employees")
for employee in employees:
    print(employee)

highest_salary = 0
for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
print("\nHighest Salary:", highest_salary)

total_salary = 0
for employee in employees:
    total_salary += employee["salary"]
average_salary = total_salary / len(employees)
print("Average Salary:", average_salary)