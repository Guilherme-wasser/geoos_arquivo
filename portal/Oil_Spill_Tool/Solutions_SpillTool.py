#Define number of solutions
number_of_solutions = 1
number_of_meteo_solutions = 1

#Define hydrodynamic solutions directory
hydrodynamics_dir = [0]*number_of_solutions
hydrodynamics_dir [0] = ["../GeneralData/Metocean/", "Hydrodynamic_2_Surface.hdf5"]
#hydrodynamics_dir [1] = ["/home/maretec/ftplocal/CEP", "Hydrodynamic_2_Surface.hdf5"]
#hydrodynamics_dir [2] = ["/home/maretec/ftplocal/PR_SC", "Hydrodynamic_2_Surface.hdf5"]
#hydrodynamics_dir [3] = ["/home/maretec/ftplocal/Plataforma_SE", "Hydrodynamic_2_Surface.hdf5"]
#hydrodynamics_dir [4] = ["/home/maretec/ftplocal/CMEMS/Brasil", "CMEMS.hdf5"]

#Define WaterProperties solutions directory
waterproperties_dir = [0]*number_of_solutions
waterproperties_dir [0] = ["../GeneralData/Metocean/", "WaterProperties_2_Surface.hdf5"]

#Define Meteo solutions directory
meteo_dir = [0]*number_of_meteo_solutions
meteo_dir [0] = ["../GeneralData/Metocean/", "wrf.hdf5"]
