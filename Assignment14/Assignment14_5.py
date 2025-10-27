class BankAccount():
    
    def __init__(self,AccNumber,Aname,Abalance):
        self.account_number=AccNumber
        self.name=Aname
        self.balance=Abalance
    
    def Deposit(self,DepositAmount):
        self.balance+=DepositAmount
        print("Amount deposited successfully...")
        print("Current Balance is:",self.balance)
        
    
    def Withdraw(self,WithdrawalAmount):
        if(self.balance>=WithdrawalAmount):
            self.balance-=WithdrawalAmount
            print("Amount withdrawaled successfulyy..")
            print("Current Balance is:",self.balance)
            
        else:
            print("Insufficient Funds..")
            
    def DisplayBalance(self):
        print("Account number is:",self.account_number)
        print("Account Holder name is:",self.name)
        print("Total balance is:",self.balance)
        
def main():
    obj1= BankAccount(23872327842,"YASH GORAKSHNATH ANDHALE",10000000)
    
    DepositAmount=int(input("Enter amount to deposit:"))
    obj1.Deposit(DepositAmount)
    
    WithdrawalAmount=int(input("Enter amount to withdraw:"))
    obj1.Withdraw(WithdrawalAmount)
    obj1.DisplayBalance()
    
    print("\n")
    
    obj2= BankAccount(4567890,"ROHIT GURUNATH SHARMA",26400000)
    
    DepositAmount=int(input("Enter amount to deposit:"))
    obj2.Deposit(DepositAmount)
    
    WithdrawalAmount=int(input("Enter amount to withdraw:"))
    obj2.Withdraw(WithdrawalAmount)
    obj2.DisplayBalance()
    
if __name__=="__main__":
    main()