# Week 12: Rasters with Rasterio

## What this folder contains
### Guided Scripts
### Guided Scripts
- [x] `clip_raster.py`: Clips the DEM to Ibadan North.
- [x] `inspect_raster.py`: Inspects raster properties and metadata.
- [x] `ndvi.py`: Calculates and exports NDVI.
- [x] `pixel_coords.py`: Converts between pixel indices and spatial coordinates.
- [x] `plot_raster.py`: Visualises NDVI and exports a map.
- [x] `read_values.py`: Calculates elevation statistics and counts NoData cells.
- [x] `reproject_raster.py`: Reprojects the DEM to WGS 84.
- [x] `sample_points.py`: Extracts elevation at health facility locations.
- [x] `zonal_stats.py`: Calculates mean elevation per ward.
- [x] `ndvi_map.png`: NDVI map from `plot_raster.py`.

### Independent Challenge
- [x] `my_index.py`: Calculates and exports NDVI for Kaltungo LGA.
- [x] `my_inspect.py`: Inspects SRTM DEM properties.
- [x] `my_zonal.py`: Calculates and exports mean elevation per ward.
- [x] `my_zonal_stats.csv`: Mean elevation statistics per ward.
- [x] `my_clip_raster.py`: Clips Landsat bands and DEM to Kaltungo LGA.
- [x] `my_map.py`: Visualises and exports the NDVI map.
- [x] `my_map.png`: NDVI map of Kaltungo LGA.

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
