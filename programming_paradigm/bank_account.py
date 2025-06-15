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
        if amount <= self.account_balance:
            self.account_balance -= float(amount)
            return f"Withdrawn: ${float(amount):.2f}"
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

