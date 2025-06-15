class BankAccount:
    def __init__(self, account_balance=0) -> None:
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"The account balance is: ${self.account_balance}")


# account1 = BankAccount()

# account2 = BankAccount(1000)

# account1.deposit(500)
# account1.display_balance()

# account1.deposit(200)

# account1.display_balance()

