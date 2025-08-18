class BankAccount:
    def __init__(self, initail_balance=0):
        self.account_balance = initail_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance: 2f}")

    def get_balance(self):
        return self.account_balance
