class BalanceException(Exception):
    pass

class BankAccount:
    def __init__ (self, initialAmount, accName):
        self.balance = initialAmount 
        self.name = accName
        print(f"\n'{self.name}' has created a new account with an initial amount of Rs.{self.balance:.2f}.\n")


    def getBalance(self):
        print(f"\n Account balance of '{self.name}' is ${self.balance:.2f}.\n")    


    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit Complete ")
        self.getBalance()
    

    def deposit(self , amount):
        self.balance = self.balance + amount
        print(f"\n Deposit Complete ")
        self.getBalance()

    def viableTransaction(self , amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f} ")
                

    def withdraw(self , amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\n Withdrawal Complete ")
            self.getBalance()   
        except BalanceException as e:
            print(f"\n Withdraw interupted due to: {e}")


    def transfer(self , amount , account):
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n Transfer Complete ")
        except BalanceException as e:
            print(f"\n Transfer interupted due to: {e}") 

            


class InterestRewardsAccnt(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05) 
        print(f"\n Deposit Complete ")
        self.getBalance()         



class SavingsAccnt(InterestRewardsAccnt):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5


    def withdraw(self, amount):
        try :
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\n Withdrawal Complete ")    
            self.getBalance()
        except BalanceException as e:
            print(f"\n Withdraw interupted due to: {e}")

