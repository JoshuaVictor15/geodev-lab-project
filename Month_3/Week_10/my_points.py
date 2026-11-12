
import pandas as pd
import geopandas as gpd

table = pd.read_csv("data/raw/Kaltungo_Health_Facilities_raw.csv")
print(table.head(5))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326"
)

facilities = facilities.to_crs(epsg=32632)

print(facilities.head(5))
print(facilities.crs)

facilities.to_file(
    "data/processed/Kaltungo_Health_Facilities.gpkg",
    layer="Kaltungo_Health_Facilities"
)

print("Saved", len(facilities), "facilities")
