import pandas as pd
data = pd.read_csv('prenajom_praha_bezrealitky1.csv', index_col=0)

data['total_price'] = data['price'] + data['charges']

# Create full URL
data['full_url'] = "https://www.bezrealitky.cz/nemovitosti-byty-domy/" + data['uri']

# Calculate price per square meter
data['price_per_sqm'] = data['price'] / data['surface']
data.to_csv('praha1.csv')

