
# geopandas will print a waring in the terminal that can b ignored

import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import pandas as pd

your_dataframe = pd.read_csv("Data Processing/data_visualzing/fish-data.csv", sep=';')

your_dataframe['Startposisjon bredde'] = your_dataframe['Startposisjon bredde'].str.replace(',', '.').astype(float)
your_dataframe['Startposisjon lengde'] = your_dataframe['Startposisjon lengde'].str.replace(',', '.').astype(float)

geometry = [Point(xy) for xy in zip(your_dataframe['Startposisjon lengde'], your_dataframe['Startposisjon bredde'])]
geo_df = gpd.GeoDataFrame(your_dataframe, geometry=geometry)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(15, 10))

geo_df.plot(ax=ax, color='red', markersize=10)
plt.title('Geospatial Analysis of Fishing Start Locations')
plt.show()
