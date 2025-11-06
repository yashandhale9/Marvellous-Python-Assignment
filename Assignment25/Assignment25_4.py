import pandas as pd

def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    df = pd.DataFrame(data)
    
    print("Original DataFrame:\n", df)
    
    df_encoded = pd.get_dummies(df, columns=['Department'], prefix='Dept')
    print("\nDataFrame after One-Hot Encoding:\n", df_encoded)

if __name__ == "__main__":
    main()
