class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display_balance(self):
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


account1 = BankAccount("Ardhra", 123456, 1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.display_balance()
