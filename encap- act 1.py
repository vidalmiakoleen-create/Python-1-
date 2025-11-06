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
            
    # optional: add a getter method to access balance safely
    def get_balance(self):
        return self.__balance


# Example usage
amount1 = BankAccount("Mia", 100000)
amount1.deposit(1500)
amount1.withdraw(2000)
amount1.withdraw(100001)

# Access balance safely through getter
print(f"Final balance: Php {amount1.get_balance()}")
