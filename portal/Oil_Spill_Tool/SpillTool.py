#!/usr/bin/env python3

import re, datetime, os, subprocess, sys, math
from Input_SpillTool import*
from Solutions_SpillTool import*

dirpath = os.getcwd()

input_file = "SpillTool.dat"

exe_dir = (dirpath+"/exe")

# exe_dir = (dirpath+"/MohidLinux")

mohid_log = (exe_dir+"//Mohid.log")

data_dir = (dirpath+"//data")
file_lagrangian = "Lagrangian_1.dat"

#####################################################

def write_date():
	
	os.chdir(data_dir)
	file_name = "Model_1.dat"
	
	with open(file_name) as file:
		file_lines = file.readlines()
		
	number_of_lines = len(file_lines)
	
	for n in range(0,number_of_lines):
		line = file_lines[n]		
		if re.search("^START.+:", line):
			file_lines[n] = "START " + ": " + str(initial_date.strftime("%Y %m %d %H %M")) + " 0\n"

		elif re.search("^END.+:", line):
			file_lines[n] = "END " + ": " + str(end_date.strftime("%Y %m %d %H %M")) + " 0\n"
			
	with open(file_name,"w") as file:
		for n in range(0,number_of_lines) :
			file.write(file_lines[n])

#####################################################
def write_lagrangian():
	
	os.chdir(data_dir)
	
	with open(file_lagrangian) as file:
		file_lines = file.readlines()
		
	number_of_lines = len(file_lines)
	
	for n in range(0,number_of_lines):
		line = file_lines[n]		
		if re.search("^START_PARTIC_EMIT.+:", line):
			file_lines[n] = "START_PARTIC_EMIT " + ": " + str(initial_date.strftime("%Y %m %d %H %M")) + " 0\n"

		elif re.search("^STOP_PARTIC_EMIT.+:", line):
			file_lines[n] = "STOP_PARTIC_EMIT " + ": " + str(stop_partic_emit.strftime("%Y %m %d %H %M")) + " 0\n"

		elif re.search("^FLOW.+:", line):
			file_lines[n] = "FLOW " + ": " + str(flow) + "\n"
			
		elif re.search("^EMISSION_TEMPORAL.+:", line):
			file_lines[n] = "EMISSION_TEMPORAL " + ": " + emission_temporal + "\n"
			
		elif re.search("^EMISSION_SPATIAL.+:", line):
			file_lines[n] = "EMISSION_SPATIAL " + ": " + emission_spatial + "\n"			
			
		elif re.search("^POSITION_COORDINATES.+:", line):
			file_lines[n] = "POSITION_COORDINATES " + ": " + lon + " " + lat + "\n"
			
		elif re.search("^POINT_VOLUME.+:", line):
			file_lines[n] = "POINT_VOLUME " + ": " + str(point_volume) + "\n"
				
		elif re.search("^NBR_PARTIC.+:", line):
			file_lines[n] = "NBR_PARTIC " + ": " + str(nbr_partic) + "\n"
			
		elif re.search("^DIFFUSION_H.+:", line):
			file_lines[n] = "DIFFUSION_H " + ": " + str(diffusion_h) + "\n"	
			
		#Oil properties
		elif re.search("^API.+:", line):
			file_lines[n] = "API " + ": " + str(API) + "\n"
			
		elif re.search("^VISCREF.+:", line):
			file_lines[n] = "VISCREF " + ": " + str(VISCREF) + "\n"
			
		elif re.search("^VISCCINREF.+:", line):
			file_lines[n] = "VISCCINREF " + ": " + str(VISCCINREF) + "\n"
			
		elif re.search("^MAXVWATERCONTENT.+:", line):
			file_lines[n] = "MAXVWATERCONTENT " + ": " + str(MAXVWATERCONTENT) + "\n"
			
		elif re.search("^OWINTERFACIALTENSION.+:", line):
			file_lines[n] = "OWINTERFACIALTENSION " + ": " + str(OWINTERFACIALTENSION) + "\n"
			
		elif re.search("^<EndOrigin>", line):
			end_line = n 
			
	with open(file_lagrangian,"w") as file:
		for n in range(0,end_line+1) :
			file.write(file_lines[n])
		
		
	write_meteo_ocean()
		
