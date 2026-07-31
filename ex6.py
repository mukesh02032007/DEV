import folium
import pandas as pd

# Load your dataset
data = pd.read_csv("your_data.csv")

# Create a map centered on a specific location
m = folium.Map(location=[45.523, -122.675], zoom_start=13)

# Group data by latitude and longitude
location_data = data.groupby(['lat', 'lon']).count()

# Add markers with popup
for i in range(len(location_data)):
    folium.Marker(
        location=[
            location_data.iloc[i].name[0],
            location_data.iloc[i].name[1]
        ],
        popup=f"Count: {location_data.iloc[i][0]}",
        icon=folium.Icon(color="red")
    ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save("map.html")

print("Map created successfully!")
print("Open 'map.html' in your web browser to view the map.")
