import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    Line="*"*51
    data={
        'Name':['Amit','Sagar','Pooja'],
        'Gender': ['Male', 'Male', 'Female'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
        }
    df=pd.DataFrame(data)
    
    #Normalized kel math score using min max scale
    Math_Min=df['Math'].min()
    Math_Max=df['Math'].max()
    df['Math_Normalized']=(df['Math']-Math_Min)/(Math_Max-Math_Min)
    print("Dataframe with Normalized math score:\n",df)
    
    #Created a gender column ani encoding kel
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    print("DataFrame after encoding gender:\n", df)

    #Student la gender nusar groupwise kel ani avg marks kadhale
    Avg_Marks=df.groupby('Gender')[['Math','Science','English']].mean()
    print("Average marks by gender:")
    print(Avg_Marks)
    
    #Pie plot of math sub marks of sagar 
    sagar = df[df['Name'] == 'Sagar'].iloc[0]
    marks=[sagar['Math'],sagar['Science'],sagar['English']]
    subjects=['Maths','Science','English']
    plt.pie(marks,labels=subjects,autopct='%1.1f%%',startangle=90)
    plt.title("Marks of Sagar")
    plt.axis('equal')
    plt.show()
    
    #Status column add kela
    df['Total']=df[['Math','Science','English']].sum(axis=1)
    df['Status'] = np.where(df['Total'] >= 250, 'Pass', 'Fail')
    print("Dataframe with total marks and Status:\n",df)
    
    #Passcount kadhala
    PassCount=(df['Status']=='Pass').sum()
    print("Number of students who passed:\n",PassCount)
    
    #Final dataframe csv madhe export kela
    df.to_csv('StudentData.csv',index=False)
    print("Final dataset exported to 'StudentData.csv' file....")
    
    #Histogram for math marks
    plt.hist(df['Math'],bins=5,color='skyblue',edgecolor='black')
    plt.title("Math Marks Distibution")
    plt.xlabel("Math Marks")
    plt.ylabel("Number of students")
    plt.grid()
    plt.show()
    
    #Rename the math column
    df.rename(columns={'Math':'Mathematics'},inplace=True)
    print(df)

    #Boxplot for the English Marks
    plt.boxplot(df['English'], vert=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue'),
                medianprops=dict(color='red'))
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid()
    plt.show()
    
if __name__=="__main__":
    main()