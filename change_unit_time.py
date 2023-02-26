from netCDF4 import num2date,date2num,Dataset
# --------------------
filein = '/home/debian/Downloads/CR2MET_pr_v2.0_mon_1979_2019_005deg.nc'
fileout= '/home/debian/Downloads/CR2MET_pr_v2.0_mon_1979_2019_005deg_EDITED_UNIT_TIME.nc'
newunit = '1978-12-15 00:00:00'
# ------------------------------

ncout = Dataset(filein,'a')
timevar = ncout.variables['time']
timein = timevar[:]
# --------------------------------------------
datesin = num2date(timein,timevar.units)
timevar.setncattr('units',newunit)
timevar[:] = date2num(datesin,newunit)
ncout.close()
# ------------------------