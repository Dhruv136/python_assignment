# <<<<<<<<<<<<<<<<< QUESTION 1 >>>>>>>>>>>>>>>>>

numbers = [2, 5, 8, 11, 15, 17, 20, 23]

for num in numbers:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)


# <<<<<<<<<<<<<<<<< QUESTION 2 >>>>>>>>>>>>>>>>>

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()


# <<<<<<<<<<<<<<<<< QUESTION 3 >>>>>>>>>>>>>>>>>

def calculate(numbers):
    even_count = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num

    return even_count, odd_sum

numbers = [1, 2, 3, 4, 5, 6]

even, odd = calculate(numbers)

print("Even Count =", even)
print("Odd Sum =", odd)


# <<<<<<<<<<<<<<<<< QUESTION 4 >>>>>>>>>>>>>>>>>

def simple_interest(p, r=5, t=2):
    si = (p * r * t) / 100
    return si

print(simple_interest(1000))
print(simple_interest(1000, 10, 3))
print(simple_interest(p=1000, r=8, t=4))


# <<<<<<<<<<<<<<<<< QUESTION 5 AND 6 >>>>>>>>>>>>>>>>>

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

s1 = Student("Rahul", 92)
s2 = Student("Amit", 68)

print(s1.name, "-", s1.grade())
print(s2.name, "-", s2.grade())


# <<<<<<<<<<<<<<<<< QUESTION 7 >>>>>>>>>>>>>>>>>

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance =", self.__balance)

acc = BankAccount(5000)

acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()


# <<<<<<<<<<<<<<<<< QUESTION 8 >>>>>>>>>>>>>>>>>

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")


# <<<<<<<<<<<<<<<<< QUESTION 9 >>>>>>>>>>>>>>>>>

file = open("student.txt", "w")

file.write("Rahul 85\n")
file.write("Amit 90\n")

file.close()

file = open("student.txt", "r")

print(file.read())

file.close()


# <<<<<<<<<<<<<<<<< QUESTION 10 >>>>>>>>>>>>>>>>>

try:
    file = open("numbers.txt", "r")

    total = 0
    count = 0

    for line in file:
        total += int(line)
        count += 1

    average = total / count

    print("Total =", total)
    print("Average =", average)

    file.close()

except FileNotFoundError:
    print("File does not exist")