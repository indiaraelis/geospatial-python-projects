# Upload to PostGIS

This script uploads geospatial data (shapefiles, GeoJSON) to a PostGIS-enabled PostgreSQL database using GeoPandas.

## Requirements

- psycopg2
- geopandas

## Usage

1. Update the connection parameters in the script (`dbname`, `user`, `password`, `host`, `port`).
2. Replace `'your_spatial_data.shp'` with your geospatial data file.
3. Run the script to upload data to your PostGIS database.
