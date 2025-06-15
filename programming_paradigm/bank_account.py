class BankAccount:
    def __init__(self, account_balance=0) -> None:
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrawn: ${amount}"
        else:
            return "Insufficient funds"

    def display_balance(self):
        return f"Current Balance: ${self.account_balance}"

