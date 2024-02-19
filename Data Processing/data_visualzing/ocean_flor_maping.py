# not finished 

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=";")

filtered_data = data[data['Redskap FDIR'] == "Bunntrål"]

coordinate_columns = ['Startposisjon bredde', 'Startposisjon lengde', 'Havdybde start',
                      'Stopposisjon bredde', 'Stopposisjon lengde', 'Havdybde stopp']
filtered_data[coordinate_columns] = filtered_data[coordinate_columns].astype(str)
filtered_data[coordinate_columns] = filtered_data[coordinate_columns].replace(',', '.', regex=True).astype(float)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(filtered_data['Startposisjon bredde'], 
           filtered_data['Startposisjon lengde'], 
           filtered_data['Havdybde start'], 
           c='b', marker='o', label='Start')

ax.scatter(filtered_data['Stopposisjon bredde'], 
           filtered_data['Stopposisjon lengde'], 
           filtered_data['Havdybde stopp'], 
           c='r', marker='o', label='Stop')

counter = 0
for index, row in filtered_data.iterrows():
    
    ax.plot([row['Startposisjon bredde'], row['Stopposisjon bredde']], 
            [row['Startposisjon lengde'], row['Stopposisjon lengde']], 
            [row['Havdybde start'], row['Havdybde stopp']], c='g')

    print(counter)
    counter += 1


ax.set_xlabel('Startposisjon bredde')
ax.set_ylabel('Startposisjon lengde')
ax.set_zlabel('Havdybde')
ax.legend()

plt.show()
