import psycopg2
import geopandas as gpd

# Connect to PostGIS database
conn = psycopg2.connect(
    dbname='your_db',
    user='your_user',
    password='your_password',
    host='localhost',
    port='5432'
)

# Load shapefile or GeoJSON
gdf = gpd.read_file('your_spatial_data.shp')

# Upload to PostGIS
gdf.to_postgis('table_name', conn, if_exists='replace', index=False)

print("Data uploaded to PostGIS successfully.")
