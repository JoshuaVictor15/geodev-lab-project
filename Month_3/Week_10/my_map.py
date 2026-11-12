
import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/Reproject_Kaltungo_Wards.gpkg", layer="Reproject_Kaltungo_Wards")
facilities = gpd.read_file("data/processed/Kaltungo_Health_Facilities.gpkg", layer="Kaltungo_Health_Facilities")

fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#050A0A")
facilities.plot(ax=ax, color="#E08986", markersize=18)
ax.set_title("Health Facilities in Kaltungo LGA")
ax.set_axis_off()

fig.savefig("Month_3/Week_10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
