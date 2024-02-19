
# geopandas prints a warning that can be ignored

import geopandas as gpd
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
import pandas as pd
import random

your_dataframe = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

your_dataframe['Startposisjon bredde'] = your_dataframe['Startposisjon bredde'].str.replace(',', '.').astype(float)
your_dataframe['Startposisjon lengde'] = your_dataframe['Startposisjon lengde'].str.replace(',', '.').astype(float)
your_dataframe['Stopposisjon bredde'] = your_dataframe['Stopposisjon bredde'].str.replace(',', '.').astype(float)
your_dataframe['Stopposisjon lengde'] = your_dataframe['Stopposisjon lengde'].str.replace(',', '.').astype(float)

start_geometry = [Point(xy) for xy in zip(your_dataframe['Startposisjon lengde'], your_dataframe['Startposisjon bredde'])]
end_geometry = [Point(xy) for xy in zip(your_dataframe['Stopposisjon lengde'], your_dataframe['Stopposisjon bredde'])]

random_indices = random.sample(range(len(your_dataframe)), 1000)
random_start_points = [start_geometry[i] for i in random_indices]
random_end_points = [end_geometry[i] for i in random_indices]

start_geo_df = gpd.GeoDataFrame(your_dataframe.iloc[random_indices], geometry=random_start_points)
end_geo_df = gpd.GeoDataFrame(your_dataframe.iloc[random_indices], geometry=random_end_points)

lines = [LineString([start, end]) for start, end in zip(random_start_points, random_end_points)]
lines_geo_df = gpd.GeoDataFrame(geometry=lines)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(15, 10))

start_geo_df.plot(ax=ax, color='blue', markersize=10, label='Start Location')
end_geo_df.plot(ax=ax, color='green', markersize=10, label='End Location')

lines_geo_df.plot(ax=ax, color='red')

plt.title('Geospatial Analysis of Fishing Start and End Locations')
plt.legend()
plt.show()
