import geopandas as gpd

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards").to_crs(epsg=32632)
facilities = gpd.read_file(
    "data/processed/Reproject_Kaltungo_Health_Facilities.gpkg", layer="Reproject_Kaltungo_Health_Facilities"
).to_crs(epsg=32632)

# count the facilities per ward
joined = gpd.sjoin(facilities, wards[["wardname", "geometry"]], how="inner", predicate="within")

counts = joined.groupby("wardname").size().rename("facility_count").reset_index()
# Merge the counts
wards = wards.merge(counts, on="wardname", how="left")
wards["facility_count"] = wards["facility_count"].fillna(0).astype(int)
print(wards[["wardname", "facility_count"]])
print("Total counted:", wards["facility_count"].sum(), "of", len(facilities))