class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal of", amount, "successful.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Balance:", self.balance)

# Create an object of BankAccount
account1 = BankAccount("1234567890", "John Doe", 1000.0)

# Accessing class variables
print("Account Number:", account1.account_number)
print("Account Holder Name:", account1.account_holder_name)

# Accessing class methods
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Calculated Interest:", interest)
# Create an object of SavingsAccount
savings_account = SavingsAccount("9876543210", "Jane Smith", 2000.0, 2.5)

# Access inherited member variables and methods
print("Account Holder Name:", savings_account.account_holder_name)
savings_account.display_balance()

# Access additional member variable and method
print("Interest Rate:", savings_account.interest_rate)
savings_account.calculate_interest()

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Calculated Interest:", interest)
# Create an object of SavingsAccount
savings_account = SavingsAccount("9876543210", "Jane Smith", 2000.0, 2.5)

# Access inherited member variables and methods
print("Account Holder Name:", savings_account.account_holder_name)
savings_account.display_balance()

# Access additional member variable and method
print("Interest Rate:", savings_account.interest_rate)
savings_account.calculate_interest()