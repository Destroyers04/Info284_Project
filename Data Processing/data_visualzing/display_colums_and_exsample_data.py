import pandas as pd

data = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')
df = pd.DataFrame(data)
pd.set_option('display.max_columns', None)
print(df)
