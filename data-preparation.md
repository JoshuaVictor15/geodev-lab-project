# CRS and Preparation
**Week3 Deliverables Author: Joshua Victor**

What I reprojected, what I clipped, what I checked, and what I fixed

## Coordinate System Decisions
>CRS Used: EPSG: 32632 (UTM 32N)

**Reason**: My project requires both area and distance calculations, therefore my chosen EPSG: 32632 is in meters and study area falls in UTM zone 32N 

## Data Preparation
|SN |Dataset |Default CRS |Modified CRS |Operation |
|---|---|---|---|---|
|1 |Health Facility Locations| EPSG:4326|EPSG: 32632 | Reprojected to the appropriate CRS, clipped to the study area, and saved as a GeoPackage named [Reproject_Kaltungo_Health_Facilities.gpkg](data/Reproject_Kaltungo_Health_Facilities.gpkg) |
|2 |Road and Path Network| EPSG:4326|EPSG: 32632 |Reprojected to the appropriate CRS, clipped to the study area, and saved as a GeoPackage named [Reproject_Highway_Klt.gpkg](data/Reproject_Highway_Klt.gpkg) |
|3 |Population Distribution Data| EPSG:4326|EPSG: 32632 |Reprojected to the appropriate CRS, clipped to the study area, and saved as a Raster named [Reproject_Population_Kaltungo.tif](data/Reproject_Population_Kaltungo.tif) |
|4 |Ward Boundaries| EPSG:4326|EPSG: 32632 |Reprojected to the appropriate CRS, clipped to the study area, and saved as a Geopackage named [Reproject_Kaltungo_Wards.gpkg](data/Reproject_Kaltungo_Wards.gpkg) |
|5 |Kaltungo LGA Boundary| EPSG:4326|EPSG: 32632 |Selected the study area, reprojected it to the appropriate CRS and saved it as a Geopackage named [Reproject_Kaltungo_LGA.gpkg](data/Reproject_Kaltungo_LGA.gpkg) |
 
  ## The Five Quality Checks

|S/N |Check |Result |Action taken |
|---|---|---|---|
|1 | Are the dataset what I think it is |Yes |None |
|2 |Are there nulls in the fields I need |No |None |
|3 |Are there duplicate features |No |None |
|4 |Are the geometry valid |yes |None |
|5 |Does the coverage span the whole study area |yes |None |

## The Problems Found, and What I did
**Problem** I found no problem in the data based on what i need for my analysis

 
## Analysis Ready Output
- All Source Layers Arrived in EPSG: 4326 - WGS 84
- Study Area: Kaltungo LGA, extracted from GRID3 LGA Boundaries
- All layers clipped to study Area, then reprojected to EPSG: 32632 (UTM 32N)
- Area check: Kaltungo 1000.11 km2, matches the published figure
-  Working files in [data](/data), raw files remain untouched

**Status:** Complete.
>Check [Week 4](month-1-summary.md) Month 1 Spatial Analysis Summary
