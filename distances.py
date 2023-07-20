from math import radians, sin, cos, sqrt, atan2
import numpy as np
import pandas as pd

df = pd.read_csv('praha1.csv', index_col=0)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius of Earth in kilometers
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)

    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
    res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))

    return np.round(res, 2)  # rounding to two decimal places
ref_lat, ref_lon = 50.08180248858138, 14.43056532883569

df['distance'] = df.apply(lambda row: haversine(ref_lat, ref_lon, row['gps.lat'], row['gps.lng']), axis=1)
df.to_csv('praha1.csv')
