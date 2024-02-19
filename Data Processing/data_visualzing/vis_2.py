import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

your_dataframe = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

sns.boxplot(x='Varighet', data=your_dataframe)
plt.title('Box Plot of Fishing Trip Duration')
plt.xlabel('Varighet')
plt.show()
