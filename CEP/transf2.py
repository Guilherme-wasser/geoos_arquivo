import numpy as np
import time
import h5py
import netCDF4
from datetime import datetime, timedelta, date



hdf_in = "/opt/geoos/data/UFPR/CEP/WaterProperties_2_Surface.hdf5"
nc_out = "/opt/geoos/data/UFPR/CEP/WaterProperties_2_Surface.nc"

hdf_file = h5py.File(hdf_in, 'r')

def read_hdf_variables(hdf_file):
    
    """Carrega um arquivo hdf5 no formato utilizado pelo MOHID e extrai dados de latitude, longitude, 
    campo de velocidade e nivel d'agua que serao utilizados na conversao para netcdf"""
    
    TimeList = list(hdf_file['Time'].keys())
    bat = hdf_file['Grid']['Bathymetry'][:].transpose()
    
    dates = list()
    n_lat = hdf_file['Grid']['Latitude'][0, :-1].shape[0]
    n_lon = hdf_file['Grid']['Longitude'][:-1, 0].shape[0]
    temperature_data, salinity_data = [np.empty(shape=(len(TimeList), n_lat, n_lon)) for i in range(2)]

    
    for x in range(len(TimeList)):
        dates.append(np.array(hdf_file['Time'][TimeList[x]][:]).astype(int))
        #dates[x] = dates[x].astype(int)

        salinity_data[x] = hdf_file["Results"]["salinity"][f"salinity_{TimeList[x][-5:]}"][0].transpose()
        temperature_data[x] = hdf_file["Results"]["temperature"][f"temperature_{TimeList[x][-5:]}"][0].transpose()
        
    for t in range(len(salinity_data)):
        for lon in range(salinity_data[0].shape[0]):
            for lat in range(salinity_data[0].shape[1]):
                if bat[lon,lat] == -99.0:
                    temperature_data[t][lon,lat] = -99.0
                    salinity_data[t][lon,lat] = -99.0
    
    dates = [datetime(*x) for x in dates]

    return temperature_data, salinity_data, dates


def write_nc_file(hdf_file, nc_outfile):

    temperature_data, salinity_data, dates = read_hdf_variables(hdf_file)


    with netCDF4.Dataset(nc_outfile, "w") as nc_file:
        
        nc_file.createDimension("latitude",   hdf_file['Grid']['Latitude'][0, :-1].shape[0])
        nc_file.createDimension("longitude", hdf_file['Grid']['Longitude'][:-1, 0].shape[0])
        nc_file.createDimension("depth", 1)
        nc_file.createDimension("time", len(dates))
        
        lat = nc_file.createVariable("latitude", 'f4', ("latitude",))
        lat.units = 'degrees_north'
        lat.unit_long = "Degrees North"
        lat.long_name = "Latitude"
        lat.standard_name = "latitude"
        lat.axis = "Y"
        
        lon = nc_file.createVariable("longitude", 'f4', ("longitude",))
        lon.units = 'degrees_east'
        lon.unit_long = "Degrees East"
        lon.long_name = "Longitude"
        lon.standard_name = "longitude"
        lon.axis = "X"
        
        depth = nc_file.createVariable("depth", 'f4', ("depth",))
        depth.units = "m"
        depth.unit_long = "Meters"
        depth.long_name = "Depth"
        depth.standard_name = "depth"
        depth.axis = "Z"
        depth.positive = "down"
        depth._CoordinateAxisType = "Height"
        depth._CoordinateZisPositive = "down"
        
        nctime = nc_file.createVariable("time", "f8", ("time",))
        nctime.long_name = "Time (seconds since 1970-01-01 00:00:00 UTC)"
        nctime.calendar = "gregorian"
        nctime.standard_name = "time"
        nctime.units = "seconds since 1970-01-01 00:00:00 UTC"
        nctime.axis = "T"
        nctime._CoordinateAxisType = "Time"
        
        salinity = nc_file.createVariable("salinity", "f4", ("time", "latitude", "longitude"), fill_value=-99.0)
        salinity.long_name = "sea water salinity"
        salinity.standard_name = "sea_water_salinity"
        salinity.units = "PSU"
        salinity.unit_long = "PSU"
        salinity.cell_methods = "area: mean"
        salinity.add_offset = 0
        #salinity.scale_factor = 0

        temperature = nc_file.createVariable("temperature", "f4", ("time", "latitude", "longitude"), fill_value=-99.0)
        temperature.long_name = "sea water temperature"
        temperature.standard_name = "sea_water_temperature"
        temperature.units = "degC"
        temperature.unit_long = "degrees Celsius"
        temperature.cell_methods = "area: mean"
        temperature.add_offset = 0
        #temperature.scale_factor = 0        
        
        
        #Escrevendo dados
        lat[:] = hdf_file['Grid']['Latitude'][0,:-1].astype('f')
        lon[:] = hdf_file['Grid']['Longitude'][:-1, 0].astype('f')
        depth[0] = 0.5
        
        for ix, data in enumerate(dates):
        
            data_tupla = (data.year, data.month, data.day, data.hour, data.second, data.microsecond, 0, 0, 0)
            data_timestamp = time.mktime(data_tupla) - (60*60*3)
    
            nctime[ix] = data_timestamp
    
            matriz = temperature_data[ix][:, :]
            temperature[ix, :, :] = matriz[:, :].astype('f')
    
            matriz = salinity_data[ix][:, :]
            salinity[ix, :, :] = matriz[:, :].astype('f')

write_nc_file(hdf_file, nc_out)