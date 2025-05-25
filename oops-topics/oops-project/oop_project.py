from bank_account import *


Dave = BankAccount(5000, "Dave")
Sara = BankAccount(2000, "Sara")


Dave.getBalance()
Sara.getBalance()
Sara.deposit(1000)
   
Dave.withdraw(7000)

Dave.transfer(300, Sara)


Jim = InterestRewardsAccnt(1000, "Jim")
Jim.deposit(1000)
Jim.transfer(300, Sara)
Jim.getBalance()


Blaze = SavingsAccnt(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100) 
Blaze.transfer(10000, Sara)



# Python applications ke liye, aap in databases ke liye respective libraries use karte hain, jaise sqlite3, pymongo, psycopg2 (PostgreSQL), mysql-connector-python, etc.
# JavaScript applications ke liye, front-end ya back-end (Node.js) mein libraries ya modules hote hain, jaise mongoose (MongoDB ke liye), mysql package, pg (PostgreSQL ke liye), etc.