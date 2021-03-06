# -*- coding: utf-8 -*-
"""gis_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1axt8djVW_O0hUuM6krCoN9pQQJnurqi9

# Gis data analysis
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import pandas_profiling as pp
import numpy as np
import seaborn as sns
sns.set()

df = pd.read_csv('/content/drive/My Drive/data_drive/ACT_Road_Crash_Data.csv')

df.head()

print(df['LONGITUDE'].values)

print(df['LATITUDE'].values)



! pip install folium

import folium

my_map3 = folium.Map(location = [-35.34139384, 149.05180491],zoom_start = 15) 
# Pass a string in popup parameter 
folium.Marker([-35.34139384,149.05180491], popup = 'accident_prone').add_to(my_map3)

my_map3.save("my_map2.html")

# pp.ProfileReport(df)

print(np.unique(df['WEATHER_CONDITION'].values))

print(np.unique(df['ROAD_CONDITION'].values))

print(np.unique(df['LIGHTING_CONDITION'].values))