#####################################################
def write_meteo_ocean():
	property_name = ["velocity U", "velocity V"]
	with open(file_lagrangian,"a") as file:
		file.write ("\n<BeginMeteoOcean>\n")
		for property in range(0,len(property_name)):
			file.write ("<<BeginProperty>>\nNAME : " + property_name[property] +"\nDESCRIPTION : velocity from operational models\nUNITS : m/s\nMASK_DIM : 3\nFILE_LIST_MODE : 1\n")
			for n in range(0,number_of_solutions):
				file.write("<<<BeginMeteoOceanFiles>>>\n")
				for i in range (0,number_of_days):
					next_initial_date = initial_date + datetime.timedelta(days = i)
					next_end_date = initial_date + datetime.timedelta(days = i+1)
					file.write(hydrodynamics_dir[n][0] + "/" + str(next_initial_date.strftime("%Y%m%d")) + "_" + str(next_end_date.strftime("%Y%m%d") + "/" + hydrodynamics_dir[n][1] + "\n"))
				file.write("<<<EndMeteoOceanFiles>>>\n")
			file.write("<<EndProperty>>\n")

	property_name = ["temperature", "salinity"]
	with open(file_lagrangian,"a") as file:
		for property in range(0,len(property_name)):
			file.write ("<<BeginProperty>>\nNAME : " + property_name[property] +"\nDESCRIPTION : density from operational models\nUNITS : degrees\nMASK_DIM : 3\nFILE_LIST_MODE : 1\n")
			for n in range(0,number_of_solutions):
				file.write("<<<BeginMeteoOceanFiles>>>\n")
				for i in range (0,number_of_days):
					next_initial_date = initial_date + datetime.timedelta(days = i)
					next_end_date = initial_date + datetime.timedelta(days = i+1)
					file.write(waterproperties_dir[n][0] + "/" + str(next_initial_date.strftime("%Y%m%d")) + "_" + str(next_end_date.strftime("%Y%m%d") + "/" + waterproperties_dir[n][1] + "\n"))
				file.write("<<<EndMeteoOceanFiles>>>\n")
			file.write("<<EndProperty>>\n")
			
	property_name = ["wind velocity X", "wind velocity Y"]
	with open(file_lagrangian,"a") as file:
		for property in range(0,len(property_name)):
			file.write ("<<BeginProperty>>\nNAME : " + property_name[property] +"\nDESCRIPTION : wind from operational models\nUNITS : m/s\nMASK_DIM : -99\nFILE_LIST_MODE : 0\n")
			for n in range(0,number_of_meteo_solutions):
				file.write("<<<BeginMeteoOceanFiles>>>\n")
				for i in range (0,number_of_days):
					next_initial_date = initial_date + datetime.timedelta(days = i)
					next_end_date = initial_date + datetime.timedelta(days = i+1)
					file.write(meteo_dir[n][0] + "/" + str(next_initial_date.strftime("%Y%m%d")) + "_" + str(next_end_date.strftime("%Y%m%d") + "/" + meteo_dir[n][1] + "\n"))
				file.write("<<<EndMeteoOceanFiles>>>\n")
				file.write("<<EndProperty>>\n")
		file.write ("<EndMeteoOcean>")
#####################################################

interval = (end_date - initial_date).total_seconds()
number_of_days = math.ceil(interval/86400)
	
write_date()
write_lagrangian()
os.chdir(exe_dir)
print(exe_dir)


output = subprocess.call(["wine", "./MohidWater.exe"])

'''
env = os.environ.copy()
# env.update(LD_LIBRARY_PATH = os.path.dirname(exe_dir))

# output = subprocess.call(["wine", "./MohidWater.exe"])
new_ld_path = exe_dir
env.update(LD_LIBRARY_PATH=new_ld_path)

output = subprocess.call(["./MohidWater"], env=env)
'''

# with open("../res/Run1/Spill.tro", "r") as spilltro:
	# for line in spilltro.readlines():
		# sys.stdout.write(line)
		
