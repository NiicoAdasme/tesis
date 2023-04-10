# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:56:01 2023

@author: Nico
"""

import xarray as xr


ds1 = xr.open_dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmin_v2.0_mon_1979_2019_005deg.nc', decode_times=False)
ds2 = xr.open_dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_tmax_v2.0_mon_1979_2019_005deg.nc', decode_times=False)
ds3 = xr.open_dataset(r'C:\Users\Nico\Desktop\ArchivosNetCDF\CR2\1979-2019\CR2MET_pr_v2.0_mon_1979_2019_005deg.nc', decode_times=False)

combined_ds = xr.merge([ds1['tmin'], ds2['tmax'], ds3['pr']])

combined_ds.to_netcdf('archivo_combinado.nc')

