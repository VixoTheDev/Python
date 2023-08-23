class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")
    
    def get_balance(self):
        return self.balance
    
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")

# Create instances of BankAccount
account1 = BankAccount("123456", 1000)
account2 = BankAccount("789012", 500)

# Perform actions on the accounts
account1.display_info()
account1.deposit(200)
account1.withdraw(300)

account2.display_info()
account2.deposit(1000)
account2.withdraw(800)
