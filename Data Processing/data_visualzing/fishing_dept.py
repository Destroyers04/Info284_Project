import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=";")
u_data = data[data["Havdybde start"] < 0]
sns.scatterplot(x="Havdybde start", y="Rundvekt", data=u_data)
plt.title("Scatter Plot of Havdybde start vs. Rundvekt")
plt.xlabel("Havdybde start")
plt.ylabel("Rundvek")
plt.show()