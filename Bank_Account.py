# Banka hesap islem programı.

class Bank_Account:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount 
            print(f"{amount} Dollars deposited. New balance = {self.balance} Dollars")
        else:
            print("The amount to be deposited must be positive.")

    def withdraw(self, amount):
        if amount >= self.balance:
            print("İnsufficient funds")
        elif amount <= 0:
            print("The amount to be deposited must be positive.")
        else: 
            self.balance -= amount
            print(f"{amount} was withdrawn. New Balance : {self.balance} Dollars.")
    
    def Show_Balance(self,):
        print(f"Account Holder: {self.account_holder} , Balance : {self.balance} Dollars.")

account1 = Bank_Account("Jake", 100000)

# Transactions
account1.Show_Balance()
account1.deposit(500)
account1.withdraw(300) 
account1.withdraw(200000)