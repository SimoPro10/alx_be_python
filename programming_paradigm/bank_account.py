

class BankAccount():
    def __init__(self,initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self,amount):
        self.account_balance += amount
        return amount
    def withdraw(self,amount):
        if amount <= account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance():
        print(f"your balance is : {account_balance}")


