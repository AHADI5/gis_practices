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
