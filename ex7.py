import folium
import pandas as pd
data = pd.read_csv("indiadata.csv")
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
folium.Choropleth(
    geo_data="indiadata.json",
    name="choropleth",
    data=data,
    columns=["State", "Value"],
    key_on="feature.properties.st_nm",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Value"
).add_to(m)
folium.LayerControl().add_to(m)
m.save("india_map.html")
print("Map created successfully!")
print("Open 'india_map.html' in your browser.")
