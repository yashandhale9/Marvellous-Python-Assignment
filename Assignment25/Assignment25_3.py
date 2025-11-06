import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data={'City':['Pune','Mumbai','Delhi','Pune','Delhi']}
    df=pd.DataFrame(data)
    
    print("Original DataFrame:",df)
    
    le=LabelEncoder()
    df['City_Encoded']=le.fit_transform(df['City'])
    
    print("DataFrame after label encoding:\n",df)
    print("City Mapping:",dict(zip(le.classes_,range(len(le.classes_)))))

    
    # Encode City using map 
    #CityMap = {'Delhi': 0, 'Mumbai': 1, 'Pune': 2}
    #df['City_Code'] = df['City'].map(CityMap)
    

if __name__=="__main__":
    main()