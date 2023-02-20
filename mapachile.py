# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. 
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx
from mpl_toolkits.basemap import Basemap
from shapely.geometry import Point, Polygon

df = pd.read_csv('/home/debian/tesis/tkinter/csv/indice_riesgo_hidrico_1979-12-15.csv')
df = df[['lat', 'lon', 'ih']]



#kings_county_map = gpd.read_file(r'C:\Users\nicolas.vasquez\Desktop\Tesis\South_America\South_America.shp')
kings_county_map = gpd.read_file('/home/debian/tesis/Shapefile/Regional.shp')

kings_county_map.plot()
kings_county_map.to_crs(epsg=4326).plot()

crs = {'init':'EPSG:4326'}
geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
geo_df = gpd.GeoDataFrame(df,
                          crs = crs, 
                          geometry = geometry)



geo_df['ih']
fig, ax = plt.subplots(figsize = (30,30),zorder=1)
kings_county_map.to_crs(epsg=4326).plot(ax=ax,color='#d66058', alpha=1,edgecolor='k',zorder=2)

cx.add_basemap(ax, crs=geo_df.crs.to_string(), source=cx.providers.Stamen.TonerLabels)
cx.add_basemap(ax, crs=geo_df.crs.to_string(), source=cx.providers.OpenTopoMap)
cx.add_basemap(ax, crs=geo_df.crs.to_string(), source=cx.providers.Stamen.Watercolor)


geo_df.plot(column = 'ih', ax=ax, cmap = 'plasma',alpha=.9,
            legend = True, legend_kwds={'shrink': .9},zorder=3,
            markersize = 150)
 


#cx.add_basemap(ax, crs=geo_df.crs)
#cx.add_basemap(ax, source=cx.providers.OpenTopoMap, zoom=10)
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLabels)
#cx.add_basemap(ax, source=cx.providers.Stamen.Watercolor, zoom=15)
#cx.add_basemap(ax, source=cx.providers.Stamen.TonerLabels, zoom=15)
#cx.add_basemap(ax, source=cx.providers.OpenTopoMap, zoom=12)


ax.set_title('INDICE ESCASEZ HIDRICA CHILE',size=60)
plt.savefig('MapaihChile',dpi=300)

