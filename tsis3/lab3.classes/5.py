''' Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''
import random

class Account:

    def __init__(self, owner, balance, depos, withdraw )
        self.owner= input()
        self.balance= int(input())
        self.depos= int(input())
        self.withdraw= random.randrange(self.balance)
    def deposit(self):
        self.balance-= self.depos
    def withdrawal(self):
        self.balance += self.withdraw

x=Account 

 