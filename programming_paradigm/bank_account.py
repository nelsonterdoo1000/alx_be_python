class BankAccount:
    def __init__(self, account_balance=0) -> None:
        self.account_balance = float(account_balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += float(amount)
            return f"Deposited: ${float(amount):.2f}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= float(amount)
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")