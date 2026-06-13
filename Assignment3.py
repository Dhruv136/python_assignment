
# <<<<<<< Question 1 >>>>>>>>

class Student:
    name = "DHruv"
    age = 20
    course = "BTECH"

s1 = Student()

print("Name:", s1.name)
print("Age:", s1.age)
print("Course:", s1.course)
# <<<<<<< Question 2 >>>>>>>>

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

c1 = Car("Maruti", "Swift", 700000)
c2 = Car("Hyundai", "i20", 900000)

print(c1.brand, c1.model, c1.price)
print(c2.brand, c2.model, c2.price)
# <<<<<<< Question 3 >>>>>>>>

class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

e1 = Employee(101, "Amit", 50000)

print(e1.employee_id)
print(e1.name)
print(e1.salary)
# <<<<<<< Question 4 >>>>>>>>

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

r1 = Rectangle(10, 5)
r1.area()
# <<<<<<< Question 5 >>>>>>>>

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14 * self.radius * self.radius)

c1 = Circle(7)
c1.area()
# <<<<<<< Question 6 >>>>>>>>

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance =", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Balance =", self.balance)

b1 = BankAccount("Rohan", 10000)

b1.deposit(2000)
b1.withdraw(1500)
# <<<<<<< Question 7 >>>>>>>>

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d1 = Dog()
d1.sound()
# <<<<<<< Question 8 >>>>>>>>

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

s1 = Student("Vikas", 20, 15)

print(s1.name)
print(s1.age)
print(s1.roll_number)
# <<<<<<< Question 9 >>>>>>>>

class Calculator:
    def add(self, a, b):
        print("Add =", a + b)

    def subtract(self, a, b):
        print("Subtract =", a - b)

    def multiply(self, a, b):
        print("Multiply =", a * b)

    def divide(self, a, b):
        print("Divide =", a / b)

n1 = 20
n2 = 5

c1 = Calculator()

c1.add(n1, n2)
c1.subtract(n1, n2)
c1.multiply(n1, n2)
c1.divide(n1, n2)
# <<<<<<< Question 10 >>>>>>>>

class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print(self.book_name, self.author, self.price)

b1 = LibraryBook("Python", "Ramesh", 450)
b2 = LibraryBook("Java", "Suresh", 550)
b3 = LibraryBook("C++", "Mahesh", 500)

b1.display_book_info()
b2.display_book_info()
b3.display_book_info()
