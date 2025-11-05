import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    Line="*"*51
    
    data={
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
    df=pd.DataFrame(data)
    print(Line)
    print(df)
    print(Line)
    print("Shape:",df.shape)
    print(Line)
    print("Columns:",df.columns)
    print(Line)
    print("Datatypes\n:",df.dtypes)
    
    #Printing Descriptive statistics
    print(Line)
    print("Description:",df.describe())
    
    #Adding new column "Total" to dataframe
    #df['Total']=[253,260,242]
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print(Line)
    print("Dataframe after adding Total column:\n",df)
    
    #Displaying the students who scores more than 85
    result=df[df['Science']>85]
    print(Line)
    print("Students who score more than 85 in science:\n",result)
    
    #Replacing the name
    print(Line)
    df['Name']=df['Name'].replace('Pooja','Puja')
    print(df)
  
    #DataFrame sorted using Total marks by decending order
    df_Sort=df.sort_values(by='Total',ascending=False)
    print(Line)
    print("Dataframe sorted by Total in decending:\n",df_Sort)
    
    
    #bar plot
    plt.bar(df['Name'],df['Total'],color=['red','green','blue'])
    plt.title("Students Total Marks")
    plt.xlabel=("Student Name")
    plt.ylabel=("Total Marks")
    plt.show()

    print(Line)
    #Created a dataframe with missing value
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88, ],
        'Science': [91, np.nan, 85],
        'English': [75, 85, np.nan]
    }
    df=pd.DataFrame(data2)
    print("Dataframe with missing values:\n",df)
    
    #Filling a missing values with column mean
    dffill=df.fillna(df.mean(numeric_only=True))
    print(Line)
    print("After filling the missing values:\n",dffill)
    
    #Drop the English column from original dataframe
    print(Line)
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)
    df=df.drop('English',axis=1)
    print("After droping the English column:\n",df)
    print(Line)
    
if __name__=="__main__":
    main()