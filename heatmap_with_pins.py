import pandas as pd
import folium
from folium.plugins import HeatMap

map_initial_location = [50.0755, 14.4378]

df = pd.read_csv('praha1.csv')
df['area'] = df['address'].apply(lambda x: x.split(',')[-1])
df = df[df['total_price'] < 20000]
decimal_places = 5  # Adjust this to change the grid cell size

df['lat_bin'] = df['gps.lat'].round(decimal_places)
df['lon_bin'] = df['gps.lng'].round(decimal_places)

df['lat'] = df['lat_bin']
df['lon'] = df['lon_bin']
def outliers_price(quantile):
    # you can specify the initial location of your map
    # for instance, let's use the coordinates for Prague
    # m = folium.Map(location=map_initial_location, zoom_start=12)
    m_outliers = folium.Map(location=map_initial_location, zoom_start=13)
    print(df.groupby('area')['price_per_sqm'])
    Q1 = df.groupby('area')['price_per_sqm'].transform('quantile', quantile)
    outliers = df[df['price_per_sqm'] < Q1]
    outliers_heat_data = [[row['lat'], row['lon'], row['price_per_sqm']] for index, row in outliers.iterrows()]
    HeatMap(outliers_heat_data).add_to(m_outliers)
    for index, row in outliers.iterrows():
        popup_text = "<a href='{url}' target='_blank'> Click here for more details</a>"
        popup_text = popup_text.format(url=row['full_url'])
        folium.Marker([row['lat'], row['lon']], popup=folium.Popup(popup_text, max_width=500)).add_to(m_outliers)
    m_outliers.save('outliers_heatmap_with_links_1.html')


outliers_price(0.15)
# Calculate the lower outlier thresholds for price and distanc

# Calculate the 5th percentile for price and distance
lower_threshold_price = df['price_per_sqm'].quantile(0.20)
lower_threshold_distance = df['distance'].quantile(0.25)

# Select the properties that are below both thresholds

# Select the properties that are below both thresholds
outliers = df[(df['price_per_sqm'] < lower_threshold_price) & (df['distance'] < lower_threshold_distance)]
m_outliers = folium.Map(location=map_initial_location, zoom_start=13)

# Create heatmap
heat_data = [[row['lat_bin'], row['lon_bin']] for index, row in outliers.iterrows()]
HeatMap(heat_data).add_to(m_outliers)

# Create clickable markers for each point
for index, row in outliers.iterrows():
    popup_text = "<a href='{url}' target='_blank'> Click here for more details</a>"
    popup_text = popup_text.format(url=row['full_url'])
    folium.Marker([row['lat_bin'], row['lon_bin']], popup=folium.Popup(popup_text, max_width=500)).add_to(m_outliers)

# Save it to html
m_outliers.save('outliers_heatmap_with_links_distance1.html')
