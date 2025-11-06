import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data={
        'Age':[25,30,45,35,22],
        'Salary':[50000,60000,80000,65000,45000],
        'Purchased':[1,0,1,0,1]
    }
    
    df=pd.DataFrame(data)
    print("Original DataFrame:\n",df)
    
    x=df[['Age','Salary']]
    y=df['Purchased']
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    print("Indepedent Variable(x_train):",x_train)
    print("Indepedent Variable(x_test):",x_test)
    print("Depedent Variable(y_train):",y_train)
    print("Depedent Variable(y_test):",y_test)
    
if __name__ == "__main__":
    main()
