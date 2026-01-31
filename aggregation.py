import geopandas as gpd
from matplotlib import pyplot as plt

protected_zones = gpd.read_file("./data/parc/Parc.shp").to_crs(epsg=3857)
# Adding a column that will store the protected zone number according to REGLEMENT
protected_zones["zone_count"] =  1
# group and count protected zone by REGLEMENT
protected_zones_by_reglement = protected_zones.dissolve(
    by="REGLEMENT", aggfunc={"NOM": lambda x: ",".join(x), "zone_count" : 'count' }
)
print(protected_zones_by_reglement.head()[["zone_count"]])

