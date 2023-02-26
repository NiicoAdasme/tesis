from netCDF4 import Dataset

data = Dataset('/home/debian/Downloads/CR2MET_pr_v2.0_mon_1979_2019_005deg.nc')

print(data.variables['time'].units)