import geopandas as gpd
from matplotlib import pyplot as plt

# Load data
provinces = gpd.read_file("./data/provinces26/Province26.shp").to_crs(epsg=3857)
protected_zones = gpd.read_file("./data/parc/Parc.shp").to_crs(epsg=3857)
# Get protected zones common per province
portion_per_province = provinces.overlay(how="intersection", right=protected_zones)

# Compute the spatial intersection between provinces and protected areas
# (this returns the portion of protected zones inside each province)
portion_per_province["occupied_area"] = portion_per_province.area / 1000000
# Retrieve virunga park in touched provinces
print(
    portion_per_province[portion_per_province["NOM_2"] == "Parc National des Virunga"][
        ["NOM_1", "occupied_area"]
    ]
)

fig, axis = plt.subplots()
provinces.plot(ax=axis)
portion_per_province.plot(ax=axis, column=portion_per_province.index, cmap="tab10")


plt.show()

# Ensure that both layers have the same CRS
# fig, ax = plt.subplots()

# assert len(protected_zones) < len(common_zones) , "Not Equal"
# virunga_portion = common_zones[common_zones["NOM_2"] == "Parc National des Virunga"]
# virunga_portion["occupied_area"] = virunga_portion.area/1000000
# print("La plus grande surface est :  ", max(virunga_portion["occupied_area"] ))
# print(virunga_portion[["NOM_1", "occupied_area"]])
# provinces.plot(
#     ax=ax,
#     column=provinces.index,
#     cmap="tab20",
# )
# protected_zones.plot(
#     ax=ax,
#     column=protected_zones.index,
#     cmap="tab10"
# )

# plt.show()


# protected_zones_envlopped = protected_zones.envelope
# protected_zones["envelopped_zones"] = protected_zones_envlopped
# protected_zones["centroid"] = protected_zones.geometry.centroid
# protected_zones.plot()
# new_data_frame =  protected_zonesge.set_geometry("centroid")
# new_data_frame.to_file("provinces_centroid.geojson", driver="GeoJson")
# new_data_frame =  protected_zones.set_geometry("centroid")
# new_data_frame.plot()
# print(protected_zones.head())
# print(protected_zones.geometry.head())
# plt.show()

# protected_zones_m.buffer(1000).plot(edgecolor="red")
# plt.show()

# self_envelopped = provinces.envelope
# provinces_envelopped = gpd.GeoSeries(provinces.union_all().envelope)
# fig, axes  = plt.subplots()
# provinces_envelopped.plot(ax=axes, facecolor="yellow")
# self_envelopped.plot(ax=axes, facecolor="aqua", edgecolor="green")
# provinces.plot(ax=axes, facecolor="red", edgecolor="white")
# plt.show()
