def calculate_bonus(salary):
    if salary > 100000:
        bonus = salary * 0.20
    else:
        bonus = salary * 0.10
    return bonus

bonus_amount = calculate_bonus(50000)
print("Bonus amount:", bonus_amount)
#Bonus amount: 5000.0


def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return average

avg = calculate_average([10, 20, 30])
print("Average:", avg)
#Bonus amount: 5000.0
#Average: 20.0


num = int(input("How many salaries: "))
salaries = []
for i in range(num):
    salary = int(input(f"Enter salary {i+1}: "))
    salaries.append(salary)
def calculated_bonus(salary):
    if salary > 100000:
        bonus = salary * 0.20
    else:
        bonus = salary * 0.10
    return bonus
for salary in salaries:
    bonus = calculated_bonus(salary)
    print(f"Salary: {salary}, Bonus: {bonus}")