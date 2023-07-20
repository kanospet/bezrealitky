import folium
from folium.plugins import HeatMap

# you can specify the initial location of your map
# for instance, let's use the coordinates for Prague
map_initial_location = [50.0755, 14.4378]

# create the folium map object
m = folium.Map(location=map_initial_location, zoom_start=12)

# we'll use df with 'lat', 'lon' and 'price_per_sqm' columns
# make sure you filter out any rows with missing data in these columns
heat_data = [[row['lat_bin'], row['lon_bin'], row['price_per_sqm']] for index, row in df.iterrows()]

# add the heatmap to the map
HeatMap(heat_data).add_to(m)

# display the map
m
m.save('heatmap1.html')
