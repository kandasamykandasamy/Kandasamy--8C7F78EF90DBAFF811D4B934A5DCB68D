class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.__account_number = account_number  # Private attribute for account number
        self.__account_holder = account_holder  # Private attribute for account holder name
        self.__balance = initial_balance        # Private attribute for account balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Balance: ${self.__balance}")

# Create an instance of the BankAccount class
account1 = BankAccount("12345", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
account1.display_balance()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.withdraw(1500.0)
account1.display_balance()