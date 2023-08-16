#1
class BankAccount:
    def __init__(self, user_name, account_type, balance = 1.0):
        self.user_name = user_name
        self.account_type = account_type
        self.balance = balance

account1 = BankAccount("Bilbo", "Savings", 15.75)
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business", 700.50)
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")
print(f"New account balance of {account1.user_name} is {account1.balance}")
print(f"New account balance of {account2.user_name} is {account2.balance}")
