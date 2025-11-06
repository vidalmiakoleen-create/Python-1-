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

h_emp = HourlyEmployee(100, 😎
s_emp = SalariedEmployee(30000)

print("Hourly Employee Pay:", h_emp.calculate_pay())
print("Salaried Employee Pay:", s_emp.calculate_pay())
