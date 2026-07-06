city = "London"

print(city.upper())
print(city.lower())
print(len(city))

languages = ["Python", "Java", "SQL"]

print(languages)

languages.append("Scala")

print(languages)

languages.remove("Java")

print(languages)


numbers = [10,20,30,40,50]

for number in numbers:
    print(number*2)


customers = [
    "aditi",
    "rahul",
    "priya",
    "aman"
]
for customer in customers:
    print(customer.capitalize())


companies = [
    "Mastercard",
    "Citadel",
    "Google",
    "Netflix"
]
for company in companies:
    print(company)


num = int(input("How many salaries? "))

salaries = []

for i in range(num):
    salary = int(input(f"Enter salary {i+1}: "))
    salaries.append(salary)

print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", sum(salaries)/len(salaries))



numbers = [4,8,15,16,23,42]

for number in numbers:
    if number % 2 == 0:
        print(number)