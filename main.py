import Bank
import Input

balance = Bank.ATM.get_balance()
print("Starting Balance: $" + str(balance))

amount = Input.Validator.get_float("Please enter deposit amount ($0.00 - $1000.00): ", 0, 1000)
   
balance = Bank.ATM.deposit(amount)
print("New Balance: $" + str(balance))

wth = Bank.ATM.withdraw(float(input("Please enter withdraw amount: ")))
