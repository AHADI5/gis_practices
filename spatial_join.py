from shapely import  Point, Polygon
import geopandas as gpd

# Load data sets
provinces  =  gpd.read_file("./data/provinces26/Province26.shp").to_crs(epsg=3857)
protected_zones = gpd.read_file("./data/parc/Parc.shp").to_crs(epsg=3857)
protected_zones_with_provinces = provinces.sjoin(protected_zones, predicate="contains")
print(protected_zones_with_provinces)
