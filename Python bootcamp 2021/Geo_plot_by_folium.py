import numpy as np
import pandas as pd
import folium as fo
%matplotlib inline

map = fo.Map()
map

volcano = pd,read_csv('volcano.csv')

lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])

vol = fo.FeatureGroup(name='My Map')

for lat,lon,name in zip(lat_vo, lon_vo, name_vo):
    vol.add_child(fo.Marker(location =[lat, lon] popup = 'name', icon = fo.Icon(color = 'red')))
    map.add_child(vol)


 