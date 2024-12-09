class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}.\nNew Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}.\nNew Balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

# Creating an object of BankAccount
account = BankAccount("12345", 10000)
account.deposit(5000)
account.withdraw(3000)
account.withdraw(1500)
print(f"Final Balance: {account.get_balance()}")
