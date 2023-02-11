# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:45:49 2023

@author: Nico
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import calc_ih as ih

data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_merged.nc')

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
time = data.variables['time'][:]
tmin = data.variables['tmin'][:]
tmax = data.variables['tmax'][:]
pr = data.variables['pr'][:]

# Latitud y longitud de la region de Ñuble. Consideramos Chillan como par de coordenadas
lat_nuble = -36.605117255930786
lon_nuble = -72.11779361226445

# Diferencia cuadrada de lat y lon
sq_diff_lat = (lat - lat_nuble)**2
sq_diff_lon = (lon - lon_nuble)**2

#Identificar el indice del minimo valor para lat y lon
min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()

# Input date that u gonna receive 
input_date = '1979-12-15'

# Creamos un dataframe vacio
# months since 1978-12-15
starting_date = data.variables['time'].units[13:23]
ending_date = input_date

date_range = pd.date_range(start= starting_date, end= ending_date, freq= 'M')
#date_range = date_range.date().strftime('%Y-%m-%d')
pos_date = date_range.size + 1

cont = 0

dt = np.arange(0, data.variables['time'].size)

df = pd.DataFrame()

dlat = np.arange(0, data.variables['lat'].size)
dlon = np.arange(0, data.variables['lon'].size)


for i in dlat:
    if i == min_index_lat:
        break
    
    for j in dlon:
        if j == min_index_lon:
           break
        else:
            print('i: '+ str(i))
            print('j: '+ str(j))
            print('cont: '+ str(cont))
            tempmin = tmin[pos_date, i, j]
            tempmax = tmax[pos_date, i, j]
            prec = pr[pos_date, i, j]
            cont = cont + 1
            tprom = (tempmin + tempmax) / 2
            indice_hidrico = ih.diciembre(tprom, prec)
            df = df.append({'lat': lat[i],  'lon': lon[j], 'tmin': tempmin, 'tmax': tempmax, 'pr': prec, 'tprom': tprom, 'ih': indice_hidrico}, ignore_index=True)
            #df['lat'] = lat[i]
            #df['lon'] = lon[j]
            #df['tmin'] = tempmin
            #df['tmax'] = tempmax
            #df['pr'] = prec
            #df['tprom'] = tprom
            #df['ih'] = indice_hidrico
            

df.to_csv('test.csv')

df = pd.read_csv('test.csv')

# remplazamos por NaN aquellos valores que no tienen informacion
df['tmin'] = df['tmin'].replace('--', np.NaN)
df['tmax'] = df['tmax'].replace('--', np.NaN)
df['pr'] = df['pr'].replace('--', np.NaN)        

# Eliminamos aquellos registros que no contengan informacion
df.dropna(inplace=True)

res = df.to_csv('test.csv')
# if res is 'None' (string) value, then the load to csv is succesfully, else it's wrong
# return res 





