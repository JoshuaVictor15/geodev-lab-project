# Week 10: GeoPandas, layers as tables

## What this folder contains
### Guided Scripts
- [x] `csv_to_points.py`: Converts health facility CSV coordinates to spatial points.
- [x] `explore_layer.py`: Inspects ward dataset properties.
- [x] `explore_pandas.py`: Explores population data and statistics.
- [x] `filter_sort.py`: Filters, ranks, and summarises ward populations.
- [x] `geom_props.py`: Inspects geometry, validity, and centroid.
- [x] `join_population.py`: Cleans ward names and joins population data.
- [x] `make_map.py`: Creates and exports a health facility map.
- [x] `save_outputs.py`: Exports ward data as GeoPackage and CSV files.
- [x] `facilities_map.png`: Health facility map of Ibadan North.

### Independent Challenge
- [x] `my_explore.py`: Inspects Kaltungo ward dataset properties.
- [x] `my_join.py`: Cleans and joins population data to ward polygons.
- [x] `my_map.py`: Creates and exports a health facility map.
- [x] `my_points.py`: Converts health facility CSV coordinates to spatial points.
- [x] `my_map.png`: Health facility map of Kaltungo LGA.

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