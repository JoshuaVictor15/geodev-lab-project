import geopandas as gpd

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer ="Reproject_Kaltungo_Wards")
print("CRS", wards.crs)

print("Suggested UTM:", wards.estimate_utm_crs())
wards_utm = wards.to_crs(epsg=32632)
wards_utm["area_km2"] = wards_utm.area/1000000
print(wards_utm[["wardname", "area_km2"]].head(3))
print("Kaltungo LGA total", round(wards_utm["area_km2"].sum(), 1), "km2")