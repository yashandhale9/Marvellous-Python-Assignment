import pandas as pd
import numpy as np
def main():
 data={'Marks':[45,67,88,32,76]}
 
 df=pd.DataFrame(data)
 print("Oroginal DataFrame:\n",df)
 
 df['Marks']=df['Marks'].where(df['Marks']>=50,'Fail')
 print("DataFrame after replacing the Marks<50 with 'Fail':\n",df)

if __name__ == "__main__":
    main()
