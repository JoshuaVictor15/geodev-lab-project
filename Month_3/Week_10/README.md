# Week 10: GeoPandas, layers as tables

## What this folder contains
### Guided Scripts
- [x] `csv_to_points.py`: Converts health facilities CSV to points (EPSG:4326) and saves them as Geopackage
- [x] `explore_layer.py`: Reads the ward dataset and inspects its records, dimensions, geometry types, CRS, and spatial bounds.
- [x] `explore_pandas.py`: Reads the ward population CSV and inspects its records, dimensions, columns, data types, and population statistics.
- [x] `filter_sort.py`: Filters wards with populations above 35,000, ranks wards by population, converts population to thousands, and calculates the total population.
- [x] `geom_props.py`: Inspects the first ward’s geometry, checks its validity, and calculates its centroid.
- [x] `join_population.py`: Cleans ward names, joins population data to ward polygons, and compares matching results before and after cleaning.
- [x] `make_map.py`: Creates and saves a map showing ward boundaries and health facility locations in Ibadan North.
- [x] `save_outputs.py`: Saves a copy of the ward dataset as a GeoPackage, exports its attribute table as a CSV, and lists the GeoPackage layers.
- [x] `facilities_map.png`: The output map from `make_map.py`
### Independent Challenge
- [x] `my_explore.py`: Reads the ward dataset from my data and inspects its records, dimensions, geometry types, CRS, and spatial bounds.
- [x] `my_join.py`: Cleans ward names, joins population data to ward polygons, and compares matching results before and after cleaning from my data.
- [x] `my_map.py`: Creates and saves a map showing ward boundaries and health facility locations in Kaltungo LGA.
- [x] `my_points.py`: Converts health facilities CSV from my data to points (EPSG:4326) and saves them as Geopackage

- [x] `my_map.png`: The output map from `my_map.py`

## How to run it
From the repository root:
```bash
uv run Month_3/Week_10/script.py
```

## What I found
- Majority of the wards in the practical dataset have population of less than 35,000. Only 5 wards have population more than 35,000
- From my data i found out that converting CSV to points in (EPSG:4326) contradicts my wards layer geopackage which is in (EPSG:32632)

## What went wrong and how I fixed it
The `my_map.py` output initially showed misaligned features because the datasets had different coordinate reference systems (CRS). I fixed this by reprojecting the health facility points to EPSG:32632, matching the wards CRS before creating the final map.