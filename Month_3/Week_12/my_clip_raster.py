import geopandas as gpd
import rasterio
from rasterio.mask import mask

with rasterio.open("data/raw/landsat/LC09_L2SP_186053_20260125_20260126_02_T1_SR_B4.TIF") as src:
    wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(src.crs)
    study_area = wards.dissolve()
    clipped, clipped_transform = mask(src, study_area.geometry, crop=True)
    profile = src.profile
    print("Before clip:", src.width, "x", src.height, "pixels")

    profile.update(
        height=clipped.shape[1], width=clipped.shape[2],
        transform=clipped_transform
    )
    with rasterio.open("data/processed/landsat/LC09_L2SP_186053_20260125_20260126_02_T1_SR_B4.TIF", "w", **profile) as dst:
        dst.write(clipped)

    print("After clip:", clipped.shape[2], "x", clipped.shape[1], "pixels")
    print("SR_B4 clipped")

with rasterio.open("data/raw/landsat/LC09_L2SP_186053_20260125_20260126_02_T1_SR_B5.TIF") as src:
    wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(src.crs)
    study_area = wards.dissolve()
    clipped, clipped_transform = mask(src, study_area.geometry, crop=True)
    profile = src.profile
    print("Before clip:", src.width, "x", src.height, "pixels")

    profile.update(
        height=clipped.shape[1], width=clipped.shape[2],
        transform=clipped_transform
    )
    with rasterio.open("data/processed/landsat/LC09_L2SP_186053_20260125_20260126_02_T1_SR_B5.TIF", "w", **profile) as dst:
        dst.write(clipped)

    print("After clip:", clipped.shape[2], "x", clipped.shape[1], "pixels")
    print("SR_B5 clipped")

with rasterio.open("data/raw/SRTMGL1.tif") as src:
    wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(src.crs)
    study_area = wards.dissolve()
    clipped, clipped_transform = mask(src, study_area.geometry, crop=True)
    profile = src.profile
    print("Before clip:", src.width, "x", src.height, "pixels")

    profile.update(
        height=clipped.shape[1], width=clipped.shape[2],
        transform=clipped_transform
    )
    with rasterio.open("data/processed/dem_Kaltungo.tif", "w", **profile) as dst:
        dst.write(clipped)

    print("After clip:", clipped.shape[2], "x", clipped.shape[1], "pixels")
    print("DEM clipped")





