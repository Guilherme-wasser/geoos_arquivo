import numpy as np
import time
import h5py
import netCDF4
from datetime import datetime, timedelta, date



hdf_in = "/opt/geoos/data/UFPR/CEP/Hydrodynamic_2_Surface.hdf5"
nc_out = "/opt/geoos/data/UFPR/CEP/Hydrodynamic_2_Surface.nc"




hdf_file = h5py.File(hdf_in, 'r')


def read_hdf_variables(hdf_file):
    
    """Carrega um arquivo hdf5 no formato utilizado pelo MOHID e extrai dados de latitude, longitude, 
    campo de velocidade e nivel d'agua que serao utilizados na conversao para netcdf"""
    
    TimeList = list(hdf_file['Time'].keys())
    bat = hdf_file['Grid']['Bathymetry'][:].transpose()
    
    dates = list()
    n_lat = hdf_file['Grid']['Latitude'][0, :-1].shape[0]
    n_lon = hdf_file['Grid']['Longitude'][:-1, 0].shape[0]
    u_data, v_data, tide_data = [np.empty(shape=(len(TimeList), n_lat, n_lon)) for i in range(3)]

    
    for x in range(len(TimeList)):
        dates.append(np.array(hdf_file['Time'][TimeList[x]][:]).astype(int))
        #dates[x] = dates[x].astype(int)

        u_data[x] = hdf_file["Results"]["velocity U"][f"velocity U_{TimeList[x][-5:]}"][0].transpose()
        v_data[x] = hdf_file["Results"]["velocity V"][f"velocity V_{TimeList[x][-5:]}"][0].transpose()
        tide_data[x] = hdf_file["Results"]["water level"][f"water level_{TimeList[x][-5:]}"][:].transpose()

        
    for t in range(len(u_data)):
        for lon in range(u_data[0].shape[0]):
            for lat in range(u_data[0].shape[1]):
                if bat[lon,lat] == -99.0:
                    u_data[t][lon,lat] = -99.0
                    v_data[t][lon,lat] = -99.0
                    tide_data[t][lon,lat] = -99.0
    
    
    dates = [datetime(*x) for x in dates]

    return u_data, v_data, tide_data, dates


def write_nc_file(hdf_file, nc_outfile):

    u_data, v_data, tide_data, dates = read_hdf_variables(hdf_file)


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
        
        u = nc_file.createVariable("uo", "f4", ("time", "depth", "latitude", "longitude"), fill_value=-99.0)
        u.long_name = "Eastward velocity"
        u.standard_name = "eastward_sea_water_velocity"
        u.units = "m s-1"
        u.unit_long = "Meters per second"
        u.cell_methods = "area: mean"
        u.add_offset = 0
        #u.scale_factor = 0
        
        v = nc_file.createVariable("vo", "f4", ("time", "depth", "latitude", "longitude"), fill_value=-99.0)
        v.long_name = "Northward velocity"
        v.standard_name = "northward_sea_water_velocity"
        v.units = "m s-1"
        v.unit_long = "Meters per second"
        v.cell_methods = "area: mean"
        v.add_offset = 0
        #v.scale_factor = 0
        
        zos = nc_file.createVariable("zos", "f4", ("time", "latitude", "longitude"), fill_value=-99.0)
        zos.long_name = "Sea surface height"
        zos.standard_name = "sea_surface_height_above_geoid"
        zos.units = "m"
        zos.unit_long = "Meters"
        zos.cell_methods = "area: mean"
        zos.add_offset = 0
        #zos.scale_factor = 0
        
        
        
        #Escrevendo dados
        lat[:] = hdf_file['Grid']['Latitude'][0,:-1].astype('f')
        lon[:] = hdf_file['Grid']['Longitude'][:-1, 0].astype('f')
        depth[0] = 0.5
        
        for ix, data in enumerate(dates):
        
            # Ajustado para incluir minutos na geração do timestamp
            data_tupla = (data.year, data.month, data.day, data.hour, data.minute, data.second, 0, 0, 0)
            data_timestamp = time.mktime(data_tupla) - (60*60*3)  # Ajuste de fuso horário se necessário
            
            nctime[ix] = data_timestamp
    
            matriz = u_data[ix][:, :]
            u[ix, 0, :, :] = matriz[:, :].astype('f')
    
            matriz = v_data[ix][:, :]
            v[ix, 0, :, :] = matriz[:, :].astype('f')
    
            matriz = tide_data[ix][:, :]
            zos[ix, :, :] = matriz[:, :].astype('f')

write_nc_file(hdf_file, nc_out)