import pandas as pd
from sklearn.model_selection import train_test_split

def main():
  data={'Grade':['A+','B','A','C','B+']}
  df=pd.DataFrame(data)
  
  print("Original DataFrame:\n",df)
  
  GradeMap={
      'A+':'Excellent',
      'A':'Very Good',
      'B+':'Good',
      'B':'Average',
      'C':'Poor'
  }
  
  df['Grade']=df['Grade'].replace(GradeMap)
  
  print("DataFrame after replacing:\n",df)
if __name__ == "__main__":
    main()
