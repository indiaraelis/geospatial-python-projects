import geopandas as gpd

# Load point data and polygon data
points = gpd.read_file('points.geojson')
polygons = gpd.read_file('polygons.geojson')

# Create buffers around points (e.g., 500 meters)
points['buffer'] = points.geometry.buffer(500)

# Convert buffers to GeoDataFrame
buffers = gpd.GeoDataFrame(points, geometry='buffer')

# Spatial join buffers with polygons
joined = gpd.sjoin(buffers, polygons, how='inner', op='intersects')

print(joined.head())
