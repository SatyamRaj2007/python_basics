import pandas as pd
data={
    'Name':['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age':[25, 30, 35, 40, 45],
    'score':[85, 90, 95, 80, 75],
    'city':['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df=pd.DataFrame(data)
print(df) 
print(df.info())
print(df.describe())