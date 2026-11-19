import geopandas as gpd
from shapely.geometry import Polygon
from shapely.validation import explain_validity

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(epsg=32632)

print("valid:", wards.is_valid)
print("why:", wards.geometry.apply(explain_validity))

layer = wards.copy()
layer["geometry"] = layer.make_valid()
print("valid now:", layer.is_valid.all())
print((~wards.is_valid).sum(), "invalid")
print("New type:", layer.geom_type.iloc[0])

