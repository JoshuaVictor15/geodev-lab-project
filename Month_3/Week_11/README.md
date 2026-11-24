# Week 11: Coordinate Reference System and Spatial Operations in Code

## What this folder contains
### Guided Scripts
- [x] `area_wrong_and_right.py`: Reprojects ward boundaries to UTM Zone 31N, calculates individual ward areas, and total area of Ibadan North in square kilometres.
- [x] `clip_dissolve.py`: Clips roads to Agodi ward, calculates total road length, and dissolves ward boundaries to calculate the LGA area.
- [x] `coverage_gap.py`: Creates and dissolves 2 km buffers around health facilities, then calculates the uncovered area and percentage of each ward.
- [x] `fix_geometry.py`: Creates an invalid polygon, identifies its geometry error, repairs it, and verifies its validity and new geometry type.
- [x] `nearest.py`: Calculates ward centroids, identifies the nearest health facility to each centroid, and measures the straight-line distance in kilometres.
- [x] `one_point.py`: Transforms longitude and latitude coordinates WGS 1984 into UTM Zone 31N Easting and Northing coordinates.
- [x] `set_vs_to.py`: Demonstrates the difference between reprojecting and assigning a CRS, and saves an incorrectly labelled as `wards_wrongly_labelled.gpkg`
- [x] `spatial_ops.py`: Creates 2 km buffers around health facilities and uses a spatial join to count the number of facilities within each ward.
### Independent Challenge
- [x] `my_count.py`: Uses a spatial join to count health facilities within each ward in Kaltungo LGA and verifies the total facility count.
- [x] `my_crs.py`: Reprojects ward boundaries to UTM Zone 32N, calculates individual ward areas, and total area of Kaltungo LGA in square kilometres.
- [x] `my_map.py`: Creates and saves a map showing ward boundaries, health facility locations, and dissolved 5 km buffers in Kaltungo LGA.
- [x] `my_reach.py`: Creates and dissolves 5 km health facility buffers, calculates the uncovered area and percentage of each ward in Kaltungo LGA, and saves the dissolved buffer as a GeoPackage named `my_buffer.gpkg`
- [x] `my_validity.py`: Checks ward geometry validity, identifies and counts invalid geometries, repairs them, and verifies the corrected geometries.
- [x] `my_buffer_map.png`: The output map from `my_map.py` showing the health facilities, the 5km dissolve buffer and the wards polygon in Kaltungo LGA

## How to run it
From the repository root:
```bash
uv run Month_3/Week_11/script.py
```

## What I found
- From `my_reach.py` I found out that only 3 out of the 10 wards have an uncovered percentage of greater than 10
- Reprojecting and assigining CRS are two distinct things and each of them have a different purpose

## What went wrong and how I fixed it
- Error messages from the output after running the code. I fixed that by checking the error message displayed and debugging that particular line. Most of the Errors are as a result of incorrect spelling or missing commas or incorrect letter case.
