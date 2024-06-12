#banking system-file handling
#create acc with capitl
#deposit/withdraw
#transaction into a file

import os
class InsufficentFundsError(Exception):
    pass
class Account:
    def __init__(self,name,deposit):
        self.balance=deposit
        self.acc_name=name
        self.file=f"{self.acc_name}_transac.txt"
        self.create_acc()

    def create_acc(self):
        with open(self.file, 'w') as bank:
            bank.write(f"New Account created for: {self.acc_name}\nAccount balance: {self.balance}\n")

    def deposit(self,amt):
        self.balance+=amt
        with open(self.file, 'a') as bank:
            bank.write(f"Log: Deposit found:- Rs{amt}\nAccount balance: {self.balance}\n")
        #print("Transaction successful")    

    def withdrawal(self,amt):
        # if self.balance-amt<0:
        #     print("Insufficent funds. unable to withdraw")    #exception hndl
        # else:
        #     self.balance-=amt
        #     with open(self.file, 'a') as bank:
        #         bank.write(f"Log: Withdrawal found:- Rs{amt}\nAccount balance:{self.balance}\n") 
        try:
            if self.balance-amt<0:
                raise InsufficentFundsError("Insufficent funds. unable to withdraw")
            else:
                self.balance-=amt
                with open(self.file, 'a') as bank:
                    bank.write(f"Log: Withdrawal found:- Rs{amt}\nAccount balance:{self.balance}\n")
        except InsufficentFundsError as ife:
            print(ife)            


    def checkbal(self):
        print("Your Balance: ",self.balance)

    def complete_history(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as bank:
                history = bank.read()
            return history
        else:
            return "No transaction history available."
                       
a=Account("AK",10000)    
a.deposit(1000)
a.withdrawal(500)
print(a.complete_history())    
a.checkbal()            




