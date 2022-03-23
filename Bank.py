class ATM:

   balance = 20.00
   
   def deposit(amount):
     print("Depositing $" + str(amount)) 
     ATM.balance += amount
     return ATM.balance

   def withdraw(amount):
        if ATM.balance >= amount:
            print("Withdrawing $" + str(amount))
            ATM.balance -= amount
            print("Your new balance is: $" + str(ATM.balance))
        else:
            print("YOUR CARD WAS DECLINED!!!")
        return ATM.balance
        
   def get_balance():
        return ATM.balance
