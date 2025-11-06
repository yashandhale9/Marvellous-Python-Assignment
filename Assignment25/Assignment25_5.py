import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data ={'Age':[22,25,47,52,46,56],'Purchased':[0,1,1,0,1,0]}
    df=pd.DataFrame(data)
    
    print("Original DataFrame:\n",df)
    
    train_df,test_df=train_test_split(df,test_size=0.2,random_state=42)
    print("Training Set:\n",train_df)
    print("Testing Set:\n",test_df)
    
if __name__ == "__main__":
    main()
