import folium
import pandas as pd
data = pd.read_csv("data.csv")
m = folium.Map(location=[45.523, -122.675], zoom_start=13)
location_data = data.groupby(['lat', 'lon']).size().reset_index(name='count')
for index, row in location_data.iterrows():
    lat = row['lat']
    lon = row['lon']
    count = row['count']
    
    folium.Marker(
        location=[lat, lon],
        popup=f"Count: {count}",
        icon=folium.Icon(color="red")
    ).add_to(m)

folium.LayerControl().add_to(m)
m.save("map.html")

print("Map created successfully!")
print("Open 'map.html' in your web browser to view the map.")
