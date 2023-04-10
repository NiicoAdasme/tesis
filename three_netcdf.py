# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:36:44 2023

@author: Nico
"""

import netCDF4 as nc
import xarray as xr

#data = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Proyecto de título\ArchivosNetCDF\CR2\1979-2019\CR2MET_merged.nc')

# temperaturas minimas por mes 1979 - 2019
data_tmin = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc')

# temperaturas maxima por mes 1979 - 2019
data_tmax = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc')

# precipitaciones por mes 1979 - 2019
data_pr = nc.Dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc')

#data = xr.open_dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc', decode_times=False)

#data = xr.open_dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\ih.nc', decode_times=False)

#merged = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\archivo_combinado.nc')

#ih = Dataset(r'C:\Users\Nico\Desktop\UBB\2022-2\Tesis\ih.nc')
#ih.close()

#time = data_tmin['time']
#data_time = data_tmin['time'][:]









