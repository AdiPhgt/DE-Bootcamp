print(20 + 5)

print(20 - 5)

print(20 * 5)

print(20 / 5)

print(20 // 3)

print(20 % 3)

print(2 ** 5)

name = input("Type your name: ")
age = input("Type your age: ")
salary = input("Type your salary: ")
age = int(age)
salary = int(salary)
if age >= 18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')
if salary >= 100000:
    print('High salary')
else:
    print('Keep growing!')


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
print("Addition:", number_1 + number_2)
print("Subtraction:", number_1 - number_2)
print("Multiplication:", number_1 * number_2)
print("Division:", number_1 / number_2)