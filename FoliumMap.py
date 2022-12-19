import pandas as pd
import folium
import webbrowser

CB_geoData = pd.read_csv('c:/Fileio/CB_geo.csv', encoding='utf-8', engine='python')

map = folium.Map(location=[37.4568621,126.7041267], zoom_start=20)
for i, store in CB_geoData.iterrows():
    folium.Marker(location=[store['_Y'], store['_X']], popup=store['store'], icon=folium.Icon(color='red', icon='star')).add_to(map)
map.save('c:/Fileio/map_coffeeBean.html')
webbrowser,open('c:/Fileio/map_coffeeBean.html')