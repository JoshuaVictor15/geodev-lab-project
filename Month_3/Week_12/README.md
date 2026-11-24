# Week 12: Rasters with Rasterio

## What this folder contains
### Guided Scripts
- [x] `clip_raster.py`: Dissolves ward boundaries, clips the DEM to Ibadan North, and saves the clipped raster while comparing pixel dimensions before and after clipping.
- [x] `inspect_raster.py`: Inspects the DEM raster’s dimensions, band count, data type, CRS, pixel size, spatial bounds, NoData value, and affine transform.
- [x] `ndvi.py`: Applies Landsat surface reflectance scaling, calculates NDVI using the Red and NIR bands, displays NDVI statistics, and saves the output as a GeoTIFF.
- [x] `pixel_coords.py`: Converts raster pixel indices to spatial coordinates and spatial coordinates to raster row and column indices.
- [x] `plot_raster.py`: Visualises NDVI using a red-yellow-green colour scale, adds a colour bar, and saves the vegetation index map as a PNG file.
- [x] `read_values.py`: Reads the DEM, masks NoData pixels, calculates minimum, maximum and mean elevation, and counts NoData cells.
- [x] `reproject_raster.py`: Reprojects the DEM to WGS 84 using bilinear resampling, saves the output, and verifies the new CRS and pixel size.
- [x] `sample_points.py`: Extracts elevation values from the DEM at health facility locations and assigns them to the `elevation_m` column.
- [x] `zonal_stats.py`: Performs zonal statistics to calculate and display the mean elevation for each ward.
- [x] `ndvi_map.png`: Map output from `plot_raster.py`
### Independent Challenge
- [x] `my_index.py`: Applies Landsat surface reflectance scaling, calculates NDVI using the Red and NIR bands, displays NDVI statistics, and saves the output as a GeoTIFF using my downloaded datasets.
- [x] `my_inspect.py`: Inspects my SRTM DEM’s dimensions, band count, data type, CRS, pixel size, spatial bounds, NoData value, and affine transform.
- [x] `my_zonal.py`: Performs zonal statistics to calculate the mean elevation for each ward in Kaltungo LGA and exports the results as a CSV file.
- [x] `my_zonal_stats.csv`: CSV output file from `my_zonal.py` containing mean elevation for each ward
- [x] `my_clip_raster.py`: Dissolves ward boundaries, clips Landsat Red (SR_B4), NIR (SR_B5), and SRTM DEM rasters to Kaltungo LGA, and saves the clipped outputs.
- [x] `my_map.py`: Visualises NDVI for Kaltungo LGA using a red-yellow-green colour scale, adds a colour bar, and saves the map as a PNG file.
- [x] `my_map.png`: Output map made from `my_map.py` visualizing the vegetation index of the LGA


## How to run it
From the repository root:
```bash
uv run Month_3/Week_12/script.py
```

## What I found
- From `my_inspect.py` I checked from the output that `Width(1711) * Resolution(0.0002777777777778146)` == `Right(11.650416666692045) - Left(11.175138888914205)` which is `0.47527777777784`
- The Mean elevation for all the wards Kaltungo LGA is below 600m

## What went wrong and how I fixed it
- I encountered difficulties downloading the DEM from USGS, so I used OpenTopography to obtain the required DEM.

## Month_3/Week_12 Downloaded Datasets and their details
>The Table below describes the exact datasets downloaded and used for Month_3/Week_12 Independent challenge.

| S/N| Product Name| Scene/Tile Name | Date | Cloud Cover |
|---|---|---|---|---|
|1 | Landsat 9 OLI-2/TIRS-2 Collection 2 Level-2 | LC09_L2SP_186053_20260125_20260126_02_T1 | 25/01/2026 | 0.10% |
|2| Shuttle Radar Topography Mission (SRTM GL1) Global 30m | SRTMGL1| 02/11/2000 (Publication date) | N/A |
>The SRTM GL1 Global 30m was downloaded from `Open-Topography`. Reason: USGS was experiencing a downtime at the time of download.
