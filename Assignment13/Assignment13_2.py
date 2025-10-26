class BankAccount:
    ROI=10.5     #class variable
    
    def __init__(self,bName,bAmount):
        self.Name=bName
        self.Amount=bAmount
    
    def Display(self):
            print("Name of customer is:",self.Name)
            print("Amount is:",self.Amount)
        
    def Deposit(self,DepositValue):
            self.Amount+=DepositValue
            print(f"₹{DepositValue} deposited successfully.Current balance:₹{self.Amount}")
        
    def Withdraw(self,WithdrawValue):
            if WithdrawValue<=self.Amount:
                self.Amount-=WithdrawValue
                print(f"₹{WithdrawValue} withdrawn successfully.Current Balance:₹{self.Amount}")
            else:
                print("Insufficient balance...")            
            
        
    def CalculateInterest(self):
            self.interest=(self.Amount*BankAccount.ROI)/100
            print("Interest is:₹",self.interest)

def main():
    Name=input("Enter a name:")
    Amount=float(input("Enter the amount:"))
    
    obj1=BankAccount(Name,Amount)
    
    print("Enter Amount to deposit:")
    DepositValue=float(input())
    obj1.Deposit(DepositValue)
    
    print("Enter amount to be withdrawn:")
    WithdrawValue=float(input())
    obj1.Withdraw(WithdrawValue)
    
    obj1.CalculateInterest()
    
    obj1.Display()
    
if __name__=="__main__":
    main()