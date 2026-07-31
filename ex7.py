import folium
import pandas as pd

# Load the data
data = pd.read_csv("india_data.csv")

# Create the map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add the choropleth layer
folium.Choropleth(
    geo_data="india_states_districts.json",
    name="choropleth",
    data=data,
    columns=["State", "Value"],
    key_on="feature.properties.NAME_1",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Value"
).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Save the map
m.save("india_map.html")

print("Map created successfully!")
print("Open 'india_map.html' in your browser.")
