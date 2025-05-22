import geopandas as gpd
import matplotlib.pyplot as plt

# Load flood-prone areas and population density data
flood_areas = gpd.read_file('flood_areas.geojson')
population = gpd.read_file('population_density.geojson')

# Spatial join to find population affected by flood zones
affected = gpd.sjoin(population, flood_areas, how='inner', op='intersects')

# Plot flood risk map
fig, ax = plt.subplots(figsize=(10, 10))
flood_areas.plot(ax=ax, color='blue', alpha=0.5, label='Flood Zones')
affected.plot(ax=ax, column='density', cmap='Reds', legend=True, label='Affected Population')

plt.title('Flood Risk Map')
plt.legend()
plt.show()
