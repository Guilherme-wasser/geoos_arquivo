import argparse
import datetime, sys

#python SpillTool.py --initial_date 2023-06-17:01:00 --end_date 2023-06-18:00:00 
#--emission_temporal Instantaneous --lon -48.1225 --lat -27.956389 --oil_class VeryLightOil 
#--point_volume 50

parser = argparse.ArgumentParser()
parser.add_argument("--lon", required=True)
parser.add_argument("--lat", required=True)
parser.add_argument("--initial_date", type=datetime.datetime.fromisoformat, help='ISOformat - YYYY-MM-DD:HH:mm:ss', required=True)
parser.add_argument("--end_date", type=datetime.datetime.fromisoformat, help='ISOformat - YYYY-MM-DD:HH:mm:ss', required=True)
parser.add_argument("--emission_temporal", default = "Instantaneous", choices=['Instantaneous','Continuous'])
parser.add_argument("--spill_duration", type=int, default = 1) #hours - only required if continuous emission
parser.add_argument("--oil_class", default = "MediumOil", choices = ['HeavyOil','MediumOil','LightOil','VeryLightOil'])
parser.add_argument("--point_volume", type=float, default = 30)#m3
parser.add_argument("--nbr_partic", type=int, default = 1000)
parser.add_argument("--diffusion_h", default = 1.0)#m2/s

args = parser.parse_args()

initial_date = args.initial_date
end_date = args.end_date
emission_temporal = args.emission_temporal
lon = args.lon
lat = args.lat
oil_class = args.oil_class
point_volume = args.point_volume
diffusion_h = args.diffusion_h

if emission_temporal == "Continuous":

	stop_partic_emit = initial_date + datetime.timedelta(hours = args.spill_duration)
	flow = point_volume/(args.spill_duration * 3600) #m3/s
	nbr_partic = int(args.nbr_partic/((args.spill_duration * 3600)/900)) #DT_PARTIC = 900 s
	emission_spatial = "Point"
	
elif emission_temporal == "Instantaneous":
	stop_partic_emit = initial_date
	flow = 0
	nbr_partic = args.nbr_partic
	emission_spatial = "Accident"
	
if oil_class == "HeavyOil":
	API                     = 13
	VISCREF                 = 3603
	VISCCINREF              = 3582.65695479991
	MAXVWATERCONTENT        = 80.0
	OWINTERFACIALTENSION    = 20
elif oil_class == "MediumOil":
	API                     = 30
	VISCREF                 = 39
	VISCCINREF              = 43.3421299816612
	MAXVWATERCONTENT        = 70.0
	OWINTERFACIALTENSION    = 20
elif oil_class == "LightOil":
	API                     = 40
	VISCREF                 = 8
	VISCCINREF              = 9.44120065647999
	MAXVWATERCONTENT        = 30.0
	OWINTERFACIALTENSION    = 26
elif oil_class == "VeryLightOil":
	API                     = 50
	VISCREF                 = 2
	VISCCINREF              = 2.49792699584711
	MAXVWATERCONTENT        = 0.0
	OWINTERFACIALTENSION    = 26
