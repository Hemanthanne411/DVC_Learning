import pandas as pd
import os

data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'city': ['New York', 'London', 'Tokyo'],
    'age': [28, 34, 25]
})

#added new row to my file 
data.loc[len(data)] = ['Charlie', 'Tokyo', 25]


foldn = "data"
filen = "thedatafile.csv"

path = os.path.join(foldn,filen)

os.makedirs(foldn, exist_ok=True)

data.to_csv(path, index=False)

