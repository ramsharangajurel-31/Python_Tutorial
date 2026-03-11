class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Your account has been credited by {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds to withdraw {amount}.")
        else:
            self.balance -= amount
            print(f"Your account has been debited by {amount}. New balance is {self.balance}")

    def get_balance(self):
        return self.balance


# creating an object of the BankAccount class
account = BankAccount("Ram Sharan", 10000)

# accessing attributes and methods
print(account.owner)
print(account.get_balance())

account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())