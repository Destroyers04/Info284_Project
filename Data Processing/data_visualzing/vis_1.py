import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


your_dataframe = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

sns.scatterplot(x='Havdybde start', y='Rundvekt', data=your_dataframe)
plt.title('Scatter Plot of Havdybde start vs. Rundvekt')
plt.xlabel('Havdybde start')
plt.ylabel('Rundvekt')
plt.show()
