import pandas as pd

def main():
  data={'Age':[18,22,25,30,35]}
  df=pd.DataFrame(data)
  
  Min_Age=df['Age'].min()
  Max_Age=df['Age'].max()
  
  df['Age_Normalized']=(df['Age']-Min_Age)/(Max_Age-Min_Age)
  
  print("DataFrame with Normalized age:\n",df)
if __name__ == "__main__":
    main()
