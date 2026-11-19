import geopandas as gpd

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(epsg=32632)
facilities = gpd.read_file(
    "data/processed/Reproject_Kaltungo_Health_Facilities.gpkg", layer="Reproject_Kaltungo_Health_Facilities"
).to_crs(epsg=32632)

wards["area_km2"] = wards.area / 1000000

#Buffer operation
reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(5000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1000000

gaps = uncovered[["wardname", "uncovered_km2"]]
result = wards.merge(gaps, on="wardname", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["wardname", "area_km2", "uncovered_km2", "uncovered_pct"]].round((2)))

my_buffer = reach.set_crs(epsg=32632, allow_override=True) 

my_buffer.to_file("data/processed/my_buffer.gpkg", layer= "my_buffer_disslove", driver="GPKG")
