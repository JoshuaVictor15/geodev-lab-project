
import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards")
buffer = gpd.read_file("data/processed/my_buffer.gpkg", layer="my_buffer_disslove")
facilities = gpd.read_file("data/processed/Kaltungo_Health_Facilities.gpkg", layer="Kaltungo_Health_Facilities")

fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
buffer.plot(ax=ax, color="#E6F2F3", edgecolor="#E7E4DF" )
facilities.plot(ax=ax, color="#E08986", markersize=18)
ax.set_title("Health Facilities 5KM Dissolve Buffer in Kaltungo LGA")
ax.set_axis_off()

fig.savefig("Month_3/Week_11/my_buffer_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
