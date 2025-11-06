import pandas as pd

def main():
    data={'Salary':[25000,27000,29000,31000,50000,100000]}
    df=pd.DataFrame(data)
    
    Q1=df['Salary'].quantile(0.25)
    Q3=df['Salary'].quantile(0.75)
    IQR=Q3-Q1
    
    LowerBound=Q1-1.5*IQR
    UpperBound=Q3+1.5*IQR
    
    Outliers = df[(df['Salary'] < LowerBound) | (df['Salary'] > UpperBound)]
    
    print("Q1:",Q1)
    print("Q3:",Q3)
    print("IQR:",IQR)
    print("Lower Bound:",LowerBound)
    print("Upper Bound:",UpperBound)
    print("Outliers:\n",Outliers)
    
if __name__=="__main__":
    main()