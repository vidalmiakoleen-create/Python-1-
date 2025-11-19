#-----Inheritance-------
#---Part 2

class Animal:
    def speak(self, speak):
        print("their sounds")

class Dog(Animal):
    def speak(self):
        print("Wooooof wooff wooff woooff")

class Cat(Animal):
    def speak(self):
        print("Meoowww!")

Dog().speak()
Cat().speak()

#------Part 2-----


class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def __init__(self, brand, fuel, doors):
        # Call the parent class constructor
        Vehicle.__init__(self, brand, fuel)
        self.doors = doors

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 1
            print(f"The {self.brand} car is driving... Fuel left: {self.fuel}")
        else:
            print(f"The {self.brand} car has no fuel left!")

my_car = Car("Tesla", 5, 4)
my_car.drive()
my_car.drive()
my_car.drive()

#--------ENCAPSULATION-------

#-----------Part 1

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private variable
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.owner} deposited Php {amount}. New balance: Php {self.__balance}")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.owner} withdrew Php {amount}. Remaining balance: Php {self.__balance}")
        else:
            print("Insufficient funds!")
            

    def get_balance(self):
        return self.__balance


amount1 = BankAccount("Mia", 100000)
amount1.deposit(1500)
amount1.withdraw(2000)
amount1.withdraw(100001)


print(f"Final balance: Php {amount1.get_balance()}")


#------Part 2

class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age must be a positive integer")

p = Person()
p.age = 19
print(p.age)


#-------Polymorphism

#----Part 1

class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for p in printers:
    print(p.print_document())

#-----Part 2

def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Tweett tweett!")

class Robot:
    def speak(self):
        print("Beepp boop!")

make_it_speak(Bird())
make_it_speak(Robot())

#-----------Abstract---------

#----Part 1

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(7)
rect = Rectangle(5, 7)
print("Circle Area:", circle.area())
print("Rectangle Area:", rect.area())


#-----Part 2
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        return self.rate * self.hours

class SalariedEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary


h_emp = HourlyEmployee(100, 8)
s_emp = SalariedEmployee(30000)

print("Hourly Employee Pay:", h_emp.calculate_pay())
print("Salaried Employee Pay:", s_emp.calculate_pay())
