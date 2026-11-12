import geopandas as gpd

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)