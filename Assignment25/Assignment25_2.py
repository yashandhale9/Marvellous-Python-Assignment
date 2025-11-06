import pandas as pd

def main():
    data={'Name':['A','B','C'],'Age':[21.0,22.0,23.0]}
    df=pd.DataFrame(data)
    
    print("DataFrame before conversion:\n",df.dtypes)
    
    df['Age']=df['Age'].astype(int)
    print("Data types after conversion:\n",df.dtypes)
    print("Updated DataFrame:\n",df)
    
if __name__=="__main__":
    main()