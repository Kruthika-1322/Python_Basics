import sys
class Customer:
    '''Customer classs with Bank Opertaion'''
    bankname="XXX BANK"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("The balance after deposit is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient fund")
        self.balance=self.balance-amount
        print("The balance after deposit is:", self.balance)
print("Welcome to",Customer.bankname)
name=input("Enter the name of the customer: ")
c=Customer(name)
while True:
    print("Enter your Choice\n 1.Deposit-D\n 2.Withdraw-W\n 3.Exit-E\n")
    choice=input().upper()
    if choice=='D':
        amount=float(input("Enter the amount to be deposited"))
        c.deposit(amount)
    elif choice=='W':
        amount = float(input("Enter the amount to be withdrawn"))
        c.withdraw(amount)
    elif choice=='E':
        sys.exit()
    else:
        print("Enter the valid choice")

