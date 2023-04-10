# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:45:37 2023

@author: Nico
"""

import netCDF4 as nc
import numpy as np

# Abrir los archivos netCDF y leer las variables

# temperaturas minimas por mes 1979 - 2019
nc_min = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc', 'r')

# temperaturas maxima por mes 1979 - 2019
nc_max = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc', 'r')

# precipitaciones por mes 1979 - 2019
nc_precip = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc', 'r')

temp_min_var = nc_min.variables['tmin']
temp_min_vals = temp_min_var[:]
temp_max_var = nc_max.variables['tmax']
temp_max_vals = temp_max_var[:]
precip_var = nc_precip.variables['pr']
precip_vals = precip_var[:]

# Calcular la temperatura promedio
temp_avg_vals = (temp_min_vals + temp_max_vals) / 2.0


#tprom = (tmin_var + tmax_var) / 2

#ih = tprom - 0.5 * (pr_var - 10)


# Calcular el índice hidrológico
p = 1.0 / (1.0 + np.exp(-12.0 * (precip_vals - 0.15))) # función sigmoide
s = np.maximum(temp_avg_vals - 10.0, 0.0) / np.maximum(temp_avg_vals - 30.0, 0.0) # índice de sequía
h = p * s # índice hidrológico

# Crear un nuevo archivo netCDF y escribir la variable del índice hidrológico
nc_out = nc.Dataset('indice_hidrico.nc', 'w', format='NETCDF4')

time_dim = nc_out.createDimension('time', None)
lat_dim = nc_out.createDimension('lat', temp_min_vals.shape[1])
lon_dim = nc_out.createDimension('lon', temp_min_vals.shape[2])

time_var = nc_out.createVariable('time', 'f4', ('time',))
lat_var = nc_out.createVariable('lat', 'f4', ('lat',))
lon_var = nc_out.createVariable('lon', 'f4', ('lon',))
ih_var = nc_out.createVariable('indice_hidrico', 'f4', ('time', 'lat', 'lon',))

time_var[:] = nc_min.variables['time'][:]
lat_var[:] = nc_min.variables['lat'][:]
lon_var[:] = nc_min.variables['lon'][:]
ih_var[:] = h[:]

nc_out.close()
