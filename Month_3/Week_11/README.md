# Week 11: Coordinate Reference System and Spatial Operations in Code

## What this folder contains
### Guided Scripts
### Guided Scripts
- [x] `area_wrong_and_right.py`: Reprojects wards and calculates accurate areas.
- [x] `clip_dissolve.py`: Clips roads, calculates road length, and dissolves ward boundaries.
- [x] `coverage_gap.py`: Calculates uncovered ward areas using 2 km buffers.
- [x] `fix_geometry.py`: Identifies and repairs invalid geometries.
- [x] `nearest.py`: Calculates distances from ward centroids to the nearest health facilities.
- [x] `one_point.py`: Transforms coordinates from WGS 84 to UTM Zone 31N.
- [x] `set_vs_to.py`: Demonstrates the difference between assigning and reprojecting a CRS.
- [x] `spatial_ops.py`: Creates 2 km buffers and counts facilities per ward.

### Independent Challenge
- [x] `my_count.py`: Counts health facilities per ward in Kaltungo LGA.
- [x] `my_crs.py`: Reprojects wards to UTM Zone 32N and calculates areas.
- [x] `my_map.py`: Creates and exports a health facility coverage map.
- [x] `my_reach.py`: Calculates uncovered ward areas and percentages using 5 km buffers.
- [x] `my_validity.py`: Checks and repairs invalid ward geometries.
- [x] `my_buffer_map.png`: Health facility map showing dissolved 5 km buffers in Kaltungo LGA.
#### Reason for using 5km Buffer
I used 5 kilometres buffer for the health facilities because 5km is within the accessibility benchmark of World Health Organisation (WHO), however this does not account for actual travel time

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
